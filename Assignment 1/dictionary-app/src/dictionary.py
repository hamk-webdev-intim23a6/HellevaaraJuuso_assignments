class Dictionary:
    def __init__(self):
        # Default dictionary with a few predefined words and definitions
        self.words = {
            "hello": "A greeting",
            "world": "The earth, together with all of its countries and peoples",
            "python": "A high-level programming language",
            "dictionary": "A collection of words and their meanings",
            "code": "A system of words, letters, or symbols used to represent something"
        }

    def search_word(self, word):
        # Convert the word to lowercase for case-insensitive search
        word_lower = word.lower()
        for key, value in self.words.items():
            if key.lower() == word_lower:
                return value
        return None

    def add_word(self, word, definition):
        self.words[word] = definition

    def load_data(self, data):
        self.words.update(data)

    def get_data(self):
        return self.words