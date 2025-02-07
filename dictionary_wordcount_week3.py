import sys
from collections import Counter

# Helper function to get word counts
def get_word_count(filename):
    word_count = Counter()
    with open(filename, 'r') as f:
        # Read file line by line, split into words and convert to lowercase
        for line in f:
            words = line.lower().split()
            word_count.update(words)
    return word_count

# Function to print all words and their counts, sorted by word
def print_words(filename):
    word_count = get_word_count(filename)
    for word in sorted(word_count):
        print(f'{word} {word_count[word]}')

# Function to print the top 20 most common words
def print_top(filename):
    word_count = get_word_count(filename)
    # Get the 20 most common words, sorted by frequency (highest first)
    for word, count in word_count.most_common(20):
        print(f'{word} {count}')

def main():
    if len(sys.argv) != 3:
        print('usage: ./wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print('unknown option: ' + option)
        sys.exit(1)

if __name__ == '__main__':
    main()
