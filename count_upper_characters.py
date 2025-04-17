sentence = input("Enter the sentence - ")
upper_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
arr = [s for s in sentence if s in upper_characters]
print(f"The number of upper case characters in a sentence is {len(arr)}")