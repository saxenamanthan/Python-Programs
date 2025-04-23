def square_number(num):
    return(num**2)
    
    
user_input = int(input("Enter the number to find its square - "))
 
s = square_number(user_input)
print(f"The square of the entered number is {s}")