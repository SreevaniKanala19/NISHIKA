a = ['nishika']
a=[i*5 for i in a]
print(a)
a = ['noor','vani','roja',2]
#print(a.pop(2))
print(a.count('noor'))
#print(a.remove('vani'))
#a.clear()
print(a.index('noor'))
print(a.reverse())
print(a)
b = ['sree','jabbe']
a.append(b)
print(a)
a.extend(b)
print(a)
a[0] = 5
print(a)
a[1] = 'u'
print(a)
print(len(a))
#del(a)
print(a)
0



def div(a,b):
    c = a/b
    return c
a = 1000
b = 45
d = div(1000,45)
print(d)

def sree_vani(a,b):
    c = len(a)*len(b)
    return c
print(sree_vani('bagya','lakshmi'))


def feb(n):
    a = 0
    b = 1
    for i in range(2,n):

        yield a,b
        a, b = b, a + b
a = feb(11)
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__()) 
print(list(feb(11)))


