words_count = int(input())

words_dict = {}

def add_word(word,definition):
    words_dict[word] = definition

def translate_sentence(words_list):
    sentence = ""

    for word in words_list:
        if word in words_dict:
            sentence += words_dict[word] + " "
        else:
            sentence += word + " "

    return sentence

for i in range(words_count + 1):
    text = input()

    words = text.split(" ")

    if len(words) == 2:
        add_word(words[0] ,words[1])

    else:
        print(translate_sentence(words))

