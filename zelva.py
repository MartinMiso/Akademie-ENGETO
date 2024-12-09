import turtle
# okno pro želvu
screen = turtle.Screen()

# samotná želva
t = turtle.Turtle()
t.speed(2)
t.color("orange")
# zvednutí pera
t.penup()
#přesun na pozici
t.goto(-20, 50)
# položení pera
t.pendown()
t.circle(50, 360)
t.goto(30, 50)
t.circle(50, 360)
t.goto(80, 50)
t.circle(50, 360)
t.penup()

# vločka
for _ in range(6):
  t.goto(10, 20)
  t.pendown()
  t.forward(30)
  t.left(60)

# další želva a zmatený tvar
t2 = turtle.Turtle()
t2.color("green")
t2.speed(10)
t2.goto(20,50)

for _ in range(6):
  t2.forward(40)
  t2.left(60)

t2.goto(-20, 50)
t2.circle(50,360)
  
#screen.mainloop()