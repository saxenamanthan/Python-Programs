user_input = int(input("Enter the number till which you want - "))


power = int(input("Enter the power you want - "))
power_array = []

for p in range(1,user_input+1):
    #print(p)
    power_array.append(p**power)
    
print(power_array)    

