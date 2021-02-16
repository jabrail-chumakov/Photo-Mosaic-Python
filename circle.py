import numpy as np
import argparse
import cv2
import glob
from itertools import product


def settings():
    parser = argparse.ArgumentParser("Project 1")
    parser.add_argument("--input", type=str, default="export/input.jpg", help="Path to input")
    parser.add_argument("--output", type=str, default="export/output.jpg", help="Path to output")
    parser.add_argument("--pool", type=str, default="dataset", help="Path to dataset")
    parser.add_argument("--stride", type=int, default=40, help="Size of small image")
    args = parser.parse_args()
    return args


def get_settings(path, size):
    images = []
    avg_colors = []
    for image_path in glob.glob("{}/*.png".format(path)) + glob.glob("{}/*.jpg".format(path)):
        image = cv2.imread(image_path, cv2.IMREAD_COLOR)
        image = cv2.resize(image, (size, size))
        images.append(image)
        avg_colors.append(np.sum(np.sum(image, axis=0), axis=0) / (size ** 2))
    return images, np.array(avg_colors)

def ciclelify(src):
    cv2.circle(src, round(opt.stride/2),round(opt.stride/2),round(opt.stride/2), (0,0,0), -1)

def main(opt):
    input_image = cv2.imread(opt.input, cv2.IMREAD_COLOR)
    height, width, num_channels = input_image.shape
    blank_image = np.zeros((height, width, 3), np.uint8)
    images, avg_colors = get_settings(opt.pool, opt.stride)
    for i, j in product(range(int(width / opt.stride)), range(int(height / opt.stride))):
        partial_input_image = input_image[j * opt.stride: (j + 1) * opt.stride,
                              i * opt.stride: (i + 1) * opt.stride, :]
        partial_avg_color = np.sum(np.sum(partial_input_image, axis=0), axis=0) / (opt.stride ** 2)
        distance_matrix = np.linalg.norm(partial_avg_color - avg_colors, axis=1)
        idx = np.argmin(distance_matrix)

        radius = 100.0/(distance_matrix[idx]/2+100)
        circle = np.zeros((round(opt.stride), round(opt.stride)), dtype=images[idx].dtype)
        cv2.circle(circle, (round(opt.stride/2),round(opt.stride/2)) ,round(radius*opt.stride/2), 1, -1)
        masked_data = images[idx] * circle[..., np.newaxis]

        blank_image[j * opt.stride: (j + 1) * opt.stride, i * opt.stride: (i + 1) * opt.stride, :] = masked_data
    cv2.imwrite(opt.output, blank_image)

if __name__ == '__main__':
    opt = settings()
    main(opt)
