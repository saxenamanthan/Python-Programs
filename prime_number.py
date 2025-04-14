num = int(input("Enter the number - "))
isPrime = True

for z in range(2, num):
    if num%z == 0:
        isPrime = False
        break

#if isPrime == False:
if isPrime:
    print(f"It is a prime number")
else:
    print(f"It is not a prime number")
