def vani(d):
    return d.upper()
def roja(variable):
    print(1)
    b = variable('this is dhunna')
    return b

d = vani
c = d('noor')


def findme(l):
    for i in l:
        for j in range(len(i)):
            print(i[3],end = '')
            break
s = ['vani', 'noor']
findme(s)

# question print fourth character in each word in a list as a word

a = [i*5 if i%2==0 else i for i in range(10)]
print(a)

a = {i:i*5 if i%2==0 else i for i in range(10)}
print(a)
a =lambda a,b : a+b
a(2,3)
print(a(2,3))

a =lambda a :a*7 if a%2==0 else a*9
a(529)
print(a(529))

#####  class
class staff:
    def __init__(self,name,cfms):
        self.name =  name
        self.cfms = cfms
    def secretariat(self,ps,welfare):
        print(self.name)
        print(self.cfms)
        print(f"our ps is {ps},our welfare is {welfare}")
a = staff('rampadu',11190008)
a.secretariat('siddadri','manoj kumar')





class village:
    a = 'rampadu'
    b = 'obulapuram'
    __c = 'pittigunta'
    def __init__(self,village1,village2):
        self.village1 = village1
        self.village2 = village2
    def panchayat(self,volunteerlist1,volunteerlist2,volunteerlist3):
        print(self.village1)
        print(self.village2)
        print(f"rampadu {volunteerlist1},obulapuram {volunteerlist2},pittigunta {volunteerlist3}")
    def life(self):
        print('vani is best')
a = village('rampadu','pittigunta')
print(a.a)
print(a.b)
a.panchayat(3,2,5)

class grampanchayat(village):
    def __init__(self,name):
        self.name = name
        super().__init__('adfads', 'adfadsf')
    def sec(self,sec):
        print(self.name)
        print(f"uppalur is one {sec}")
a = grampanchayat('guru')
a.panchayat(10,5,3)
a.life()
a.sec('gp')
class zero(grampanchayat):
    def __init__(self,one):
        self.one = one
    def first(self,second):
        print(f"{second} is second")
# a = zero('prizeone')
# a.first('vani')
# a.panchayat(3,5,10 )

def dhunna(*args):
    print(*args)
dhunna(1,2,3,4,5)

def dhunna1(**kwargs):
    print(kwargs['vami'])
dhunna1(vami='noor',dhunna = 5)
vaaa = 5

a = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
import sys
print('vvvvvvvvvvvv')
print(sys.getsizeof(a))
print(sys.getsizeof(iter(a)))

import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))
print(x.strftime("%a"))

def add(a,b):
    c = a+b
    return c
d = add(3,78)
print(d)



def add(a,b):
    return (a + b).upper()
def string_add(operation):
    addition = operation('vani','roja')
    print(addition)
string_add(add)


def mix(a):
    c = [i*5 if i%2==0 else i for i in a]
    return c
# def list(addition):
#     add = addition([2,4,5,6])
    print(add)
# list(mix)


def feb(n):
    a = 0
    b = 1
    for i in range(2,n):
        yield a,b
        a,b = b,a+b
a = feb(11)
print(a.__next__())
print(a.__next__())
print(a.__next__())

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



class family:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add(self,b,d):
        print(self.a)
        print(self.b)
        c = b/d
        return c
e = family(34,17)
f = e.add(16,8)
print(f)




a = 'sreevani'
b = ''
for i in a:
    b = i + b
print(b)
if a is b:
    print('given string is palindrome')
else:
    print('given string is not palindrome')


# Function to reverse words of string

def rev_sentence(sentence):
    # first split the string into words
    words = sentence.split(' ')

    # then reverse the split string list and join using space
    reverse_sentence = ' '.join(reversed(words))

    # finally return the joined string
    return reverse_sentence


if __name__ == "__main__":
    input = 'geeks quiz practice code'
    print(rev_sentence(input))







a = 'the monkey'
i = 2
print(b)
print(a[::-1])
print(a[:2] + a[3:])



a = 'jhfjwugfuagsufasufuiahfiuwah'
c = 0
for i in a:
    c = c+1
print(c)


a = 'akhg ajfkh akhfkqwh'
a.split(' ')
b = list(a)




a = 'vani is a good girl'
b =a.split(' ')
c = list(b)
d = c[::-1]
print(d)
e = ' '.join(d)
print(str(e))


def fib(n):
    a,b = 0,1
    for i in range(2,n):
        yield a,b
        a,b = b,a+b
e = fib(5)
print(e.__next__())
print(e.__next__())
print(e.__next__())



a = ['jabee','roja','chinni']
b = ['afreen']
c = 'vani'
print(a.reverse())
print(a)
a.append(b)
a.extend(c)
print(a)
a.pop(2)
a.remove('v')
#a.clear()
a.insert(3,'sree')
print(a)
print(len(a))




a = ('v','g','jabee','roja')
print(len(a))
print(a.count('v'))
print(a.index('g'))


a = {'g':'t',1:2}
b = {'vani':'jabee'}
a.update({'gs':'ete'})
print(a)
print(a.values())
print(a.keys())
print(a.items())
print(a.get('gs'))
b.pop('vani')
print(b)
#a.clear()
print(a)
del(a)


a = [i*5 for i in range(10)]
print(a)
a = [i*5 for i in range(10) if i%2==0]
print(a)
print([i*3 if i%2==0 else i*3 for i in range(10)])
print({i:i*3 for i in range(10)})
print({i:i*3 if i%2==0 else i for i in range(10)})

def mul(a,b,c):
    return a*b*c
print(mul(25,45,80))

def fib(n):
    a,b = 0,1
    for i in range(2,n):
        yield a,b
        a,b = b,a+b
c = fib(11)
print(c.__next__())
print(c.__next__())
print(c.__next__())
print(c.__next__())
print(c.__next__())
print(list(c))


def add(a):
    return a.upper()
def mix(operation):
    greeting = operation('this is sreevani kanala')
    print(greeting)
b = mix(add)


class add:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def mix(self,a,b,c):
        print(self.a)
        print(self.b)
        print(self.c)
        print(f"{a},{b},{c}")
a = add('roja','jabee','sree')
a.mix('rani','sree','ismaiel')



def sree_vani(a):
    a.mix('noor','fahf','aufeh')
sree_vani(a)

class roja_vani:
    def __init__(self,a):
        self.a = a
    def ja_bee(self,a):
        print(self.a)
        print(a*a)
    def bj(self,a,b,c):
        print(f"{a},{b},{c}")

g = roja_vani(add)
g.ja_bee(25)
g.bj('this is vani','digital assistant','rampadu')



a = 'vani'
print(a[:2]+a[3:])

a = 'nishika'
c = 0
for i in a:
    c = c+1
print(c)




a = [1,2,3]
for i , j in enumerate(a):
    print(i, j)



a = 'this is roja srivani and jabee'
b = a.split(' ')
print(b)
for i in b:
    if len(i)%2 == 0:
        print(i)


a = 'vani is a bad girl'
b = a.split(' ')
c = []
for i in range(len(b)):
    if len(b[i])>=2:
        c.append(b[i][0].upper() + b[i][1:-1] +b[i][-1].upper())
    else:
        c.append(b[i].upper())
d =' '.join(c)
print(d)

print('vani is a bad girl'.title())
s = "vani is a bad girl"
print(s.title().split())
print(' '.join(map(lambda s: s[:-1]+s[-1].upper(), s.title().split())))



a = 'vani19 noor100 roja 10 888'
b = a.split(' ')
print(b)
c = []
for i in b:
    alp, num = False, False
    for j in i:
        if j.isalpha():
            alp = True
        if j.isnumeric():
            num = True
        if alp and num:
            c.append(i)
            break
d =' '.join(c)
print(d)


a = 'vani dhunnapotu'
li = ['a','e','i','o','u']
for i in li:
    if i in a or i.upper() in a:
        pass
    else:
        print('not accepted')
        break
else:
    print('Accepted')


a = 'nishika'
b = a.find('i')
print(b)




a = 'noorroja'
b = 'sree vani'
c =''
print(len(a))
for i in b:
    if i in a:
        c = c+i
print(c)


a = [1,2,3,4,5,6]
a.remove(2)
print(a)
a.sort(reverse=True)
print(a)


ip = 'zaabbccddeeffgg'
op = ''
prev = ''
for i in ip:
    d = ip.count(i)
    if i != prev and i not in op:
        op = op + i + str(ip.count(i))

    else:
        prev = i
print(op)



a = ['chinni','vani','roja','sree']
c = a[0]
a[0] = a[-1]
a[-1] = c
print(a)


a = ['jabee','sky','earth']
a[0],a[-1] = a[-1],a[0]
print(a)


a = [20,45,78,89]
a[1],a[3] = a[3],a[1]
print(a)


a = [1,2,3,4,5,'ri','sky',9,'sree']
c = 0
for i in a:
    c = c+1
print(c)


a = ['sri','jo','jabee',4,5,6]
b = []
for i in a:
    b.insert(0,i)
print(b)


a = [2,2,4,5,'vani','jabee']
c = 0
for i in a:
    if i =='vani':
        c = c+1
print(c)


a = [12,67,98,34]
b = 1
for i in a:
    b = b*i
print(b)


a = [13,45,78,21]
pre = 0
for i in a:
    if i>pre:
        pre = i
    else:
        pass
print(pre)
a.remove(78)
print(a)
a.sort()
print(a)
print(a[2])


ip = 'aabbccddeeffgg'
op = ''
prev = ''
for i in ip:
    if i != prev and i not in op:
        op = op+i+str(ip.count(i))
    else:
        prev = i
print(op)























