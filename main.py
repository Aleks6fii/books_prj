from collections import Counter
import json


def preprocess_text(text):
    cleaned_text = ''
    previous_char = ''
    for char in text:
        if char.isalpha() or char.isspace():
            if char.isspace() and previous_char.isspace():
                continue                    # Skip consecutive spaces
            cleaned_text += char.lower()    # Convert to lowercase
        previous_char = char
    return cleaned_text.strip()             # Strip leading and trailing spaces


def word_ignore(word, filename):
    with open(filename, 'r') as file:
        for line in file:
            if word in line.split():
                return True
    return False


def most_common_words(book_file, ignr, num_words=1):
    with open(book_file, 'r') as file:
        text = file.read()
        text = preprocess_text(text)    # Preprocess the text
        words = text.split()            # Split the text into words
        tocount = []

        for word in words:
            if word_ignore(word, ignr):
                continue
            else:
                # print(f"The word '{word}' does not exist in ignore")
                tocount.append(word)

        word_counts = Counter(tocount)  # Count the occurrences of each word
        most_common = word_counts.most_common(num_words)  # Find the most common word(s)

    return most_common  # return words and counts 


book = "pogo_planet.txt"
ignore = "most_common_en.txt"

num_words = 10   # the desired number of most common words in the book
most_common = most_common_words(book, ignore, num_words)

print("The {} most common word(s) are:".format(num_words))
for word, count in most_common:
    print("Word: '{}', Count: {}".format(word, count))

output_file = "words.json"
with open(output_file, 'w') as json_file:
    json.dump(most_common, json_file)

