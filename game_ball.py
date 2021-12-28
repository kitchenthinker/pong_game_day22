from turtle import Turtle
import random
DEFAULT_ALIGNMENT = 5


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("green")
        self.pensize(10)
        self.penup()
        self.is_out_off_boundaries = False
        self.setheading(random.randint(0, 359))
        self.set_up_default_position()

    def set_up_default_position(self, player_side=True):
        self.hideturtle()
        offset = -20
        if not player_side:
            offset *= -1
        self.setposition(offset, 0)
        self.showturtle()

    def set_out_off_boundaries(self, variable: bool):
        self.is_out_off_boundaries = variable

    def go_out_off_boundaries(self):
        return self.is_out_off_boundaries

    def move(self, speed=20):
        #self.setheading(direction)
        self.forward(speed)
