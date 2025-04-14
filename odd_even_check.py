print("Check number is odd or even")
num = input("Enter your number - ")
num = int(num)
if num == 0:
    print(f"It is nor odd nor even")
elif num%2 == 0:
    print(f"As {num} is divisible by 2 and gives remainder zero,it is an even number")
elif num%2 != 0:
    print(f"As {num} is not divisible by 2 and gives remainder,it is an odd number")