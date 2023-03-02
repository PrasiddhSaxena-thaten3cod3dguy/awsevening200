'''
WAP to armstrong's number, palindrome number, and sum of digits depending on users choice.
'''

def armstrong(num):
    sum=0
    dup=num
    dup2=num
    count=0
    while num>0:
        count +=1
        num=num // 10 
    
    while dup2 >0:
        rem = dup2 % 10
        sum = sum + (rem**count)
        dup2 = dup2 // 10
    
    if sum == dup:
        print("Armstrong")
    else:
        print("Not Armstrong")

def palindrome(num):
    rev=0
    dup=num
    while num>0:
        rem= num % 10
        rev = rev * 10 + rem
        num = num // 10
    if rev == dup:
        print("Palindrome")
    else:
        print("Not Palindrome")

def sumofdigits(num):
    sum=0
    while num > 0:
        rem = num % 10
        sum = sum + rem
        num = num //10
    print(f"Result: {sum}")

number=int(input("Enter The Number: "))

print("Please Select one of the option from following:\n1.Armstrong Number\n2.Palindrome\n3.Sum Of digits")

choice=int(input("The Choice: "))

if choice == 1:
    armstrong(number)
elif choice == 2:
    palindrome(number)
elif choice == 3:
    sumofdigits(number)
else:
    print("Dont Act Smart you fool !!")
    