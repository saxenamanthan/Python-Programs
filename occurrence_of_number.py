numbers = input("Enter the numbers semi colon separated - ")
arr = numbers.split(";")
#print(arr)

int_array = [int(i) for i in arr]   
#print(int_array)

dictionary = {}
#Way 1
"""
for c in set(int_array):
    dictionary[c] = int_array.count(c)
"""

#Way 2  
for c in int_array:
    dictionary[c] = dictionary.get(c, 0) + 1
    
print(dictionary)    
    
    
   