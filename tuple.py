a = ('a','vani',[1,2])
print(a.count('vani'))
print(len(a))
print(a.index([1,2]))



a = {2:3,'vani':'noor','sree':'roja'}
print(list(a.values()))
print(list(a.keys()))
#print(a.pop(2))
print(a)
print(list(a.items()))
#print(a.clear())
print(a)
print(a.get(2))
a['vu']='uv'
print(a)
b = {'e':2}
print(a.update(b))
print(a)

a = {'e','f',3,3,4,5}
print(a)
b = {'f','r',4,6,8}
print(a.update(b))
print(a)
print(a.union(b))
print(a.intersection(b))
print(a.add('g'))
print(a)
print(a.pop())
print(a.remove('g'))
print(a)
#print(a.clear())
print(f"{a}{b}")
