#INIZIO CONFIGURAZIONE UMANO

import turtle
import random 
a=turtle.Turtle()
b=turtle.Turtle()
c=turtle.Turtle()
x=turtle.Turtle()
a.color("red")
b.color("blue")
c.color("pink")

lista_x=[25, 75, 125, 175]
lista_y=[-25, -75, -125, -175]
m=random.randint(0,3)
n=random.randint(0,3)
o=random.randint(0,3)
p=random.randint(0,3)
q=random.randint(0,3)
r=random.randint(0,3)
s=random.randint(0,3)
t=random.randint(0,3)
punti_player=0
punti_bot=0




def quadrato():
  for i in range(4):
    x.forward(50)
    x.right(90)
x.speed(0.25)
def righe():
  for i in range(4):
    quadrato()
    x.forward(50)
  x.right(90)
  x.forward(50)
  x.right(90)
  x.forward(200)
  x.left(180)
for i in range(4):
  righe()



def if_1():
  if m==o or m==q:
    m==t
  if n==p or n==r:
    n==s
if_1()

def goto_1():
  a.penup()
  a.goto((int(lista_x[m])),(int(lista_y[n])))
  b.penup()
  b.goto((int(lista_x[o])),(int(lista_y[p])))
  c.penup()
  c.goto((int(lista_x[q])),(int(lista_y[r])))
goto_1()



#INIZIO CONFIGURAZIONE BOT

aa=random.randint(0,3)
ab=random.randint(0,3)
ac=random.randint(0,3)
ad=random.randint(0,3)
am=random.randint(0,3)
an=random.randint(0,3)
ae=[(int(lista_x[aa])),(int(lista_y[ab]))]
af=[(int(lista_x[ac])),(int(lista_y[ad]))]
ao=[(int(lista_x[am])),(int(lista_y[an]))]



#CONFIGURAZIONE PRIMA NAVE
print("PRIMA NAVE")
print(lista_x)
print(lista_y)
print(aa)
print(ab)
ag=int(input("inserire x, da 1 a 4, guardando la lista 1: "))
ah=int(input("inserire y, da 1 a 4, guardando la lista 2: "))
ai=0
aj=0

while ((ag-1)!=aa or (ah-1)!=ab) or (ai!=aa or aj!=ab):
  ai=random.randint(0,3)
  aj=random.randint(0,3)
  if ai!=aa or aj!=ab:
    print("IL NEMICO HA SBAGLIATO")
  if ai==aa and aj==ab:
    print("PECCATO! L'AVVERSARIO HA ABBATTUTO LA PRIMA NAVE")
    punti_bot+=1
    break
  if(ag-1)==aa and (ah-1)==ab:
    print("BRAVO HAI ABBATTUTO LA PRIMA NAVE")
    punti_player+=1
    break
  ag=int(input("inserire x, da 1 a 4, guardando la lista 1: "))
  ah=int(input("inserire y, da 1 a 4, guardando la lista 2: "))

#CONFIGURAZIONE SECONDA NAVE 
print("SECONDA  NAVE")
print(lista_x)
print(lista_y)
print(ac)
print(ad)
ak=int(input("inserire x, da 1 a 4, guardando la lista 1: "))
al=int(input("inserire y, da 1 a 4, guardando la lista 2: "))
ap=0
ar=0

while ((ak-1)!=ac or (al-1)!=ad) or (ap!=ac or ar!=ad):
  ar=random.randint(0,3)
  ap=random.randint(0,3)
  if ap!=ac or ar!=ad:
    print("IL NEMICO HA SBAGLIATO")
  if ap==ac and ar==ad:
    print("PECCATO! L'AVVERSARIO HA ABBATTUTO LA SECONDA NAVE")
    punti_bot+=1
    break
  if(ak-1)==ac and (al-1)==ad:
    print("BRAVO HAI ABBATTUTO LA SECONDA NAVE")
    punti_player+=1
    break
  ak=int(input("inserire x, da 1 a 4, guardando la lista 1: "))
  al=int(input("inserire y, da 1 a 4, guardando la lista 2: "))



#CONFIGURAZIONE TERZA NAVE
print("TERZA NAVE")
print(lista_x)
print(lista_y)
print(am)
print(an)
ao=int(input("inserire x, da 1 a 4, guardando la lista 1: "))
at=int(input("inserire y, da 1 a 4, guardando la lista 2: "))
au=0
av=0

while ((ao-1)!=am or (at-1)!=an) or (au!=am or av!=an):
  au=random.randint(0,3)
  av=random.randint(0,3)
  if au!=am or av!=an:
    print("IL NEMICO HA SBAGLIATO")
  if au==am and av==an:
    print("PECCATO! L'AVVERSARIO HA ABBATTUTO LA SECONDA NAVE")
    punti_bot+=1
    break
  if(ao-1)==am and (at-1)==an:
    print("BRAVO HAI ABBATTUTO LA PRIMA NAVE")
    punti_player+=1
    break
  ao=int(input("inserire x, da 1 a 4, guardando la lista 1: "))
  at=int(input("inserire y, da 1 a 4, guardando la lista 2: "))


print(punti_player, punti_bot)