def get_num_words(string):
    list_words = string.split()
    return len(list_words)

def character_count(string):
    string = string.lower()
    dict = {}
    for char in string:
        if char in dict:
            dict[char] += 1
        else: 
            dict[char] = 1
    return dict

def sort_dict(dict):
    list = []
    for i in dict:
        char_dict = {"char" : "",
                     "num" : 0}
        char_dict["char"] = i
        char_dict["num"] = dict[i]
        list.append(char_dict)
    return sorted(list, reverse=True, key=lambda x: x["num"])