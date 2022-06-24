with open('small_dhunna/nishi.txt','r') as sree:
    a =sree.readlines()
    d ={}
    for i in a:
        c = i.replace('\n','')
        b =c.split(', ')
        if b[0] in d:
            d[b[0]] = d[b[0]] + 1
        else:
            d[b[0]] = 1
print(d)


import json
with open('vani.txt','r') as sree:
    b = sree.read()
    print(b)
    # print(json.loads(b))
    # # c = eval(b)['vani']
    # # print(c)

# Python program to convert
# Python to JSON


import json

dictionary = {
    "id": "04",
    "name": "sunil",
    "department": "HR"
}
# Serializing json
json_object = json.dumps(dictionary, indent=4)
d = json_object
print(type(d))


dictionary = {
    "id": "04",
    "name": "sunil",
    "department": "HR"
}

with open('new_file.txt', 'w') as fr:
    json.dump(dictionary, fr)

