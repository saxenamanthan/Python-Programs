print("Leap year or not")
year = input("Enter the year - ")
year = int(year)
if year % 4 == 0:
    print("It is a Leap Year")
elif year % 4 != 0:
    print("It is not a Leap Year")