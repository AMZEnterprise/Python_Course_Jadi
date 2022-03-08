text = input()

sentences = list(filter(None, text.split(".")))

visited_words = []

for sentence in sentences:
    words = list(filter(None, sentence.split(" ")))
    words = [s.replace(',', '') for s in words]
    sentences[sentences.index(sentence)] = words

words = []

for sentence in sentences:
    sentences[sentences.index(sentence)][0] = "***"


for sentence in sentences:
    for word in sentence:
        words.append(word)

for word in words:

    if word[0].isupper():
        how_many_times_word_appeared = sum(x.count(word) for x in visited_words)         

        if how_many_times_word_appeared == 0:
            visited_words.append([word, words.index(word) + 1])
        else:
            idx = [i for i, n in enumerate(words) if n == word][how_many_times_word_appeared]
            visited_words.append([word, idx + 1])
                
if len(visited_words) == 0:
    print("None")
else:
    for word in visited_words:
        print(str(word[1]) + ":" + word[0])
