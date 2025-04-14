str = "Hello World"
print(f"number of l letters in {str} is {str.count('l')}")
print(f"number of o letters in {str} is {str.count('o')}")
print(f"number of word Hello in {str} is {str.count('Hello')}")
print(f"Finding character e index {str} is {str.find('e')}")
print(f"Finding character e index {str} is {str.find('Hello')}")
print(f"Finding character e index {str} is {str.find('World')}")
print(f"Checking {str} is starting with H or not {str.startswith('H')}")
print(f"Checking {str} is starting with Hello or not {str.startswith('Hello')}")
print(f"Checking {str} is ending with d or not {str.endswith('d')}")
print(f"Checking {str} is ending with World or not {str.endswith('World')}")

arr = str.split()
print(arr)

str3 = "a:b:c"
arr1 = str3.split(":")
print(arr1)

str4 = " ".join(arr1)
print(str4)

str5 = "-".join(arr)
print(str5)                                                               






