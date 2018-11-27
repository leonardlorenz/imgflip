#!/bin/python

import sys
import image_processor

def main():
    if !(len(sys.argv) >= 4):
        print_help()
        sys.exit(0)
    else:
        '''
        process commandline parameters
        '''
        do_mirror_horizontal = False
        do_mirror_vertical = False
        do_rotate_180 = False
        do_rotate_90 = False
        do_rotate_minus_90 = False

        if sys.argv[1].startswith("-"):
            input_path = sys.argv[2]
            options = sys.argv[1].strip("-")
            for i in range(0, len(options)):
                # mirror image
                if options[i] == "m":
                    do_mirror_horizontal = True
                if options[i] == "v":
                    do_mirror_vertical = True
                if options[i] == "r"
                    do_rotate_90 = True
                if options[i] == "l"
                    do_rotate_minus_90 = True
                if options[i] == "a":
                    do_rotate_180 = True
        processor = image_processor.image_processor(do_mirror_horizontal, do_mirror_vertical, do_rotate_90, do_rotate_minus_90, do_rotate_180)
        processor.process_image()

    def print_help():
        print("imgflip -vhrlr input_img output_img")
        print("\n")
        print("-v to mirror the image vertically")
        print("-h to mirror the image horizontally")
        print("-r to rotate 90 degrees to the left (clockwise)")
        print("-l to rotate 90 degrees to the right (counter clockwise)")
        print("-a to rotate 180 degrees")
        print("\n")
        print("You can chain these commands in order.")
        print("For example setting the flags: \"-hr\"\n will mirror the image horizontally and then rotate it 90 degrees to the right.")

if __name__ == "__main__":
    main()
