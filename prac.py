ip = 'aabbccddeeffgg'
op = ''
prev = ''
for i in ip:
    if i != prev and i not in op:
        op = op+i+str(ip.count(i))
    else:
        prev = i
print(op)