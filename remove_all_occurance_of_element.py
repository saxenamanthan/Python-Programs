list_arr = [1,2,1,3,1,5,6,2]
no_to_remove = int(input("Enter the number to remove - "))

#Way 1
arr = [i for i in list_arr if i != no_to_remove]
print(arr)

#Way 2
print(list(map(int,list("".join(list(map(str, list_arr))).replace(str(no_to_remove), "")))))