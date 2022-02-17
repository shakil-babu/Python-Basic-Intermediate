import turtle


class AjobTurtle(turtle.Turtle):
    """AjobTurtle is a class for new type of turtle"""

    def forward(self, pixel):
        super().backward(pixel)

    def backward(self, pixel):
        super().forward(pixel)

    def left(self, pixel):
        super().right(pixel)

    def right(self, pixel):
        super().left(pixel)


if __name__ == "__main__":
    turtle = AjobTurtle()
    turtle.left(30)
    turtle.forward(200)
    turtle.left(45)
    turtle.right(90)
