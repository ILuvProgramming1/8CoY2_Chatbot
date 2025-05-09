from turtle import Turtle

GRID_SIZE = 600
sub_divisions = 100
cell_size = GRID_SIZE / float(sub_divisions)

diddy = turtle.Turtle()
diddy = Turtle()

diddy.penup()
diddy.goto(-GRID_SIZE/2, GRID_SIZE/2)
diddy.pendown()

for _ in range(4):
    diddy.forward(GRID_SIZE)
    diddy.right(90)

for _ in range(2):
    for _ in range(1, sub_divisions):
        diddy.forward(cell_size)
        diddy.right(90)
        diddy.forward(GRID_SIZE)
        diddy.left(90)

        angle = -angle

    diddy.forward(cell_size)
    diddy.right(90)

screen.exitonclick()
