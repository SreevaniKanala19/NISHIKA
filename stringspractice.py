
def feb(a):
    for i in range(a):
        yield i
c = feb(11)
# print(c.__next__(), end='')
# print(c.__next__())
# for i in c:
#     print(i , end = '')

def add(a,b):
    c = a+b
    return c




a = 0
b = 1
for i in range(11):
    print(a, end='')
    a, b = b, a + b



a = 'laks,hmi'
print('asdfasdf')
print(a.find('i'))
print('u7hhhhhhhhhhhh')
print(a.replace('m','n'))
print(a.count('k'))
print(a.index('k'))
print(a.capitalize())
print(a.istitle())
print(a.split(','))
print(a.strip())
print(len(a))
print(a[:])
print(a[6:5:-1])

a = 'madam'
b = ""
for i in a:
    b = i + b
print(b)
