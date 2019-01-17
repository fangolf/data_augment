# -*- coding: utf-8 -*-
import numpy as np
import random
import cv2


def addGaussionBlur(image, kenel_size, sigma):
    return cv2.GaussianBlur(image, (kenel_size, kenel_size), sigma)


def shelter(image, center_x_range, center_y_range, size_x_range, size_y_range):
    center_x = random.randint(center_x_range[0], center_x_range[1])
    center_y = random.randint(center_y_range[0], center_y_range[1])
    size_x = random.randint(size_x_range[0], size_x_range[1])
    size_y = random.randint(size_y_range[0], size_y_range[1])
    top = int(max(0, center_y - size_y / 2))
    left = int(max(0, center_x - size_x / 2))
    bottom = int(min(image.shape[0] - 1, center_y + size_y / 2))
    right = int(min(image.shape[1] - 1, center_x + size_x / 2))
    c1 = random.randint(0, 255)
    c2 = random.randint(0, 255)
    c3 = random.randint(0, 255)
    cv2.rectangle(image, (left, top), (right, bottom), (c1, c2, c3), -1)


def noise(image, noise_ratial_range):
    height = image.shape[0]
    width = image.shape[1]
    pix_num = height * width
    noise_ratial = random.uniform(noise_ratial_range[0], noise_ratial_range[1])
    noise_num = int(noise_ratial * pix_num)
    noises = random.sample(range(pix_num), noise_num)
    for i in noises:
        c1 = random.randint(0, 255)
        c2 = random.randint(0, 255)
        c3 = random.randint(0, 255)
        image[int(i / width)][i % width] = (c1, c2, c3)


if __name__ == "__main__":
    srcImage = cv2.imread("lena.jpg")
    cv2.namedWindow("Original image")
    cv2.imshow("Original image", srcImage)
    grayImage = srcImage
    grayImage = cv2.resize(grayImage, (112, 112))

    noise(grayImage, (0, 0.05))  # 添加10%的高斯噪声
    shelter(grayImage, (0, 112), (0, 112), (0, 30), (0, 30))
    cv2.imshow("Add_GaussianNoise Image", grayImage)
    cv2.imwrite("Glena.jpg ", grayImage)

    # SaltAndPepper_noiseImage = SaltAndPepper(grayImage, 0.1)  # 再添加10%的椒盐噪声
    # cv2.imshow("Add_SaltAndPepperNoise Image", SaltAndPepper_noiseImage)

    cv2.waitKey(0)
    cv2.destroyAllWindows()