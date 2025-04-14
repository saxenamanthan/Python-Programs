a = ["g","f","a","b","c","d"]
a.append("r")
print(f"{a}")
a.insert(1,"f")
print(a)

a.pop()
print(a)

a.pop(2)
print(a)

i = a.index("a")
print(i)

d = a.index("c")
print(d)

a.append("a")
a.append("a")
a.append("a")
print(a)

a_count = a.count("a")
print(f"The count of a in array {a} is {a_count}")

a.sort()
print(a)

a.sort(reverse = True)
print(a)

arr = [7,6,90,0]
arr.reverse()
print(arr)

