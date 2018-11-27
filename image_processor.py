import numpy as np
import cv2 as cv

class image_processor():
    def __init__(self,
            input_path,
            output_path,
            do_mirror_horizontal,
            do_mirror_vertical,
            do_rotate_90,
            do_rotate_minus_90,
            do_rotate_180):
        self.input_path = input_path
        self.output_path = output_path
        self.do_mirror_horizontal = do_mirror_horizontal
        self.do_mirror_vertical = do_mirror_vertical
        self.do_rotate_90 = do_rotate_90
        self.do_rotate_minus_90 = do_rotate_minus_90
        self.do_rotate_180 = do_rotate_180

    def process_image(self):
        img = cv.imread(self.input_path)

        if self.do_mirror_horizontal == True:
            img = self.mirror_horizontal(img)

        if self.do_mirror_vertical == True:
            img = self.mirror_vertical(img)

        if self.do_rotate_90 == True:
            img = self.rotate_90(img)

        if self.do_rotate_minus_90 == True:
            img = self.rotate_minus_90(img)

        if self.do_rotate_180 == True:
            img = self.rotate_180(img)

        cv.imwrite(self.output_path, img)
        print("Wrote flipped image to " + self.output_path)

    def mirror_horizontal(self, img):
        height, width, channels = img.shape
        output_img = np.zeros((width, height, channels), np.uint8)
        x = 0
        for i in range(0, width):
            y = height - 1
            for j in range(0, height):
                output_img[i,j] = img[x,y]
                y -= 1
            x += 1
        return output_img

    def mirror_vertical(self, img):
        height, width, channels = img.shape
        output_img = np.zeros((width, height, channels), np.uint8)
        x = width
        for i in range(0, width):
            y = height
            for j in range(0, height):
                output_img[i,j] = img[x,y]
                y -= 1
            x -= 1
        return output_img

    def rotate_90(self, img):
        height, width, channels = img.shape
        output_img = np.zeros((height, width, channels), np.uint8)
        x = width - 1
        for i in range(0, width):
            y = 0
            for j in range(0, height):
                output_img[x,y] = img[i,j]
                y += 1
            y -= 1
        return output_img

    def rotate_minus_90(self, img):
        print("nothing")

    def rotate_180(self, img):
        print("nothing")
