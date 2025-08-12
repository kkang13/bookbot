from stats import get_num_words, character_count, sort_dict
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}")
        book = get_book_text(sys.argv[1])
        
        #print number of words in book
        print("----------- Word Count ----------")
        num_words = get_num_words(book)
        print(f"Found {num_words} total words")
        
        #retrieve dictionary of characters and number occurred
        print("--------- Character Count -------")
        dict_characters = character_count(book)

        #sort the dictionary of characters into a list
        list_char = sort_dict(dict_characters)
        for item in list_char:
            if item["char"].isalpha():
                print(f'{item["char"]}: {item["num"]}')
        print("============= END ===============")

main()