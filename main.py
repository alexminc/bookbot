from stats import counts, characters, sorted_list
import sys
from pathlib import Path

# opens and reads the content of whole book
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
        

def main():
    if len(sys.argv) != 2: #user must enter two arguments 1. name of program (main.py) and 2. path to book (books/<name of book>)
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = Path.cwd() / sys.argv[1]

    book_text = get_book_text(book_path)
    # word_count = counts(book_text)

    # print("============ BOOKBOT ============")
    # print(f"Analyzing book found at books/frankenstein.txt...")
    # print("----------- Word Count ----------")
    # print(f"Found {word_count} total words")
    # print("--------- Character Count -------")
    sorted_list(characters(book_text))
    # print("============= END ===============")
    

main()