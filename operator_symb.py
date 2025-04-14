print("**************Calculator******************")
a = input("Enter 1st number - ")
a = int(a)
b = input("Enter 2nd number - ")
b = int(b)
c = input("Enter the operator - ")
if c == "+":
    print("You have selected sum symbol")
    print(f"The sum of {a} and {b} is {a + b}")
if c == "-":
    print("You have selected substract symbol")
    if a > b:
        print(f"Number {a} is bigger than {b} therefore the diff of {a} and {b} is {a - b}")
    else:
        print(f"Number {b} is bigger than {a} therefore the diff of {b} and {a} is {b - a}")
if c == "*":
    print("You have selected multiply symbol")
    print(f"The multiplication of {a} and {b} is {a * b}")     
if c == "/":
    print("You have selected divide symbol")
    if a > b:
        print(f"Number {a} is bigger than {b} therefore the division of {a} and {b} is {a / b}")
    else:
        print(f"Number {b} is bigger than {a} therefore the division of {b} and {a} is {b / a}")
if c == "%":
    print("You have selected modulus symbol")
    print(f"The modulus of {a} and {b} is {a % b}")
if c == "**":
    print("You have selected exponent symbol")
    print(f"The power of {a} to {b} is {a ** b}")
if c == "==":
    print("You have selected equals symbol")
    print(f"{a} is equal to {b} {a == b}")
