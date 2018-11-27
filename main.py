#!/bin/python

import sys
import image_processor

def main():
    if not (len(sys.argv) >= 4):
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
        input_path = ""
        output_path = ""

        if sys.argv[1].startswith("-"):
            input_path = sys.argv[2]
            output_path = sys.argv[3]
            options = sys.argv[1].strip("-")
            for i in range(0, len(options)):
                # mirror image
                if options[i] == "m":
                    do_mirror_horizontal = True
                if options[i] == "v":
                    do_mirror_vertical = True
                if options[i] == "r":
                    do_rotate_90 = True
                if options[i] == "l":
                    do_rotate_minus_90 = True
                if options[i] == "a":
                    do_rotate_180 = True
                if options[i] == "h":
                    print_help()
                    sys.exit(0)

        processor = image_processor.image_processor(
                input_path,
                output_path,
                do_mirror_horizontal,
                do_mirror_vertical,
                do_rotate_90,
                do_rotate_minus_90,
                do_rotate_180)
        processor.process_image()

def print_help():
    print("\nSYNOPSIS:\n")
    print("\timgflip -[v,h,r,l,r] [INPUT_IMAGE] [OUTPUT_IMAGE]\n")
    print("You can chain these commands in order.")
    print("\t-v to mirror the image vertically")
    print("\t-h to mirror the image horizontally")
    print("\t-r to rotate 90 degrees to the left (clockwise)")
    print("\t-l to rotate 90 degrees to the right (counter clockwise)")
    print("\t-a to rotate 180 degrees")
    print("\nEXAMPLE:")
    print("\tMirror the image horizontally and then rotate it 90 degrees to the right (clockwise).")
    print("\timgflip -hr\n")

if __name__ == "__main__":
    main()
