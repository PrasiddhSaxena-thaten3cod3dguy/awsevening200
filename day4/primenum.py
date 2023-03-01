'''
WAP in function to find a num is prime or not.

'''
#First Approach

num=int(input("Enter a num: "))
flag=False
if num >=1:
    for i in range(2,num):
        if num % i == 0:
            flag=True
    
    if flag:
        print("Not a prime num.")
    else:
        print("Prime Number")
    