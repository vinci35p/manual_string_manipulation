# Input any characters
user_char = str(input("Enter any character: "))

# Input how many number of characters
parameter = int(input("Enter the length of characters desired: "))

# Add spaces to the inputted character to match the parameter given
result = "{:<{}}".format(user_char, parameter)

# Print the result
print(result)