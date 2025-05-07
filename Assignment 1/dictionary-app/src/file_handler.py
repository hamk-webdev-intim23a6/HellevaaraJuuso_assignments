import json

class FileHandler:
    @staticmethod
    def load_dictionary(file_path):
        try:
            with open(file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"File '{file_path}' not found. Starting with default dictionary.")
            return {}
        except json.JSONDecodeError:
            print(f"File '{file_path}' is not a valid JSON file. Starting with default dictionary.")
            return {}
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return {}

    @staticmethod
    def save_dictionary(file_path, dictionary):
        try:
            with open(file_path, 'w') as file:
                json.dump(dictionary, file, indent=4)
        except Exception as e:
            print(f"An error occurred while saving to '{file_path}': {e}")