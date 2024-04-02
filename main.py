from collections import Counter
import json


def preprocess_text(text):
    cleaned_text = ''
    previous_char = ''
    for char in text:
        if char.isalpha() or char.isspace():
            if char.isspace() and previous_char.isspace():
                continue  # Skip consecutive spaces
            cleaned_text += char.lower()  # Convert to lowercase
        previous_char = char
    return cleaned_text.strip()  # Strip leading and trailing spaces


def most_common_words(file_path, num_words=1):
    with open(file_path, 'r') as file:
        text = file.read()
        text = preprocess_text(text)  # Preprocess the text
        words = text.split()  # Split the text into words
        word_counts = Counter(words)  # Count the occurrences of each word
        most_common = word_counts.most_common(num_words)  # Find the most common word(s)
        return most_common  # Return the most common word(s) and their counts


file_path = "pogo_planet.txt"
num_words = 100  # Change this number to get the desired number of most common words
most_common = most_common_words(file_path, num_words)
print("The {} most common word(s) are:".format(num_words))
for word, count in most_common:
    print("Word: '{}', Count: {}".format(word, count))

output_file = "words.json"
with open(output_file, 'w') as json_file:
    json.dump(most_common, json_file)

