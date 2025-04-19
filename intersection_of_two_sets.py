arr_1 = input("Enter the elements comma separated in first array - ")
arr_2 = input("Enter the elements comma separated in second array - ")
ary_1 = arr_1.split(",")
ary_2 = arr_2.split(",")

set_1 = {int(i) for i in ary_1}
set_2 = {int(g) for g in ary_2}

#print(set_1)
#print(set_2)

z = {c for c in set_1 if c in set_2}
print(f"The intersection of two sets is {z}")
