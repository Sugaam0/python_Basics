# Write a program to accept a string from the user and display characters that are present at an even index number.

string = input("Enter any string : ")

count = len(string)

for i in range(0,count,2):
    print(string[i])
   
