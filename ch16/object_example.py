class Entity:
    """ Entity class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):
        """ Create a new Entity at the given coordinates. """
        self.x = initX
        self.y = initY
        self.speed=5 #default speed all Entity objects start with
        self.width=None #making them None to start with, maybe I will use later?
        self.height=None


    def getX(self): #method to get the current value of x
        return self.x

    def getY(self):
        return self.y

    def move_it(self): #change Entity's x value by the speed, in other words move it
        self.x+=self.speed
        return self.x #return the new value



p = Entity(7,6)
j=Entity(5,0) #another instance
k=Entity(2,1) #another instance, you get the point I can make a ton of these really quick

print(p.getX())
print(p.getY())
p.speed=1000000000000 #though it starts with a default, I can change the objects speed
print(p.speed)
print(p.move_it())
print(p.x)