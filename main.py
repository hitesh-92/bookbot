def main():    
    path = "books/frankenstein.txt"
    book_content = get_book_content()
    
    word_count = get_word_count(book_content)
    #print(word_count)

    char_dict = char_count(book_content)
    #print(char_dict)

    print_report(path, char_dict, word_count)


def get_book_content():
    with open("books/frankenstein.txt") as f:
        book_content = f.read()
        return book_content

def get_word_count(text):
    split_arr = text.split()
    word_count = len(split_arr)
    return word_count

def char_count(text):
    char_dict = {}

    def filter_string(arr):
        filtered_list = []
        split = list(arr)
        for i in split:
            if i.isalpha():
                filtered_list.append(i.lower())
        return filtered_list
    
    def is_char_in_dict(char):
        return char in char_dict.keys()

    text_arr = text.split()
    for word in text_arr:
        #print(word)
        filtered_word_arr = filter_string(word)
        #print(filtered_word) #["t","o"]
        
        if len(filtered_word_arr)==0:
            continue

        for char in filtered_word_arr:
            if is_char_in_dict(char):
                char_dict[char] = char_dict[char] + 1
            else:
                char_dict[char] = 1


    return char_dict

def print_report(path, char_dict, book_word_count):

    print(f"--- Begin report of {path} ---")
    print(f"{book_word_count} found in the document")

    for k,v in char_dict.items():
        print(f"The '{k}' character was found {v} times")
    
    print(f"--- End report ---")



main()
