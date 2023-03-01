"""
WAP to find the cube sum of the number entered from 1^3.


User--> 8

O/P --> 1^3 + 2^3 + 3^3 + 4^3 + 5^3 + 6^3 + 7^3 + 8^3 = x

"""
#For Loop Approach
# num=5
# sum=0
# for x in range(1,num+1):
#     sum = sum + x**3

# print(sum)

#While Loop Approach

num=5
sum=0
count=1

while count <= num:
    sum = sum + count ** 3
    count = count + 1

print(sum)
