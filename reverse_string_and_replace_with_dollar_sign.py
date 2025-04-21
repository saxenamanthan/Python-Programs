string = input("Enter the string - ")
#Way 1
"""
arr = list(string.replace(" ","$"))
#print(arr)

arr.reverse()
#print(arr)

str = "".join(arr)
print(str)
"""

#Way 2
"""
new_string = ""
for i in string:
    new_string = i + new_string
    
print(new_string.replace(" ","$"))
"""

#Way 3
print(string[::-1].replace(" ","$"))