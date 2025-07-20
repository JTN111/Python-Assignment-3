def fact(n):
    if n<2:
        return 1
    else:
     return n * (fact(n-1))
#To take input on runtime, un-comment 1 and 2 and replace fact(5) with fact(n).
n = input('Enter a number: ')
n= int(n)
result= fact(n)
print("factorial of",n, "is",result)
