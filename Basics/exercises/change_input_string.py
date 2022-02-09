username = input()
disallowed_characters = "aeuoiAEUOI"

for character in disallowed_characters:
    username = username.replace(character, "")

new_username = ""

for character in username:
    new_username += "." + character

print(new_username.lower())
