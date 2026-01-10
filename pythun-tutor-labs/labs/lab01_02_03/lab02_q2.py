text = input("Enter a string: ")
vowels = "aeiouAEIOU"
new_text = ""

for ch in text:
    if ch in vowels:
        new_text += chr(ord(ch) + 1)  
    else:
        new_text += ch
print("new string:", new_text)

letters = "abcdefghijklmnopqrstuvwxyz"

for letter in vowels:
    print(letter, ord(letter), end='\n')
