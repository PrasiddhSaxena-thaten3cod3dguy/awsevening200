import random 

num=random.randint(1, 50)
chance=1
flag=True
print(num)

#Approach:- 1 

while chance <=5 :
    guess=int(input("Enter Your guess: "))
    if guess > num:
        print("Try Lower")
    elif guess < num:
        print("Try Higher")
    else:
        print("Hoorah Jingalala Hoho")
    chance += 1

#Approach2
while (chance <=5 and flag==True):

    guess=int(input("Enter Your guess: "))
    if guess > num:
        print("Try Lower")
    elif guess < num:
        print("Try Higher")
    else:
        print("Hoorah Jingalala Hoho")
        flag=False
    chance += 1

#break approach3

while chance <= 5:
    guess=int(input("Enter Your guess: "))
    if guess > num:
        print("Try Lower")
    elif guess < num:
        print("Try Higher")
    else:
        print("Hoorah Jingalala Hoho")
        break
    chance += 1
