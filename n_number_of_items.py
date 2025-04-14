num = int(input("Enter number of elements you want to enter - "))

array = []

for elements in range(1,num+1):
    element = input("Enter your element - ")
    array.append(element)

print(array)