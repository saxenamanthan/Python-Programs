list_arr = input("Enter the numbers comma separated - ")
string = input("Enter the string - ")
arr1 = list_arr.split(",")

#print(arr1)
#print(arr2)

arr3 = arr1 + list(string)
print(arr3)

str = "".join(arr3)
print(str.replace(" ",""))