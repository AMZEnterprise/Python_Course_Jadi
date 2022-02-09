math_expression = input()

math_expression = math_expression.replace("+", "")

math_expression = ''.join(sorted(math_expression))

output = ""

for character in math_expression:
    output += character + "+"

output = output[:-1]

print(output)
