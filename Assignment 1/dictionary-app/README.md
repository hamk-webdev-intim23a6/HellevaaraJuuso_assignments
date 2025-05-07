# Dictionary Application

This is a simple dictionary application that allows users to search for words, add definitions, and manage their own dictionary. The dictionary is stored in JSON format, making it easy to save and load.

## Features

- Search for words and retrieve their definitions.
- Add new words and definitions to the dictionary.
- Load the dictionary from a JSON file on startup.
- Save the dictionary to a JSON file upon exit.
- User-friendly error handling and prompts.

## Project Structure

```
dictionary-app
├── src
│   ├── main.py          # Entry point of the application
│   ├── dictionary.py    # Contains the Dictionary class
│   ├── file_handler.py   # Manages loading and saving of the dictionary
│   └── utils.py         # Utility functions for error handling and user prompts
├── requirements.txt     # Lists the dependencies required for the project
└── README.md            # Documentation for the project
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd dictionary-app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the following command in your terminal:

```
python src/main.py
```

Follow the on-screen prompts to interact with the dictionary application.

## Error Handling

The application includes error handling to manage issues such as file loading errors and invalid user input. Users will receive clear messages to guide them in resolving any issues.

## Contributing

Feel free to submit issues or pull requests if you have suggestions for improvements or new features!