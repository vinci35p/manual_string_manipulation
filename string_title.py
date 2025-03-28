# Input full name
user_name = str(input("Enter your full name in random case: "))

# Convert first letter of every word to upper case and the rest lower cased
words = user_name.split()
title_case = " ".join(word[0].upper() + word[1:].lower() if word else "" for word in words)

# Print the result
print(title_case)