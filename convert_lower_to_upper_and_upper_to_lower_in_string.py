string = input("Enter the string - ")

#arr = list(string.replace(" ",""))
arr = list(string)
#print(arr)

str_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
str_lower = "abcdefghijklmnopqrstuvwxyz"

array = []

for i in arr:
    if i in str_upper:
        array.append(i.lower())
    if i in str_lower:
        array.append(i.upper())
    if i == " ":
        array.append(i)
        
print("".join(array))
        
        