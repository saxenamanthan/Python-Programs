print("Largest of three numbers")
num1 = int(input("Enter your 1st number - "))
num2 = int(input("Enter your 2nd number - "))
num3 = int(input("Enter your 3rd number - "))
if num1 == num2 and num1 == num3:
    print("No number is greater")
elif num1 > num2 and num1 > num3:
    print(f"Largest number is {num1}")
elif num2 > num1 and num2 > num3:
    print(f"Largest number is {num2}")
else:
    print(f"Largest number is {num3}")

