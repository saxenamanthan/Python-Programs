number = input("Enter the number - ")

array = number.split(",")
#print(array)
int_array = []

for i in array:
    print(int(i))
    int_array.append(int(i))
    
print(int_array)
   
int_array.sort(reverse = True)
print(int_array)
print(f"Largest number is {int_array[0]}")
print(f"Second largest number is {int_array[1]}")
print(f"Third largest number is {int_array[2]}")
print(f"Fourth largest number is {int_array[3]}")
