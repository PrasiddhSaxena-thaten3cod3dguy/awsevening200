'''
WAP calculator but here you have to accept operator also from the user 

I/P

4 
5 

%

'''
def add():
    num1=int(input("Enter First Num: "))
    num2=int(input("Enter Second Num: "))
    return num1 + num2

def subract():
    num1=int(input("Enter First Num: "))
    num2=int(input("Enter Second Num: "))
    return num1 - num2
def multiply():
    num1=int(input("Enter First Num: "))
    num2=int(input("Enter Second Num: "))
    return num1 * num2
def div():
    num1=int(input("Enter First Num: "))
    num2=int(input("Enter Second Num: "))
    return num1 / num2

operator=input("Enter the Operator: ")
if operator == "+":
    result=add()
elif operator == "-":
    result=subract()
elif operator == "*":
    result=multiply()
elif operator == "/":
    result=div()
else:
    print("No result")

print(result)
