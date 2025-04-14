num = int(input("Enter how many numbers you want in your array - "))

array = []
for numbers in range(1,num+1):
    number = input("Enter your number - ")
    array.append(int(number))
    
array.sort()

smallest_number = array[0]
print(smallest_number)
print(smallest_number**3)

is_prime = True

for p in range(2, smallest_number):
    if smallest_number%p == 0:
        is_prime = False
        break

if is_prime:
    print("It is a prime number")
else:
    print("It is not a prime number")
    
