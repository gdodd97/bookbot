from stats import count_words,count_letters

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents



def main():
   print("============ BOOKBOT ============")
   print("Analyzing book found at books/frankenstein.txt...")
   print("----------- Word Count ----------")
   num = count_words(get_book_text("./books/frankenstein.txt"))
   letter_count = count_letters(num)
   for letter, count in sorted(letter_count.items(), key=lambda x: x[1], reverse=True):
        print(f"{letter}: {count}")


main()
