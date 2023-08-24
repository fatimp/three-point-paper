#!/bin/sh

convert -composite -gravity center -geometry 1500x1200+400+150 \
        ../images/balls-s3.png ../images/balls-s3-zoom.png ../images/balls-s3-result.png
