import turtle
import time
from random import randrange
BREAK_FLAG = False

# draw a window for the game
screen = turtle.Screen()
screen.title('Map')
screen.bgcolor('cyan')
screen.setup(650, 650, 720, 50)
screen.tracer(0)

# draw a game field border
border = turtle.Turtle()
border.hideturtle()
border.penup()
border.goto(-311, 311)
border.pendown()
border.goto(311, 311)
border.goto(311, -311)
border.goto(-311, -311)
border.goto(-311, 311)


# draw a snake of three segments and
# paint the head of the snake in black
snake = []
for i in range(3):
    snake_segment = turtle.Turtle()
    snake_segment.shape('square')
    snake_segment.penup()
    if i > 0:
        snake_segment.color('gray')
    snake.append(snake_segment)


food=turtle.Turtle()
food.shape('circle')
food.penup()
food.goto(randrange(-300, 300, 20), randrange(-300, 300, 20))

screen.onkeypress(lambda: snake[0].setheading(90), 'Up')
screen.onkeypress(lambda: snake[0].setheading(270), 'Down')
screen.onkeypress(lambda: snake[0].setheading(0), 'Right')
screen.onkeypress(lambda: snake[0].setheading(180), 'Left')
screen.listen()

while True:
    if snake[0].distance(food) < 10:
        food.goto(randrange(-300, 300, 20), randrange(-300, 300, 20))
        snake_segment = turtle.Turtle()
        snake_segment.shape('square')
        snake_segment.color('grey')
        snake_segment.penup()
        snake.append(snake_segment)
    for i in range(len(snake)-1, 0, -1):
        x=snake[i-1].xcor()
        y=snake[i-1].ycor()
        snake[i].goto(x,y)
    snake[0].forward(20)
    screen.update()

    x_cor = snake[0].xcor()
    y_cor = snake[0].ycor()
    if x_cor > 300 or x_cor < -300:
        screen.bgcolor('red')
        break
    if y_cor > 300 or y_cor < -300:
        screen.bgcolor('red')
        break
    for i in snake[1:]:
        i = i.position()
        if snake[0].distance(i)< 10:
            BREAK_FLAG = True
        if BREAK_FLAG:
            screen.bgcolor('red')
            break
    time.sleep(0.1)
screen.mainloop()