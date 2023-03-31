# Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.

numbers = [1,2,3,4,5,6]
numbers1 = [1,2,3,4,1]

def to_check(number):
    print("Given list is :")
    print(number)
    first_num = number[0]
    last_num = number[-1]

    if(first_num == last_num):
        return True
    else:
        return False

print("result is : "+ str(to_check(numbers)))
print("result is : "+ str(to_check(numbers1)))