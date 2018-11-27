# What does it do?
imgflip is a small program that flips and mirrors images. The goal is to make it as scriptable as possible, meaning that it supports chaining and piping.

# How does it do that?
imgflip is a very small python program. It uses OpenCV to load images and to access their pixel values.

# Synopsis:

`imgflip -[h,v,r,l,r] [INPUT_IMAGE] [OUTPUT_IMAGE]`

## You can chain these commands in order.
- `-h` to mirror the image horizontally
- `-v` to mirror the image vertically
- `-r` to rotate 90 degrees to the right (clockwise)
- `-l` to rotate 90 degrees to the left (counter clockwise)
- `-a` to rotate 180 degrees
- `--help` to print the help message (this one)

# Examples:
Mirror the image horizontally and then rotate it 90 degrees to the right (clockwise).\
`imgflip -hr image.png output.jpg`\
Mirror the image vertically and then rotate it 180 degrees.\
`imgflip -va image.jpg output.png`
