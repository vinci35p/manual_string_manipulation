# Input sentence
sentence = str(input("Enter a sentence: "))

# Input word to check if it matches the end of first input
end_word = str(input("Input the ending word to check: "))

# Decide if inputted value matches and print decision
if sentence[-len(end_word):] == end_word:
    print("The sentence ends with the end word inputted!")

else:
    print("The sentence does not end with the end word inputted.")