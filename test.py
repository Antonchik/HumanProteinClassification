from loader import DataLoader
from data_utils import show_image, open_image, cv
from tqdm import tqdm


train_images_dir = \
    "X:\\DataScience\\human-protein-atlas-image-classification\\train"
train_labels_file = \
    "X:\\DataScience\\human-protein-atlas-image-classification\\train.csv"


if __name__ == "__main__":
    print('start')
    loader = DataLoader(train_images_dir, train_labels_file, qty=10)
    for image, label in loader.get_data():
        print(label)
        show_image(image)                          # show opened image
        # show_image(open_image(_image))            # open and show image
        cv.waitKey(0)
    print('finish')

    ### === Speed testing === ###
    loader = DataLoader(train_images_dir,
                        train_labels_file, qty=10)  # It is your class for loading data

    for images, label in tqdm(loader.get_data()):
        pass
