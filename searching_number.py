numbers = input("Enter the numbers - ")
number_to_search = input("Enter the number  to search - ")

arr = numbers.split(",")

if number_to_search in arr:
    print("Found")
else:
    print("Not Found")