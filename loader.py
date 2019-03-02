
import data_utils as du


class DataLoader:
    def __init__(self, images_dir: str, labels_file: str):
        self.images_dir = images_dir
        self.labels_file = labels_file
        self.images = {}
        self.labels = {}
        self.read_data()

    def read_data(self):
        self.images = du.read_images(self.images_dir)
        self.labels = du.read_labels(self.labels_file)

    def get_data(self):
        return self.images, self.labels


# a = DataLoader(
#     r"X:\DataScience\human-protein-atlas-image-classification\train",
#     r"X:\DataScience\human-protein-atlas-image-classification\train.csv"
# )



