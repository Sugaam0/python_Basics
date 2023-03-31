# Iterate the given list of numbers and print only those numbers which are divisible by 5

numbers = [10,20,22,21,80]

print("Given list is : ")
print(numbers)

for num in numbers:
    if num % 5 == 0:
        print(num)