word = input()

word = word.lower()

if(word.__eq__(word[::-1])):
      print("palindrome")
else:
      print("not palindrome")