numbers = input("Enter the numbers comma separated - ")
a = int(input("Enter the number to print greater numbers from this - "))
arr = numbers.split(",")
#print(arr)

int_array = [int(i) for i in arr]
#print(int_array)

s = [i for i in int_array if i > a]
print(f"The numbers which are greater than {a} is {s} and the count of those numbers is {len(s)}")


