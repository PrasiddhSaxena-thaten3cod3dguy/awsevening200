def primenumsec():
    num=int(input("Enter The Number: "))
    flag=False
    if num >=1:
        for i in range(2,(num//2)+1):
            if (num % i == 0):
                flag=True
        
        if flag:
            print("Not a Prime Number")
        else:
            print("Prime Number")

primenumsec()