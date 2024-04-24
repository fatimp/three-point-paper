module Shit
import CorrelationFunctions.Utilities as U
using NPZ
using StaticArrays

const sides = [300, 600]

function foo!()
    for side in sides
        data = npzread("lisp/data-0-$(side).npy")
        for s in 1:9
            angle = s/10 * π/4
            rot = U.make_rotation(SVector(0, 0, 1), angle)
            datarot = U.rotate_array(data, rot, U.Torus())
            npzwrite("julia/data-$(s)-$(side).npy", datarot)
        end
    end
end

end
