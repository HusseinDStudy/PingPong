from turtle import *
import turtle
#prblm de vitesse demande le prof
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)


#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed("slowest")
forward(1)#speed(0) 
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()#to not draw a line
paddle_a.goto(-350, 0)

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed("slowest")
forward(1)#speed(0) 
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()#to not draw a line
paddle_b.goto(350, 0)

#Ball
ball = turtle.Turtle()
ball.speed("slowest")
forward(1)#speed(1)
ball.shape("square")
ball.color("white")
ball.penup()#to not draw a line
ball.goto(0, 0)
ball.dx = 2#bouge par 2px caq mvmt horizentale
ball.dy = -2#bouge par 2px caq mvmt verticalement

#Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)
    
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)
    
#Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "z")
wn.onkeypress(paddle_a_down, "s")

wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


#Main Game Loop
while True:
    wn.update()
    #Move the ball
    ball.setx(ball.xcor() + ball.dx)#bouge par 2px caq mvmt horizentale
    ball.sety(ball.ycor() + ball.dy)#bouge par 2px caq mvmt verticalement
    
    #Border checking
    #Y
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    #X
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
    elif ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
    #Paddle and ball collisions
    if ( ball.xcor() > 340 and ball.xcor() < 350)and ( ball.ycor() <  paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40 ):
        ball.setx(340)
        ball.dx *= -1
    if ( ball.xcor() > -340 and ball.xcor() < -350)and ( ball.ycor() <  paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40 ):
        ball.setx(-340)
        ball.dx *= -1
        
        
