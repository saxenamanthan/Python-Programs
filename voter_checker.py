print("Voter Eligibility Checker")
a = input("Enter your age - ")
a = int(a)
if a < 18:
    print("You are uneligible to vote")
else:
    print("You are eligible to vote")