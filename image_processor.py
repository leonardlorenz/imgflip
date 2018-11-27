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
        output_img = np.zeros((height, width, channels), np.uint8)
        j = width - 1
        for y in range(0, width):
            i = 0
            for x in range(0, height):
                output_img[i, j] = img[x, y]
                i += 1
            j -= 1
        return output_img

    def mirror_vertical(self, img):
        height, width, channels = img.shape
        output_img = np.zeros((height, width, channels), np.uint8)
        j = 0
        for y in range(0, width):
            i = height - 1
            for x in range(0, height):
                output_img[i, j] = img[x, y]
                i -= 1
            j += 1
        return output_img

    def rotate_90(self, img):
        height, width, channels = img.shape
        output_img = np.zeros((width, height, channels), np.uint8)
        j = 0
        for y in range(0, width):
            i = 0
            for x in range(0, height):
                output_img[j, i] = img[x, y]
                i += 1
            j += 1
        return output_img

    def rotate_minus_90(self, img):
        height, width, channels = img.shape
        output_img = np.zeros((width, height, channels), np.uint8)
        j = width - 1
        for y in range(0, width):
            i = 0
            for x in range(0, height):
                output_img[j, i] = img[x, y]
                i += 1
            j -= 1
        return output_img

    def rotate_180(self, img):
        height, width, channels = img.shape
        output_img = np.zeros((height, width, channels), np.uint8)
        j = width - 1
        for y in range(0, width):
            i = height - 1
            for x in range(0, height):
                output_img[i, j] = img[x, y]
                i -= 1
            j -= 1
        return output_img
