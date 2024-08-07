def count_words(book):
    return book.split()

def count_character(words):
    character = {}   

    for word in words:
        word = word.lower()

        for c in word:
            if c not in character:
                character[c] = 1
            else:
                character[c] += 1

    return character

def create_list(dictionary):
    list_of_dicts = []
    
    
    for k,v in dictionary.items():
        if k.isalpha() == True:
            temp_dict = {}
            temp_dict["Letter"] = k
            temp_dict["Amount"] = v
            list_of_dicts.append(temp_dict)       
        
    return list_of_dicts

def sort_on(dict):
    return dict["Amount"]

def sort_dict_list(list_of_dicts):
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts

def report(book, words, characters):
    dict_list = create_list(characters)
    sorted = sort_dict_list(dict_list)    
    print(f"--- Begin report of {book} ---")
    print(f"{len(words)} words found in the document")    
    for dictionary in sorted:        
            print(f"The '{dictionary['Letter']}' character was found {dictionary['Amount']} times")
    print("--- End report ---")
    

def main():
    path = "books/frankenstein.txt"
    with open(path) as f:
        book = f.read()

    words = count_words(book)    
    characters = count_character(words)    
    report(path, words, characters)
main()