from loader import DataLoader
from data_utils import show_image, open_image


train_images_dir = \
    "X:\\DataScience\\human-protein-atlas-image-classification\\train"
train_labels_file = \
    "X:\\DataScience\\human-protein-atlas-image-classification\\train.csv"


if __name__ == "__main__":
    print('start')
    loader = DataLoader(train_images_dir, train_labels_file)
    files = loader.labels.keys()
    for file in files:
        colors = loader.images[file].keys()
        print(loader.labels[file])
        for color in colors:
            _image = loader.images[file][color]
            show_image(open_image(_image, opencv=False), opencv=False)
    print('finish')
