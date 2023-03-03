# file=open("test.txt","w",encoding='utf-8')
# name=input("Enter the name: ")
# file.writelines(name)
# file.close()

file=open("test1.txt","r",encoding='utf-8')
data=file.readlines()
print(data)
file.close()

