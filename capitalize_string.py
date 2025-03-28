# Input any string characters
user_char = str(input("Enter any string characters: "))

# Capitalize the first letter, then lower case the rest
capitalized_char = user_char[0].upper() + user_char[1:].lower()

# Print the capitalized character
print(capitalized_char)