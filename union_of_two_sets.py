list_array1 = input("Enter the elements of first list comma separated - ")
list_array2 = input("Enter the elements of second list comma separated - ")

int_ar1 = [int(i) for i in list_array1.split(",")]
int_ar2 = [int(j) for j in list_array2.split(",")]
#print(int_ar1)
#print(int_ar2)

print(set(int_ar1 + int_ar2))
