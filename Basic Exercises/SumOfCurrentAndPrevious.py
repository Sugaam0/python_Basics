# Write a program to iterate the first 10 numbers and in each iteration, print the sum of the current and previous number.

prev_num = 0

currrent_num = 1

while currrent_num <= 10:
    sum = prev_num + currrent_num
    print("Sum of " + str(prev_num) + " and " + str(currrent_num) + " is " + str(sum))
    prev_num += 1
    currrent_num +=1