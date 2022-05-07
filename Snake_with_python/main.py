#importing libraries
import sys

import pygame
import turtle
import random
import time

Run_1 = False # xac dinh xem map 1 hay 2
#creating turtle screen
screen = turtle.Screen()
def screen_0():
    screen.title('Snake_Game_ne')
    screen.setup(width=700, height=700)
    screen.tracer(0)  # dung man hinh ve lai
    turtle.bgcolor('turquoise')
def screen_1():
    turtle.speed(5)
    turtle.pensize(4)
    turtle.penup()
    turtle.goto(-310, 250)
    turtle.pendown()  # bat dau ve, ve khi di chuyen
    turtle.color('black')
    turtle.forward(600)
    turtle.right(90)
    turtle.forward(500)
    turtle.right(90)
    turtle.forward(600)
    turtle.right(90)
    turtle.forward(500)
    turtle.penup()  # dung ve
    turtle.hideturtle()
def screen_2():
    barrier = turtle.Turtle()
    barrier.penup()
    barrier.goto(-200, 80)
    barrier.color("red")
    barrier.pensize(20)
    barrier.pendown()
    barrier.left(90)
    barrier.forward(100)
    barrier.right(90)
    barrier.forward(100)
    barrier.penup()

    barrier.goto(100, 200)
    barrier.color("red")
    barrier.pensize(20)
    barrier.pendown()
    barrier.right(90)
    barrier.forward(340)
    barrier.right(90)
    barrier.penup()

    barrier.goto(-200, -80)
    barrier.color("red")
    barrier.pensize(20)
    barrier.pendown()
    barrier.left(90)
    barrier.forward(100)
    barrier.left(90)
    barrier.forward(100)
    barrier.penup()
text = turtle.Turtle()
text.goto(0,0)
text.write("Ban muon choi map 1 hay 2?\n",align="center",font=("Time New Roman",24,"bold"))
text.write("(nhan phim 1 hoac 2 de chon ne)",align="center",font=("Time New Roman",24,"bold"))

text.hideturtle()
def option_1():
    if True:
        text.clear()
        screen_1()
        global Run_1
        Run_1 = True
def opiton_2():
    if True:
        text.clear()
        screen_1()
        screen_2()
screen_0()

# nhan 1 chon map 1 va nguoc lai
screen.listen()
screen.onkeypress(option_1,"1")
screen.onkeypress(opiton_2,"2")


#score
score = 0
delay = 0.1


#snake
snake = turtle.Turtle()
snake.speed(0)
snake.shape('square')
snake.color("black")
snake.penup()
snake.goto(0,0)
snake.direction = 'stop'

#food
fruit = turtle.Turtle()
fruit.speed(0)
fruit.shape('circle')
fruit.color('#FFCC66')
fruit.penup()
fruit.goto(30,30)

old_fruit=[]

#scoring
scoring = turtle.Turtle()
scoring.speed(0)
scoring.color("black")
scoring.penup()
scoring.hideturtle()
scoring.goto(0,300)
scoring.write("Score :",align="center",font=("Time New Roman",24,"bold"))

#define how to move
def snake_go_up():
    if snake.direction != "down":
        snake.direction = "up"

def snake_go_down():
    if snake.direction != "up":
        snake.direction = "down"

def snake_go_left():
    if snake.direction != "right":
        snake.direction = "left"

def snake_go_right():
    if snake.direction != "left":
        snake.direction = "right"

def snake_move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)

    if snake.direction == "down":
        y = snake.ycor() # tra lai toa do cua snake
        snake.sety(y - 20)

    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)

    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)

# Keyboard bindings
screen.listen() #(để thu thập các sự kiện chính). Các đối số giả được cung
                # cấp để có thể chuyển listen()đến phương thức onclick.
screen.onkeypress(snake_go_up, "Up")
screen.onkeypress(snake_go_down, "Down")
screen.onkeypress(snake_go_left, "Left")
screen.onkeypress(snake_go_right, "Right")
#main loop

def pause_game():
    time.sleep(1)
    screen.clear()
    screen.bgcolor('turquoise')
    scoring.goto(0, 0)
    scoring.write("    GAME OVER \n Your Score is {}".format(score), align="center",
                  font=("Time New Roman", 30, "bold"))

def new_fruit(color):
    ## creating new_ball
    new_fruit = turtle.Turtle()
    new_fruit.speed(0)
    new_fruit.shape('square')
    new_fruit.color(color)
    new_fruit.penup()
    old_fruit.append(new_fruit)

def random_position_fruit():
    x = random.randint(-280, 260)
    y = random.randint(-240, 240)
check = True
timer = pygame.time.get_ticks
timeout = 5 # thoi gian cho ran di xuyen vat can
# milliseconds
pygame.init() # bat dau tinh gio
deadline = int(timer()/1000) + timeout

while True:

        now = int(timer() / 1000)
        screen.update()
        if (now >= deadline):
            check = True # check  == true: het thoi gian di xuyen vat can
            #snake and fruit coliisions
        if snake.distance(fruit)<(20):  #khoang cach tu snake toi fruit
                x = random.randint(-280, 260)
                y = random.randint(-240, 240)
                while (x == 100 and (y >= -140 and y<=200)):
                    random_position_fruit()
                while (y == 180 or y ==-180 and (x >= -200 and x<= -100)):
                    random_position_fruit()
                # fruit dac biet
                if (score!=0 and (score+1) % 5 == 0):
                    fruit.shape("square")
                    fruit.color("blue")
                else:
                # fruit binh thuong
                    fruit.shape("circle")
                    fruit.color("yellow")
                    check = True
                fruit.goto(x,y)
                if(score) % 5 == 0 and score != 0:
                    check = False
                    if now < deadline:
                        check = False
                score += 1
                scoring.clear()  # xoa bo trang thai hien thoi
                scoring.write("Score:{}".format(score), align="center", font=("Time New Roman", 24, "bold"))
                delay-=0.001
                color = "yellow"
                new_fruit(color)

        #adding ball to snake

        for index in range(len(old_fruit)-1,0,-1):
                a = old_fruit[index-1].xcor()
                b = old_fruit[index-1].ycor()

                old_fruit[index].goto(a,b)

        if len(old_fruit)>0:
                a= snake.xcor()
                b = snake.ycor()
                old_fruit[0].goto(a,b)
        snake_move()
        if check == True:
            deadline = now + timeout # lam moi deadline
            if Run_1 == False:
            ##va cham voi chuong ngai vat
                if (snake.xcor() == -200 and (snake.ycor() >= 80 and snake.ycor() <= 180)) or (
                    snake.ycor() == 180 and (snake.xcor() >= -200 and snake.xcor() <= -100)):
                    pause_game()
                if ((snake.xcor() == 100) and (snake.ycor() >= -140 and snake.ycor() <= 200)):
                    pause_game()
                if (snake.xcor() == -200 and (snake.ycor() >= -180 and snake.ycor() <= -80)) or (
                    snake.ycor() == -180 and (snake.xcor() >= -200 and snake.xcor() <= -100)):
                    pause_game()
            ## snake collision
            for food in old_fruit:
                if food.distance(snake) < 20:
                    pause_game()
        # va cham tuong
        if snake.xcor() > 280 or snake.xcor() < -300 or snake.ycor() > 240 or snake.ycor() < -240:  # va cham vao tuong
            pause_game()
        time.sleep(delay)
turtle.Terminator()






