def word_count(text):
    words = text.split()
    return len(words)


def char_count(text):
    char_dict = {}

    for char in text:
        lower = char.lower()
        if lower not in char_dict:
            char_dict[lower] = 0

        char_dict[lower] += 1

    return char_dict

def get_num(num_char):
    return num_char["num"]


def sort_char_count(num_chars):
    char_count_list = []

    for char in num_chars:
        char_count_list.append({ "char": char, "num": num_chars[char] })

    char_count_list.sort(reverse=True, key=get_num)
    return char_count_list

