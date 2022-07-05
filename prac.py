ip = 'aabbccddeeffgg'
op = ''
prev = ''
for i in ip:
    if i != prev and i not in op:
        op = op+i+str(ip.count(i))
    else:
        prev = i
print(op)


num = 5
for i in range(1,11):
    print(f'{num}x{i} = {num*i}')