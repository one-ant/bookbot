def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def get_num_words(path_to_file):
    book_text = get_book_text(path_to_file)
    return len(book_text.split())

def get_num_chars(path_to_file):
    book_text = get_book_text(path_to_file)
    character_count = {}
    for char in book_text:
        ch = char.lower()
        try:
            character_count[ch] += 1
        except KeyError:
            character_count[ch] = 1
    return character_count

def sort_inventory(character_count):
    counts_list = []
    for key, value in character_count.items():
        counts_list.append({"char": key, "num": value})
    counts_list.sort(reverse=True, key=sort_on)
    return counts_list

def sort_on(items):
    return items["num"]
