num = input("Enter the numbers(space separated) - ")

#Variables
ary = num.split()
small_array = []

for s in ary:
    small_array.append(int(s))

smallest = small_array[0]
#second_largest = lar_array[0]

for s in small_array:
    if s < smallest:
        #second_largest = largest
        smallest = s
        

print(f"Smallest number in the array {small_array} is {smallest}")