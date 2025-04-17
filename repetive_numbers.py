numbers_list = [1,9,3,9,2,3,1,3,3]

s = set(numbers_list)
largest_count = 0
largest_count_number = 0

for f in s:
    count = numbers_list.count(f)
    #print(f"Number {f} is coming {count} times") 
    if count > largest_count:
        largest_count = count
        largest_count_number = f


print(f"The number which is most repeating is {largest_count_number} with count {largest_count}")
