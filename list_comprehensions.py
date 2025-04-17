ar = [i for i in range(1,11)]
print(ar)

even_ar = [i for i in range(1,11) if i%2 == 0]
print(even_ar)

odd_ar = [i for i in range(1,11) if i%2 != 0]
print(odd_ar)

square_ar = [i**2 for i in range(0,11)]
print(square_ar)

cube_ar = [i**3 for i in range(0,11)]
print(cube_ar)

str = "hello world"
arr = str.split()
upper_ar = [i.upper() for i in arr]
print(upper_ar)
upper_helloworld = "-".join(upper_ar)
print(upper_helloworld)
