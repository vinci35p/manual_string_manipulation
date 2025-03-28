# Input any characters
user_char = str(input("Enter any characters: "))

# Input default parameter
parameter = 50

# Center the character based on the default parameter
total_spaces = max(0, parameter - len(user_char))
left = total_spaces // 2
right = total_spaces - left

# Print the result