try:
    num=1/0
    print("In try")
    print(num)
except ZeroDivisionError:
    print("Dividing by zero you fool")
print("Done")