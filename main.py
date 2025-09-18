from stats import get_num_words
from stats import get_num_chars
from stats import sort_inventory
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        text = sys.argv[1]
        num_words = get_num_words(text)
        num_chars = get_num_chars(text)
        counts_list = sort_inventory(num_chars)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {text}")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for dic in counts_list:
            if not dic["char"].isalpha():
                next
            else:
                print(f"{dic["char"]}: {dic["num"]}")
        print("============= END ===============")

if __name__ == "__main__":
    main()
