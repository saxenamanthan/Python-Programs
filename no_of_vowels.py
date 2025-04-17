str = input("Enter the string - ")
str = str.lower()

"""
count = 0
vowels_str = "aeiou"

for ch in str:
    if ch in vowels_str:
        count +=1
        
print(count)        
"""

array = [ch for ch in str if ch in "aeiou"]
#print(array)
print(f"The number of vowels in the given string {str} is {len(array)}")


