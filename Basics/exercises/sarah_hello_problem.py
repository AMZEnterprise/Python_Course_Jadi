text = input()


def hello_exists(text):

    hello = "hello"

    detected = ""

    for i in hello:
        if text.find(i) != -1:
            text = text[text.find(i)+1:]
            detected += str(i);

    return detected == hello


if hello_exists(text):
    print("YES")
else:
    print("NO")
