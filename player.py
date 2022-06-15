import turtle
import random 


class player():

    def __init__ (self,n4, n5, n6, px1, py1, px2, py2, px3, py3, list_x, list_y):
        self.px1 = px1
        self.py1 = py1
        self.px2 = px2
        self.py2 = py2
        self.px3 = px3
        self.py3 = py3               
        self.n4 = n4
        self.n5 = n5
        self.n6 = n6
        self.list_x = list_x 
        self.list_y = list_y 

    def changes(self):
        #p1
        if self.px1 == "A":
            self.px1 = -200
        if self.px1 == "B":
            self.px1 = -100
        if self.px1 == "C":
            self.px1 = 0
        if self.px1 == "D":
            self.px1 = 100
        if self.px1 == "E":
            self.px1 = 200
        if self.py1 == 1:
            self.py1 = 200
        if self.py1 == 2:
            self.py1 = 100
        if self.py1 == 3:
            self.py1 = 0
        if self.py1 == 4:
            self.py1 = -100
        if self.py1 == 5:
            self.py1 = -200

        #p2
        if self.px2 == "A":
            self.px2 = -200
        if self.px2 == "B":
            self.px2 = -100
        if self.px2 == "C":
            self.px2 = 0
        if self.px2 == "D":
            self.px2 = 100
        if self.px2 == "E":
            self.px2 = 200
        
        if self.py2 == 1:
            self.py2 = 200
        if self.py2 == 2:
            self.py2 = 100
        if self.py2 == 3:
            self.py2 = 0
        if self.py2 == 4:
            self.py2 = -100
        if self.py2 == 5:
            self.py2 = -200

        #p3
        if self.px3 == "A":
            self.px3 = -200
        if self.px3 == "B":
            self.px3 = -100
        if self.px3 == "C":
            self.px3 = 0
        if self.px3 == "D":
            self.px3 = 100
        if self.px3 == "E":
            self.px3 = 200
        
        if self.py3 == 1:
            self.py3 = 200
        if self.py3 == 2:
            self.py3 = 100
        if self.py3 == 3:
            self.py3 = 0
        if self.py3 == 4:
            self.py3 = -100
        if self.py3 == 5:
            self.py3 = -200



    def turtling(self):
        self.n4.penup()
        self.n5.penup()
        self.n6.penup()
        self.n4.hideturtle()
        self.n5.hideturtle()
        self.n6.hideturtle()
        self.n4.color("blue")
        self.n5.color("green")
        self.n6.color("pink")



    def positioning(self):  
#        self.n4.goto(self.list_x[int(random.randint(0,4))],self.list_y[int(random.randint(0,4))],)
#       self.n4.showturtle()
#        self.n5.goto(self.list_x[int(random.randint(0,4))],self.list_y[int(random.randint(0,4))],)
#        self.n5.showturtle()
#        self.n6.goto(self.list_x[int(random.randint(0,4))],self.list_y[int(random.randint(0,4))],)
#        self.n6.showturtle()
        self.n4.goto(self.px1, self.py1)
        self.n4.showturtle()
        self.n5.goto(self.px2, self.py2)
        self.n5.showturtle()
        self.n6.goto(self.px3, self.py3)
        self.n6.showturtle()