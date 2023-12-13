#version 3.7;
#include "colors.inc"

global_settings {
    assumed_gamma 1.7
}

background {color White}

camera {
    location <0, 1, -1>
    look_at <0, 0, 2>
    up y
    right x
}

#macro mypigment(filename)
    pigment {
        image_map {
            png filename
            interpolate 3
        }
        rotate 90*x - 90*y
        scale 2
        translate x+z
    }
#end

#declare myplot = box {
    <-1, -0.0001, -1>, <1, 0.0001, 1>

    finish {
        ambient White
        emission 0
    }
}

#declare delta = 0.4;
#declare i = 0;

#while (i < 4)
    #declare filename = concat("texture", str(i,1,0), ".png")
    object {
        myplot
        mypigment(filename)
        translate 2*z + (i * delta - 0.9) * y// + (i * delta * 0.25 - 0.2)* x
    }
    #declare i = i + 1;
#end
