user_input = input("Enter the numbers in sequence comma separated - ")
int_array = [int(i) for i in user_input.split(",")]

#Way 1
"""
for i in range(1,len(int_array)+2):
    if i not in int_array:
        print(i)
        break
"""
     
#Way 2
sum_array = sum(int_array)
n = len(int_array)+1
sum_ints = (n * (n+1))//2        

print(sum_ints - sum_array)