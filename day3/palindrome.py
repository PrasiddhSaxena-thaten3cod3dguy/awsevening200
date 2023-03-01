num=int(input("Enter a num: "))
duplicate=num
rev=0
while num > 0:
    temp= num % 10
    rev = rev * 10 + temp
    num = num // 10

print(f"The Reverse of the num is {rev}")

if duplicate == rev:
    print("Palindrome")
else:
    print("Not Palindrome")