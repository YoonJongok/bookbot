from stats import get_num_words, get_charactor_frequency, sort_characters
import sys


def get_book_text(filepath: str) -> str:
    with open(filepath, "r") as file:
        return file.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")


    whole_text = get_book_text(f"{sys.argv[1]}")
    num_words = get_num_words(whole_text)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")


    char_dict = get_charactor_frequency(whole_text)

    char_list = sort_characters(char_dict)

    for item in char_list:
        char: str = item["char"]
        num: int = item["num"]
        print(f"{char}: {num}")

    
    print("============= END ===============")


if __name__ == "__main__":
    main()




