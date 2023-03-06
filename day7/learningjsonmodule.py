import json 

# data={
#     "Name":"Prasiddh",
#     "Age": 22
# }

# file=open("sample.json","w",encoding='utf-8')
# file.write(json.dumps(data,indent=1))
# file.close()

file=open("sample.json","r",encoding='utf-8')
filedata= json.load(file)
file.close()

print(filedata)
print((type(filedata)))