def get_word_count (content):
    words = content.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

# def dict_to_list(dict):
#     l = []
#     for key in dict:
        
#     return
def char_dict_to_sorted_list(dict):
    ls = []
    for char in dict:
        d = {'char': char,
             'num': dict[char]}
        ls.append(d)
    ls.sort(reverse=True, key=sort_on)
    return ls

def sort_on(dict):
    return dict['num']

def get_char_count(content):
    content = content.lower()
    chars = {}

    for word in content.split():
        for c in word:
            if not c.isalpha():
                continue
            if c in chars:
                chars[c] += 1
            else:
                chars[c] = 1
    return chars




def main():
    path_to_file = 'books/frankenstein.txt'
    content = get_book_text(path_to_file)
    word_count = get_word_count(content)
    char_count = get_char_count(content)
    char_count = char_dict_to_sorted_list(char_count)
    
    print(f'--- Begin report of {path_to_file} ---')
    print(f'{word_count} words fount in the document')
    
    for char in char_count:
        print(f'The character "{char['char']}" was found {char['num']} times')
    
    print('--- End report ---')
    
    
    
main()
