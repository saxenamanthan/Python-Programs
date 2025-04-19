list_array = input("Enter the elements in the list comma separated - ")
array = list_array.split(",")
print(array)

#ary = []

int_array = [int(i) for i in array]

non_duplicate_arr = []

for i in int_array:
    if i not in non_duplicate_arr:
        non_duplicate_arr.append(i)

print(non_duplicate_arr)


#print(int_array)


