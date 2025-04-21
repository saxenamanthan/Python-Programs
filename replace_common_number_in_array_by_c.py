list_array1 = [1,2,3,4,5]
list_array2 = [3,5,7,9,10]

print(list_array1)

common_elements = [i for i in list_array1 if i in list_array2]
print(common_elements)

for i in common_elements:
    index = list_array1.index(i)
    list_array1[index] = "c"
    
    index1 = list_array2.index(i)
    list_array2[index1] = "c"  
    
print(list_array1)
print(list_array2)
    
    