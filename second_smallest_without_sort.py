num = input("Enter the numbers(space separated) - ")

#Variables
ary = num.split()
small_array = []

for s in ary:
    small_array.append(int(s))

smallest = small_array[0]

for s in small_array:
    if s < smallest:
        smallest = s

small_array.remove(smallest)
second_smallest = small_array[0] #Need to select some value

# Need to modify logic to find second smallest
for s in small_array:
    if s < second_smallest:
        second_smallest = s      

print(f"Second Smallest number in the array {small_array} is {second_smallest}")