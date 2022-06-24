class module:
    def __init__(self,name, rollno):
        self.name = name
        self.rollno = rollno
    def part(self,branch,college):
        print(self.name)
        print(self.rollno)
        print(f"this is my {branch},this is my {college}")
# a = module('roja',15)
# a.part('ECE', 'YVU')
class abcd:
    def vvvv(self):
        print(4554866)
    def yyyyyy(self):
        print(7887889)

class section(module, abcd):
    def __init__(self,a,b,name,rollno):
        self.a = a
        self.b = 2
        module.__init__(self, name,rollno)
    def element(self,score,avg):
        print(self.a)
        print(self.b)
        print(f"this is my {score},this is {avg}")
x = section(40,45,'sree',20)
x.part('EEE','AITS')
x.element(780,300)
y = section(80,45,'vani',30)
y.part('ECE','GOUTHAMI')
y.element(900,300)
y.vvvv()

