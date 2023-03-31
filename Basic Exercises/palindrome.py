# Write a program to check if the given number is a palindrome number.

number = int(input("enter any string : "))

def palindrome(number):
    print("your number  is : ", number)

    original = number
    reverse = 0
    i=1
    while number > 0:
        remainder = number % 10
        reverse = (reverse * 10) + remainder
        number //= 10
    
    if original == reverse:
        return True
    else:
        return False
    

print("palindrome = " , palindrome(number))





