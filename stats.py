def get_word_count(booktext):
     words = booktext.split()
     return len(words)

def char_stats(booktext):
    text = booktext.lower()

    char_count = {}

    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count

def sort_greatest_least(stats):
    return stats["num"]

def sort_char_list(stats):
    char_list = [{"char": char, "num": count} for char, count in stats.items() if char.isalpha()]

    char_list.sort(reverse=True, key=sort_greatest_least)

    return char_list