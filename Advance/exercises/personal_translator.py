words_count = int(input())

english_persian_dict = {}
france_persian_dict = {}
german_persian_dict = {}

for i in range(words_count):
    words = input().split()

    english_persian_dict[words[1]] = words[0]
    france_persian_dict[words[2]] = words[0]
    german_persian_dict[words[3]] = words[0]


sentence = input()
translated = ""

for word in sentence.split(" "):
    if word in english_persian_dict:
        translated += english_persian_dict[word] + " "
    elif word in france_persian_dict:
        translated += france_persian_dict[word] + " "
    elif word in german_persian_dict:
        translated += german_persian_dict[word] + " "
    else:
        translated += word + " "

print(translated)
