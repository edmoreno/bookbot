import sys

from stats import count_words, count_characters, generate_dictionaries


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]

    book_text = get_book_text(book_path)
    words_count = count_words(book_text)
    characters_count = count_characters(book_text)
    count_list = generate_dictionaries(characters_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {words_count} total words")
    print("--------- Character Count -------")

    for character in count_list:
        if character["char"].isalpha():
            print(f"{character["char"]}: {character["count"]}")

    print("============= END ===============")


main()
