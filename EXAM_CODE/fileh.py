def count_words_and_characters(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

            # Count words
            word_count = len(content.split())

            # Count characters
            char_count = len(content)

            print(f"Number of words: {word_count}")
            print(f"Number of characters: {char_count}")

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
file_path = 'my.txt'  # Replace 'your_file.txt' with the actual file path
count_words_and_characters(file_path)
