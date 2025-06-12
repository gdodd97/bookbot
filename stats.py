def count_words(book):
    book_split = book.split()
    num = 0
    for word in book_split:
        num += 1
    print(f"Found {num} total words")
    return book_split

def count_letters(book):
    letter_counts = {}
    
    for word in book:
        for char in word.lower():
            if char.isalpha():
                letter_counts[char] = letter_counts.get(char, 0) + 1
    
    return letter_counts