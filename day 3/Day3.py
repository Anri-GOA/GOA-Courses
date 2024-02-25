#Drawing A Enviroment
from turtle import *
import turtle
import turtle as t
import math


shape("turtle")
speed(20)
bgcolor("gold")
title("Goa day 3 homework housees with Enviroment")


#Drawing A Sun
penup()
goto(-600,200)
pendown()
color("Orange")
begin_fill()
circle(60)
end_fill()
#Drawing a House

#Drawing a suare
penup()
goto(-400,-100)
pendown()
shape("turtle")
color("Orange")
begin_fill()
for i in range(4):
    fd(200)  
    lt(90)  
end_fill()

#drawing a door using Loop
fd(70)
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
color("brown")
pencolor("black")
penup()
goto(-380,50)
pendown()
begin_fill()
for i in range(4):
    lt(90)
    fd(30)
end_fill()

#Drawing 2 Window
color("brown")
pencolor("black")
penup()
goto(-250,50)
pendown()
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
goto(-200,100)
pendown()
begin_fill()
lt(400)
fd(150)
lt(100)
fd(150)

end_fill()


#Drawing A 2 House 



#Square
penup()
goto(200,100)
pendown()
color = "red"
fillcolor("red")
begin_fill()
lt(130) #start
fd(400)# first 
lt(270)#down
fd(250)#down
lt(270)
fd(400)
end_fill()


#Door

color = "blue"
fillcolor("blue")
begin_fill()
lt(180)
fd(150)
lt(90)
fd(120)
lt(270)
fd(50)
lt(270)
fd(120)
end_fill()

#1 Window

penup()
goto(250,50)
pendown()
color = "black"
fillcolor = "black"
begin_fill()
lt(90)
fd(30)
lt(90)
fd(30)
lt(90)
fd(30)
end_fill()


#2 Window
penup()
goto(520,80)
pendown()
color = "black"
fillcolor = "black"
begin_fill()
lt(90)
fd(30)
lt(90)
fd(30)
lt(90)
fd(30)
end_fill()


# 3 roof


penup()
goto(600,100)
pendown()
color = "blue"
fillcolor = "blue"
begin_fill()
lt(68)
fd(200)
lt(40)
fd(240)
end_fill()


#Sky


##Drawong Sky
penup()
goto(100,300)
circle =(6)
radius = 50
sky_color = "orange"
pendown()

penup()
goto(50,300)
def filled_circle(radius, sky_color):
    t.color(color,color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()



filled_circle(radius,sky_color)
t.forward(radius)
filled_circle(radius,sky_color)
t.right(90)
filled_circle(radius,sky_color)
t.right(90)
filled_circle(radius,sky_color)
t.right(90)
filled_circle(radius,sky_color)
t.right(90)
end_fill()


penup()
goto(-800,400)
pendown() 

radius = 50
sky_color="orange"

def filled_circle(radius, color):
    t.color(color,color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()


filled_circle(radius,sky_color)
t.forward(radius)
filled_circle(radius,sky_color)
t.right(100)
filled_circle(radius,sky_color)
t.right(100)
filled_circle(radius,sky_color)
t.right(100)
filled_circle(radius,sky_color)
t.right(100)
end_fill()


#Tree
  
# Function to draw rectangle 
def drawRectangle(t, width, height, color): 
    t.fillcolor(color) 
    t.begin_fill() 
    t.forward(width) 
    t.left(90) 
    t.forward(height) 
    t.left(90) 
    t.forward(width) 
    t.left(90) 
    t.forward(height) 
    t.left(90) 
    t.end_fill() 
  
      
# Function to draw triangle     
def drawTriangle(t, length, color): 
    t.fillcolor(color) 
    t.begin_fill() 
    t.forward(length) 
    t.left(135) 
    t.forward(length / math.sqrt(2)) 
    t.left(90) 
    t.forward(length / math.sqrt(2)) 
    t.left(135) 
    t.end_fill() 
  
# reating turtle object 
tip = turtle.Turtle() 
tip.color ("black") 
tip.shape ("turtle") 
tip.speed (20) 
  
  
# Tree base 
tip.penup() 
tip.goto(100, -130) 
tip.pendown() 
drawRectangle(tip, 20, 40, "brown") 
  
  
# Tree top 
tip.penup() 
tip.goto(65, -90) 
tip.pendown() 
drawTriangle(tip, 90, "lightgreen") 
tip.penup() 
tip.goto(70, -45) 
tip.pendown() 
drawTriangle(tip, 80, "lightgreen") 
tip.penup() 
tip.goto(75, -5) 
tip.pendown() 
drawTriangle(tip, 70, "lightgreen")
pendown()



#Drawing A 3 House 

#Square
penup()
goto(-100,0)
pendown()
fillcolor = "orange"
begin_fill()
lt(110)
fd(200)
lt(90)
fd(120)
lt(90)
fd(200)
lt(90)
fd(120)
end_fill()


#Door
penup()
goto(-130,-200)
pendown()
fillcolor = "purple"
begin_fill()
lt(180)
fd(60)
lt(90)
fd(100)
lt(270)
fd(40)
lt(270)
fd(100)
end_fill()


#1 Window
penup()
goto(-80,-50)
pendown()
fillcolor = "black"
begin_fill()
lt(90)
fd(30)
lt(90)
fd(30)
lt(90)
fd(30)
lt(90)
fd(30)
end_fill()

#2 window
penup()
goto(-20,-50)
pendown()
fillcolor = "black"
begin_fill()
lt(90)
fd(30)
lt(90)
fd(30)
lt(90)
fd(30)
lt(90)
fd(30)
end_fill()

#roof
penup()
goto(-100,0)
pendown()
fillcolor = "orange"
begin_fill()
lt(150)
fd(100)
lt(250)
fd(130)
end_fill()



exitonclick()