


def on_pages(words_on_page, word):
    """returns a list of the pages where the word occurs"""
    pages = []
    for page_num, word_list in words_on_page.items():
        if word in word_list:
            pages.append(page_num)
    return pages



def make_index(words_on_page):
    """fkl fklenwmfl kenrlfknerklfn elnfv ler"""
    
    all_words = []
    for words in words_on_page.values():
        for word in words:
            all_words.append(word)
    word_set = set(all_words)
    word_list = list(word_set)

    new_list = []

    for word in word_list:
        new_list.append((word, on_pages(words_on_page, word)))

    new_list.sort(key=lambda x : x[1])

    return dict(new_list)







input_dict = {
   1: ['hi', 'there', 'fred'], 
   2: ['there', 'we', 'go'],
   3: ['fred', 'was', 'there']}
output_dict = make_index(input_dict)
print(input_dict)
print(output_dict)