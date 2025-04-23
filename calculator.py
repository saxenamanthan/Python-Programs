def print_calculator(num1, num2, operator):
    if operator == "+":
        print(f"You have selected sum operator\nThe sum of {num1} and {num2} is {num1+num2}")
    elif operator == "-":
        print(f"You have selected subtract operator\nThe substraction of {num1} and {num2} is {num1-num2}")
    elif operator == "*":
        print(f"You have selected multiply operator\nThe multiplication of {num1} and {num2} is {num1*num2}")
    elif operator == "/":
        print("You have selected division operator")
        if num2 == 0:
            print(f"{num1} cannot be divided by zero")
        else:
            print(f"The division of {num1} and {num2} is {num1/num2}")

user_input = input("Enter the first number second number and the operator space separated - ")
arr = user_input.split()

print_calculator(int(arr[0]), int(arr[1]), arr[2])
        