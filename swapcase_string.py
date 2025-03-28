# Input any characters
user_char = str(input("Enter any string characters: "))

# Swap the case of the characters
swapped_characters = "".join(
    chr(ord(char) + 32) if 'A' <= char <= 'Z' else
    chr(ord(char) - 32) if 'a' <= char <= 'z' else
    char
    for char in user_char
)

# Print the swapped characters
print(swapped_characters)
