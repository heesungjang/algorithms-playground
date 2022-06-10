import turtle

tri_width = 300
colors = ["red", "blue", "green"]


def draw_triangle(color):
    board.pensize(10)
    board.begin_fill()
    board.color("black", color)
    board.forward(tri_width)  # draw base
    board.right(120)
    board.forward(tri_width)
    board.right(120)
    board.forward(tri_width)
    board.end_fill()


board = turtle.Turtle()

for color in colors:
    draw_triangle(color)
    board.penup()
    board.right(150)
    board.forward(55)
    board.setheading(0)
    tri_width -= 100

turtle.done()
