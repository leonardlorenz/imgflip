import numpy as np
import cv2 as cv

class image_processor(input_path, output_path):

    def image_processor(self, do_mirror_horizontal, do_mirror_vertical, do_rotate_90, do_rotate_minus_90, do_rotate_180):
        self.do_mirror_horizontal = do_mirror_horizontal
        self.do_mirror_vertical = do_mirror_vertical
        self.do_rotate_90 = do_rotate_90
        self.do_rotate_minus_90 = do_rotate_minus_90
        self.do_rotate_180 = do_rotate_180

    def process_image(self):
        img = cv.imread(input_path)
        if self.do_mirror_horizontal == True:
            img = mirror_horizontal(img):
        if self.do_mirror_vertical == True:
            img = mirror_vertical(img)
        if self.do_rotate_90== True:
            img = rotate_90(img)
        if self.do_rotate_minus_90 == True:
            img = rotate_minus_90(img)
        if self.do_rotate_180 == True:
            img = rotate_180(img)
        cv.imwrite(output_path, img)
        print("Wrote flipped image to " + output_path)

    def mirror_horizontal(img):
        height, width, channels = img.shape
        output_img = np.zeros((width, height, channels), np.uint8)
        x = 0
        for i in range(0, width):
            y = height - 1
            for j in range(0, height):
                #print(i, j, x, y)
                output_img[i,j] = img[x,y]
                y -= 1
            x += 1
        return output_img

    def mirror_vertical(img):
        height, width, channels = img.shape
        output_img = np.zeros((width, height, channels), np.uint8)
        x = width
        for i in range(0, width):
            y = height
            for j in range(0, height):
                #print(i, j, x, y)
                output_img[i,j] = img[x,y]
                y -= 1
            x -= 1
        return output_img

    def rotate_90(img):
        continue
    def rotate_minus_90(img):
        continue
    def rotate_180(img):
        continue

