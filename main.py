import sys
from stats import count_words,count_letters

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents



def main():
    args = sys.argv
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        print("============ BOOKBOT ============")
        print("Analyzing book found at books/frankenstein.txt...")
        print("----------- Word Count ----------")
        num = count_words(get_book_text(args[1]))
        letter_count = count_letters(num)
        for letter, count in sorted(letter_count.items(), key=lambda x: x[1], reverse=True):
            print(f"{letter}: {count}")


main()
