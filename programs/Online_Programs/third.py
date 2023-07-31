import turtle as t
import colorsys
s=t.Screen()
t.title("SuPrIyA")
t.bgcolor('black')
t.tracer(10)
m=0.9
n=95

for i in range(450):
    c=colorsys.hsv_to_rgb(m,1,1)
    m+=0.005
    t.pencolor(c)
    t.right(90)
    t.forward(i+1)
    t.left(90)
    t.forward(i)
    t.circle(2,n)
    t.left(120)
    t.circle(m,1)
    t.hideturtle()
    
t.done()