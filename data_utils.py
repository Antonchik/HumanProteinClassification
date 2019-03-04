import os
from PIL import Image
import cv2 as cv
import csv

file_path = r"X:\DataScience\human-protein-atlas-image-classification\train.csv"
dir_path = r"X:\DataScience\human-protein-atlas-image-classification\train"


def open_image(image_file: str, opencv=False):
    img = _open_image_cv(image_file) if opencv else Image.open(image_file)
    return img


def show_image(image, opencv=False, window_name='image'):
    _show_image_cv(window_name, image) if opencv else image.show()


def _open_image_cv(image_file: str):
    img = cv.imread(image_file)
    return img


def _show_image_cv(window_name: str, image):
    cv.imshow(window_name, image)


def read_labels(file=file_path):
    labels_dict = {}
    with open(file, "r") as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            if row[1].isalpha():                    # skip title row
                continue
            labels = row[1].split(' ')
            one_hot_labels = [0 for _ in range(28)]
            for label in labels:
                one_hot_labels[int(label)] = 1
            labels_dict[row[0]] = one_hot_labels
    return labels_dict


def read_images(directory=dir_path):
    files = sorted(os.listdir(directory))
    images = {}
    for file in files:
        splited = file.split('_')
        image, color = splited[0], splited[1][:-4]
        pic = open_image('\\'.join([directory, file]))      # open image
        # pic = '\\'.join([directory, file])                # save link to image
        if image not in images:
            images.update({image: {color: pic}})
        else:
            images[image].update({color: pic})
    return images


# print(read_images())

# print(read_labels())
