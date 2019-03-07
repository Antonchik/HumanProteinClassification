
import data_utils as du


class DataLoader:
    def __init__(self, images_dir: str, labels_file: str):
        self.directory = images_dir
        self.file = labels_file
        self.images = []
        self.labels = []
        self.read_data()

    def read_data(self):
        self.labels, self.images = du.read_data(self.file, self.directory)

    def get_data(self):
        return zip(self.images, self.labels)
