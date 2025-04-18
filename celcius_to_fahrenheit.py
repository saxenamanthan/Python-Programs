celcius = input("Enter the temperatures in celcius - ")
arr_t = celcius.split(" ")
#print(arr_t)
"""
float_array = []
for c in arr_t:
    float_array.append(float(c))
    
print(float_array)
"""

float_array = [float(c) for c in arr_t]
print(f"The temperature in celcius is {float_array}")

"""
fahrenheit_array = []
for temp in float_array:
    #f = (temp*9/5) + 32
    fahrenheit_array.append((temp*9/5) + 32)
"""

fahrenheit_array = [(temp*9/5) + 32 for temp in float_array] 
print(f"The temperature in fahrenheit after conversion is {fahrenheit_array}")    

"""
f = (arr_t*9/5) + 32
[temp for temp in arr_t]
print(temp)
"""


