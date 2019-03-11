import os
from PIL import Image
import cv2 as cv
import numpy as np
import pandas as pd


cv.setNumThreads(0)


def read_csv(file_name):
    csv_data = pd.read_csv(file_name)
    return csv_data


def normalize_image(image):
    return np.divide(image, 255)


def resize__image(image, new_size=(128, 128)):
    return cv.resize(image, new_size)


def open_image(image_file: str, opencv=True):
    if opencv:
        img = _open_image_cv(image_file)
    else:
        image = Image.open(image_file)
        img = np.asarray(image)
    return img


def show_image(image, opencv=True, window_name='image'):
    if opencv:
        _show_image_cv(window_name, image)
    else:
        Image.fromarray(image).show()


def _open_image_cv(image_file: str):
    img = cv.imread(image_file, 0)
    return img


def _show_image_cv(window_name: str, image):
    cv.imshow(window_name, image)


def one_hot_encoder(labels, categories_num):
    lst = np.zeros(categories_num)
    for label in labels.split(' '):
        index = int(label)
        lst[index] = 1
    return lst


def read_data(file, directory, qty, cat_num=28):
    labels = read_csv(file)[:qty] if qty else read_csv(file)
    targets = []
    images = []
    for image_id, target in zip(labels['Id'], labels['Target']):
        targets.append(one_hot_encoder(target, cat_num))
        images.append(read_all_image_channels(directory, image_id))
    targets = np.array(targets)
    images = np.array(images, dtype=np.uint8)
    return targets, images


def read_image(images_dir, image_id, color):
    image_name = image_id + '_' + color + '.png'
    image_path = os.path.join(images_dir, image_name)
    image = open_image(image_path)
    # image = image_path
    return image


def read_all_image_channels(images_dir, image_id):
    colors = ['red', 'green', 'blue', 'yellow']
    image = np.empty((512, 512, 4))
    for color in colors:
        channel_image = read_image(images_dir, image_id, color)
        image[:, :, colors.index(color)] = channel_image
    return image

