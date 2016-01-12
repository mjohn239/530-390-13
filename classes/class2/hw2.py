#!/usr/bin/env python
import improc

img = improc.read("gilman-hall.jpg")

# find max values
image_max = improc.max_img(img)

# find min values
image_min = improc.min_img(img)

# convert to grayscale
img_gray_lit = improc.rgb_to_gray_lit(image_min, image_max)

# show images
improc.show_n([img,img_gray_lit])
