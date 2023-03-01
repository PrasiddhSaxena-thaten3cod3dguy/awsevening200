num=int(input("Enter a num: "))
rev=0
while num > 0:
    temp= num % 10
    rev = rev * 10 + temp
    num = num // 10

print(f"The Reverse of the num is {rev}")

# #Python
# temp1=str(num)
# print(temp1)
# print(type(temp1))
# print(f"The Value of the reverse in python tricks is {temp1[::-1]}")