num = input("Enter the number - ")
num_list = list(num)
sum = 0

for n in num_list:
    sum = sum + int(n)**3
    
print(sum)

if sum == int(num):
    print(f"{num} ,is a armstrong number")
else:
    print(f"{num} ,is not an armstrong number" )