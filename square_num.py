num = int(input("Enter the num - "))

ar = []
for k in range(1,num+1):
    #print(k*k)
    ar.append(k*k)
    
print(f"The square array is {ar}")    

sum = 0
for s in ar:
    #print(s)
    sum = sum + s 
    
print(f"The sum of this array is {sum}")    