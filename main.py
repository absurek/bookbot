import sys
from stats import word_count, char_count, sort_char_count

def get_book_text(book_path):
    with open(book_path) as book:
        return book.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book = get_book_text(sys.argv[1])
    num_words = word_count(book)
    num_chars = char_count(book)
    sorted_num_chars = sort_char_count(num_chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for num_char in sorted_num_chars:
        if num_char["char"].isalpha():
            print(f"{num_char['char']}: {num_char['num']}")


main()

