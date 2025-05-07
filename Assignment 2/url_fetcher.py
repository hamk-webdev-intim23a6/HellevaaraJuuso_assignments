import requests
import re

def main():
    dangerous_words = {"bomb", "kill", "murder", "terror", "terrorist", "terrorists", "terrorism"}
    
    # Step 1: Ask for a valid URL
    url = input("Give me a valid URL to download? ").strip()
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error opening url")
        input("Press Enter to exit...")
        return

    # Step 2: Check if the content is HTML with utf-8 encoding
    content_type = response.headers.get('Content-Type', '')
    if 'text/html' in content_type and response.encoding and response.encoding.lower() == 'utf-8':
        # Extract text content by removing HTML tags
        html_content = response.text
        text_content = re.sub(r'<[^>]+>', '', html_content)  # Remove HTML tags
        
        # Count dangerous words
        word_count = 0
        for word in re.findall(r'\b\w+\b', text_content):  # Extract words
            if word.lower() in dangerous_words:
                word_count += 1
        
        print(f"Number of dangerous words: {word_count}")
    else:
        print("The content is not an HTML file with utf-8 encoding or is binary data.")

    # Step 3: Ask for a path to save the contents
    save_path = input("Give me a valid path to save the contents? ").strip()
    try:
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"Saving succeeded")
    except OSError as e:
        print(f"Saving failed.")

    # Wait for user to press Enter before exiting
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()