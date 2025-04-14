print("Atm cash withdrawl")

balance = 20000
withdrawl = input("Enter the amount to withdraw - ")
withdrawl = float(withdrawl)
if withdrawl <= 0:
    print("Withdrawl amount should not be less than or equal to 0")
elif withdrawl <= balance:
    print(f"You have withdrawn Rs.{withdrawl} and your remaining balance is Rs.{balance - withdrawl}")
else:
    print(f"Insufficient balance!!")