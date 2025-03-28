# Input full name with spaces before the name
user_name = str(input("Enter full name with several spaces before the name: "))

# Remove spaces before the name
modified_name = " ".join(user_name.split())

# Print modified name
print(modified_name)