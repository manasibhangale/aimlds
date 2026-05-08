class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):
        return Vector(self.x+other.x,self.y+other.y)
    def __sub__(self,other):
        return Vector(self.x-other.x,self.y-other.y)
    def __mul__(self,other):
        return Vector(self.x*other.x,self.y*other.y)
    def __equal__(self,other):
        return Vector(self.x==other.x and self.y==other.y)
    def __repr__(self):
        return f"{self.x} and {self.y}"
v1=Vector(2,3)
v2=Vector(4,5)
print(v1+v2)
print(v1==v2)
print(v1-v2)
print(v1*v2)