from pyscript import document
from secrets import choice

def get_words ():
    with open('./usr_share_dict_italian.txt') as infile:
        return list(line.strip() for line in infile)

def choose_words (arr, num):
    return list(choice(arr) for _ in range(num))

def random_words (event):
    n = int(document.querySelector("#words_number").value)
    output_div = document.querySelector("#output")
    output_div.innerText = ' '.join(choose_words(get_words(), n))
