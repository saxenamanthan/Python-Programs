print("Check which number is Greater")
num1 = input("Enter your 1st number - ")
num1 = int(num1)
num2 = input("Enter your 2nd number - ")
num2 = int(num2)
if num1 == num2:
    print(f"As {num1} and {num2} are same therefore no one is greater")
if num1 > num2:
    print(f"From {num1} and {num2}, {num1} is greater")
if num1 < num2:
    print(f"From {num1} and {num2}, {num2} is greater")    
    