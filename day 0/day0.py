from turtle import *
import turtle
# We want to paint a house

bgcolor("black")

speed(50)

title("Goa day 0 homework house with windows")

pensize(5)
pencolor("gold")
#Drawing a suare
goto(0,0)
shape("turtle")

for i in range(4):
    fd(200)  
    lt(90)  


#drawing a door using Loop
forward(70)
color("yellow")
pencolor("orange")
begin_fill()
left(90)
for i in range(1):
    fd(120)
    rt(90)
forward(60)
for i in range(1):
    rt(90)
    fd(120)
end_fill()

   
#Drawing 1 WInodw
color("orange")
pencolor("black")
penup()
goto(30,160)
begin_fill()
for i in range(4):
    lt(90)
    fd(30)
end_fill()

#Drawing 2 Window
color("orange")
pencolor("black")
penup()
goto(140,160)
begin_fill()
for i in range(1):
    lt(180)
    fd(30)
for i in range(4):
    rt(90)
    fd(30)

end_fill()

#Drawing Roof

color=("red")
pencolor("gold")
penup()
goto(200,200)
begin_fill()
lt(400)
fd(150)
lt(100)
fd(150)

end_fill()

#drawing a tree
tree = turtle.Turtle()
tree.penup() # lift pen off of "paper"
tree.goto(-180,-180) # move to desired location
tree.pendown() # make pen touch the "paper" again

tree.begin_fill()
tree.goto(0,220)
tree.goto(180,-180)
tree.goto(7,-180)
tree.goto(7,-260)
tree.goto(-7,-260)
tree.goto(-7,-180)
tree.goto(-180,-180)
tree.end_fill()

#drawing a staar
tree.fillcolor('yellow')

tree.penup()
tree.goto(0,260)
tree.pendown()

tree.begin_fill()
tree.goto(11,230)
tree.goto(40,230)
tree.goto(16,211)
tree.goto(26,181)
tree.goto(0,200)
tree.goto(-26,181)
tree.goto(-16,211)
tree.goto(-40,230)
tree.goto(-11,230)
tree.goto(0,260)
tree.end_fill()

exitonclick()