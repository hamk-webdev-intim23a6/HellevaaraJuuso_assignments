import json
from dictionary import Dictionary
from file_handler import FileHandler
from utils import display_error, prompt_user

def main():
    dictionary = Dictionary()
    file_handler = FileHandler()
    
    # Load the dictionary from a JSON file
    try:
        dictionary_data = file_handler.load_dictionary('dictionary.json')
        dictionary.load_data(dictionary_data)
    except Exception as e:
        display_error(f"Error loading dictionary: {e}")

    while True:
        user_input = prompt_user("Enter a word to search (or press Enter to exit): ").strip()
        
        if not user_input:  # Exit if input is empty
            try:
                file_handler.save_dictionary('dictionary.json', dictionary.get_data())
                print("Dictionary saved. Exiting the application.")
                break
            except Exception as e:
                display_error(f"Error saving dictionary: {e}")
                break

        definition = dictionary.search_word(user_input)
        if definition:
            print(f"{user_input}: {definition}")
        else:
            print("Word not found. Please input a definition.")
            new_definition = prompt_user("Enter the definition: ").strip()
            if new_definition:
                dictionary.add_word(user_input, new_definition)
                print(f"Added '{user_input}' to the dictionary.")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")