from loader import DataLoader
from data_utils import show_image, open_image, cv
from tqdm import tqdm


train_images_dir = \
    "X:\\DataScience\\human-protein-atlas-image-classification\\train"
train_labels_file = \
    "X:\\DataScience\\human-protein-atlas-image-classification\\train.csv"


if __name__ == "__main__":
    print('start')
    loader = DataLoader(train_images_dir, train_labels_file)
    for images, label in loader.get_data():
        colors = ['red', 'green', 'blue', 'yellow']
        print(label)
        for color in colors:
            _image = images[color]
            # show_image(_image)                          # show opened image
            show_image(open_image(_image))            # open and show image
            cv.waitKey(0)
    print('finish')

    ### === Speed testing === ###
    loader = DataLoader(train_images_dir,
                        train_labels_file)  # It is your class for loading data

    for images, label in tqdm(loader.get_data()):
        pass
