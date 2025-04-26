from stats import get_word_count
from stats import char_stats
from stats import sort_char_list
import sys



def get_book_text(filepath):
    try:
            with open (filepath) as f:
                return f.read()
    except FileNotFoundError:
            return f"Error: The file at {filepath} was not found."        
    except IOError as e:
        return f"Error reading the file: {e}"


def main():
    
    if len(sys.argv) != 2:
         print("Usage: python3 main.py <path_to_book>")
         sys.exit(1)

         
    filepath = sys.argv[1]

    book_text = get_book_text(filepath)
    word_count = get_word_count(book_text)

    char_count = char_stats(book_text)
    sorted_char_count = sort_char_list(char_count)

    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for entry in sorted_char_count:
         print(f"{entry['char']}: {entry['num']}")
    print("============= END ===============")
    
    



main()
