# What does it do?
imgflip is a small program that flips and mirrors images. The goal is to make it as script compatible as possible, meaning that it supports chaining and piping.

# How does it do that?
imgflip is a very small python program. It uses OpenCV to load images and access their pixelvalues.

# SYNOPSIS:

`imgflip -[v,h,r,l,r] [INPUT_IMAGE] [OUTPUT_IMAGE]`

## You can chain these commands in order.
- `-v` to mirror the image vertically
- `-h` to mirror the image horizontally
- `-r` to rotate 90 degrees to the left (clockwise)
- `-l` to rotate 90 degrees to the right (counter clockwise)
- `-a` to rotate 180 degrees

# EXAMPLE:
Mirror the image horizontally and then rotate it 90 degrees to the right (clockwise).
`imgflip -hr`
