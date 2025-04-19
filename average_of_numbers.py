numbers = input("Enter the numbers comma separated - ")
arr = numbers.split(",")
#print(arr)

int_array = [int(i) for i in arr]
print(int_array)

average = sum(int_array)/len(int_array)
print(f"The average of numbers entered is {average}")