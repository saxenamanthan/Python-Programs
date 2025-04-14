numbers = input("Enter the numbers - ")
number_to_search = int(input("Enter the number  to search - "))

arr = numbers.split(",")

found = False
#print(arr)


for f in arr:
    #print(int(f))
    
    #array.append [f]
    if int(f) == number_to_search:
        found = True
        #print(f"Number is found {f}")
        break

if found:
    print("Number is found")
else:
    print("Number is not found")    
       