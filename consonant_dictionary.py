word_list = list(input("Enter the sentence - ").replace(" ",""))
#print(word_list)

dictionary = {}
for c in "bcdfghjklmnpqrstvwxyz":
    count = word_list.count(c)
    if count != 0:
        dictionary[c] = count

print(dictionary)