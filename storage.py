import json

# template for Storage


class Storage:

    # static method as we don't need of state for saving files purposes
    @staticmethod
    # method to save file and data
    def save_data(file_path, data):
        with open(file_path, 'w') as file:
            json.dump(data, file)

    # static method as we don't need of state for saving files purposes
    @staticmethod
    # method to load/read file and data
    def load_data(file_path):
        try:
            with open(file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []
