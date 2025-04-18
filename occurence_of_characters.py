sentence = input("Enter the sentence - ")

#array = list(sentence)
#print(array)
"""
arr = []
for ch in sentence.replace(" ",""):
    #print(ch)
    arr.append(ch)
"""    
char_array = [ch for ch in sentence.replace(" ","")]
print(char_array)    
    

dictionary = {}

for ch in char_array:
    dictionary[ch] = char_array.count(ch)
    
print(dictionary)
