arr_1 = [i for i in range(1,11)]
arr_2 = [j for j in range(5,16)]
arr_2.extend(arr_1)
print(arr_2)

remove_duplicates = set(arr_1)
sorted_set = sorted(remove_duplicates)
sorted_set.sort(reverse = True)
print(sorted_set)

"""
#Another way to merge 2 arrays 
arr_3 = [] 

for i in arr_1:
    arr_3.append(i)

for i in arr_2:
    arr_3.append(i)
    
print(set(arr_3))
"""