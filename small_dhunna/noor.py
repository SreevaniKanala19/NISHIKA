class roja:
    def __init__ (self,a,b):
        self.a = a
        self.b = b
    def add(self,c,d):
        print(self.a)
        print(self.b)
        return c+d
    def sub(self,e,f):
        print(self.a)
        print(self.b)
        return e-f
z = roja(3,4)
x = z.sub(5,4)
print(x)





class nivasree:
    a = 2
    b = 5
    def __init__ (self,a,b):
        self.a = a
        self.b = b
    def mul(self,m,n):
        print(self.a)
        print(self.b)
        return m*n
    def div(self,x,y):
        print(self.a)
        print(self.b)
        return x/y
e = nivasree(100,25)
f = e.div(200,50)
print(f)
