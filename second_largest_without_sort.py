num = input("Enter the numbers(space separated) - ")

#Variables
ary = num.split()
lar_array = []

for k in ary:
    lar_array.append(int(k))

largest = lar_array[0]
second_largest = lar_array[0]

for l in lar_array:
    if l > largest:
        second_largest = largest
        largest = l
        

print(f"Second Largest number in the array {lar_array} is {second_largest}")      