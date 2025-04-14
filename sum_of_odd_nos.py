num = int(input("Enter the number - "))

sum_array = []
for o in range(1, num+1):
    if o%2 != 0:
        #print(o)
        sum_array.append(o)
        
sum = 0
for s in sum_array:
    sum = sum + s
    
print(f"Sum of all odd numbers between 1 and {num} is {sum}")    
    

        
        
        
        
