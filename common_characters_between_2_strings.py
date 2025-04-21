string1 = input("Enter string1 - ")
string2 = input("Enter string2 - ") 

arr1 = list(string1.replace(" ",""))
arr2 = list(string2.replace(" ",""))

#print(arr1)
#print(arr2)

z = {i for i in arr1 if i in arr2}
print(f"The common characters of two strings are {z} and their count is {len(z)}")