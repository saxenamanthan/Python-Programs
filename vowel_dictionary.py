sentence = input("Enter the sentence - ")
s = list(sentence.replace(" ",""))
#print(s)
dictionary = {}

for v in "aeiou":
    dictionary[v] = s.count(v)
    #print(f"The count of {v} in a sentence is {s.count(v)}")
print(dictionary)    
