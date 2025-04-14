user_str = input("Enter a string - ")
user_array = list(user_str)
print(user_array)

user_array.reverse()
print(user_array)

reverse_user_str = "".join(user_array)
print(reverse_user_str)

if user_str == reverse_user_str:
    print("It is a palindrome number")
else:
    print("It is not a palindrome number")
    
