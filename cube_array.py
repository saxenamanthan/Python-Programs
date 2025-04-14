user_input = int(input("Enter the number till which you want cubes - "))

cube_array = []

for cube in range(1,user_input+1):
    #print(cube*cube*cube)
    cube_array.append(cube*cube*cube) 
    
print(cube_array)    

sum = 0

for addition in cube_array:
    sum = sum + addition
    
print(sum)    