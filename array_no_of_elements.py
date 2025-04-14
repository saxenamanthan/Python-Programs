elements = input("Enter number of elements in array - ")
elements = int(elements)

#create empty array
ary = []

for i in range(elements):
    #Input value from user
    value = input("Enter the value - ")
    
    #append values in array
    ary.append(value)


#printing array
for val in ary:
    print(f"The value in this array is {val}")

print(f"Array is - {ary}")
print(f"The size of array is - {len(ary)}")


