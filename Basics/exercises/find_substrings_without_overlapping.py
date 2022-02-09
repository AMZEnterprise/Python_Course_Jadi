text = input()

first = "AB"
second = "BA"

flag = False

while True:

    if text.find(first) != -1:
        text = text[text.find(first)+2:]
    elif text.find(second) != -1:
        text = text[text.find(second)+2:]
    else:
        break

    if len(text) == 0:
        flag = True
        break

if flag == True:
    print("YES")
else:
    print("NO")
