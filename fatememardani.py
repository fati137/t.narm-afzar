import turtle 
import random

emtiyaz=0

screen=turtle.Screen()
screen.setup(600,600)
screen.bgcolor('cyan')
screen.title('بازی')

wal=turtle.Turtle()
wal.up()
wal.goto(-275,275)
wal.down()
wal.width(4)
for i in range(4):
    wal.fd(550)
    wal.rt(90)

lki=turtle.Turtle()
lki.shape('turtle')
lki.color('darkgreen')
lki.shapesize(2)
lki.up()
bal=turtle.Turtle()
bal.shape('circle')
bal.color('blue')
bal.up()
bal.goto(random.randint(-260,260),random.randint(-260,260))

def right():
    lki.seth(0)
    lki.fd(20)
def left():
    lki.seth(180)
    lki.fd(20)
def up():
    lki.seth(90)
    lki.fd(20)
def down():
    lki.seth(270)
    lki.fd(20)
screen.listen()
screen.onkey(right,'d')
screen.onkey(left,'a')
screen.onkey(up,'w')
screen.onkey(down,'s')
writ=turtle.Turtle()
writ.up()
writ.goto(-270,275)
writ.ht()
writ.color('black')
writ.write('امتیاز شما:'+str(emtiyaz),font=14)
while True:
    lki.fd(1)
    if lki.xcor() > 270 or lki.xcor() < -270 or lki.ycor() > 270 or lki.ycor() < -270:
        lki.right(180)
        emtiyaz=emtiyaz-3
        writ.clear()
        writ.write('امتیاز شما:'+str(emtiyaz),font=14)
    if lki.distance(bal)<20:
        bal.goto(random.randint(-260,260),random.randint(-260,260))
        emtiyaz=emtiyaz+6
        writ.clear()
        writ.write('امتیاز شما:'+str(emtiyaz),font=14)
        if emtiyaz>=30:
            writ.goto(-100,0)
            writ.write(str(emtiyaz),font=24+'تبریک می گویم شما با این امتیاز برنده شدید!!!')
            break

screen.mainloop()