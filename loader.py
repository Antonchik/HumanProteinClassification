
import data_utils as du


class DataLoader:
    def __init__(self, images_dir: str, labels_file: str, qty=None):
        self.directory = images_dir
        self.file = labels_file
        self.images = []
        self.labels = []
        self.read_data(qty)

    def read_data(self, qty):
        self.labels, self.images = du.read_data(self.file, self.directory, qty)

    def get_data(self):
        return zip(self.images, self.labels)
