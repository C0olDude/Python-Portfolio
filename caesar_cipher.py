code = input("Enter something to encode: ")
shift = int(input("Enter shift: "))
letters = "abcdefghijklmnopqrstuvwxyz"
result  = ""
# letter is z
# shift is 5
# index_of_letter is 25
# new_index 30 % 26 -> 4
for char in code:
    if char.lower() in letters:
        index_of_letter = letters.index(char.lower())
        # to loop back to the beginning if index_of_letter + shift exceeds 26
        index_of_new_letter = (index_of_letter + shift) % 26
        new_letter = letters[index_of_new_letter]
        if char.isupper():
            result += new_letter.upper()
        else:
            result += new_letter
    else:
        result += char
print(result)