n = input("Enter your number - ")
n = int(n)

n = n+1

arr_even = []
arr_odd = []

for num in range(1,n):
    if num%2 == 0:
        arr_even.append(num)
    else:
        arr_odd.append(num)
    
print(f"Even number array is - {arr_even}")
print(f"Odd number array is - {arr_odd}")