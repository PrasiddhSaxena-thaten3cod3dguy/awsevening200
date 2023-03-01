num=int(input("Eneter Number: "))
duplicate=num
temp=num
count=0

while temp >0:
    temp = temp // 10
    count = count + 1

print(count)

sum=0

while num>0:
    rem = num % 10
    sum = sum + (rem**count)
    num = num // 10

print(sum)

if duplicate == sum:
    print("Armstrong")
else:
    print("Jinga lala Hohoho ")
