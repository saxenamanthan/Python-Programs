list_array = input("Enter the numbers comma separated - ")
ary = list_array.split(",")

int_arr = [int(i) for i in ary]
#print(int_arr) 

largest = int_arr[0]

for l in int_arr:
    if l > largest:
        largest = l
print(f"The largest number in an array {int_arr} is {largest} and its index is {int_arr.index(largest)}")