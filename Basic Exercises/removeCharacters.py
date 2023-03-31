# Write a program to remove characters from a string starting from zero up to n and return a new string

string = input("ENter any string : ")

count = int(input("How many characters you want to remove ? "))


def remove_chars(word, n):
    x = word[n:]
    return x

print(remove_chars(string,count))