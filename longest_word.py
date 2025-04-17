sentence = input("Enter the sentence - ")
arr = sentence.split()
longest_length = 0
longest_word = ""
for l in arr:
    len_word = len(l)
    if len_word > longest_length:
        longest_length = len_word
        longest_word = l

print(f"The longest word is {longest_word} with length {longest_length}")

    
#print(arr)
#print(len(arr))

