# Input any characters
user_char = str(input("Enter any characters: "))

# Check sentence if upper-cased or not and print decision
if user_char == user_char.swapcase().upper():
    print("The inputted characters is in upper case.")

else:
    print("The inputted characters is not in upper case.")
