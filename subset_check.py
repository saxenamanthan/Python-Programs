list_ary1 = input("Enter the elements of first list comma separated - ")
list_ary2 = input("Enter the elements of second list comma separated - ")

int_ary1 = {int(i) for i in list_ary1.split(",")}
int_ary2 = {int(k) for k in list_ary2.split(",")}

#print(int_ary1)
#print(int_ary2)

s = {i for i in int_ary1 if i in int_ary2}

if s == int_ary2:
    print(True)
else:
    print(False)
#print(s)