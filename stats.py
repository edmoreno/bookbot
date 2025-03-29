def count_words(text):
    words_list = text.split()
    words_count = len(words_list)
    return words_count


def count_characters(text):
    character_counts = {}
    text_lowercase = text.lower()
    for char in text_lowercase:
        if char not in character_counts:
            character_counts[char] = 1
        else:
            character_counts[char] += 1
    return character_counts


def generate_dictionaries(count_dict: dict[str, int]) -> list[dict[str, int]]:
    dict_list = []
    for key, value in count_dict.items():
        char_dict = {}
        char_dict["char"] = key
        char_dict["count"] = value
        dict_list.append(char_dict)

    def sort_on(dict):
        return dict["count"]

    dict_list.sort(reverse=True, key=sort_on)
    return dict_list
