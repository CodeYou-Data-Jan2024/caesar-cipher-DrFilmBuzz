# Wesley Gift Caesar Cipher Homework Submission
# Implement a Caesar Cipher with a right shift of 5
# Ask user to enter a phrase

print("Enter phrase:")
phrase = input()

# Show entered phrase to user

print("You entered: " + phrase)

# Provide alphabet for code

alphabet = 'abcdefghijklmnopqrstuvwxyz'
new_phrase = ""

# Right shift 5 for input phrase

for i in range(0, len(phrase)):
    try: 
        char = phrase[i]
        new_char = str(alphabet[alphabet.index(char)+5])

        new_phrase += new_char

    except: 
        new_char = str(alphabet[0])
        new_phrase += new_char

# Prompt code to print new phrase

print("The Cipher Phrase is" + new_phrase)