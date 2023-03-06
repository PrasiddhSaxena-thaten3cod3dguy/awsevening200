import json
with open("sample.json","r",encoding='utf-8') as file:
    data=json.load(file)
    print(data)
    print(type(data))

