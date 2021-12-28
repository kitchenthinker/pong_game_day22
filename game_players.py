import turtle

GAP_BETWEEN_CELLS = 20
STEPS = 20


class PlayerStick:

    def __init__(self, v_player_stick=True):
        self.body = []
        self.create_body()
        self.head = self.body[0]
        self.head.setheading(90)
        self.xcor = self.head.xcor()
        self.ycor = self.head.ycor()
        self.is_player_stick = v_player_stick

    def check_walls(self):
        if self.head.ycor() > 280:
            for segment in self.body:
                segment.setheading(270)
        elif self.body[-1].ycor() < -280:
            for segment in self.body:
                segment.setheading(90)

    def ai_moving(self):
        self.check_walls()
        for segment in self.body:
            segment.forward(STEPS)

    def set_default_position(self, xcor):
        if not self.is_player_stick:
            xcor *= -1
        for segment in self.body:
            segment.goto(xcor, segment.ycor())

    def create_body(self):
        for _ in range(5):
            self.add_segment_2_tail()

    def move(self, head=True):
        if head:
            for segment in self.body:
                # new_x = self.body[segment - 1].xcor()
                # new_y = self.body[segment - 1].ycor()
                # self.body[segment].goto(new_x, new_y)
                segment.forward(STEPS)
            # self.head.forward(STEPS)
        else:
            for segment in reversed(self.body):
                segment.backward(STEPS)

    def add_segment(self, start_x=0, start_y=0, first_segment=False):
        segment = turtle.Turtle(shape="square")
        segment.penup()
        segment.width(10)
        if first_segment:
            segment.color("blue")
        else:
            segment.color("white")
        segment.setposition(start_x, start_y)
        segment.setheading(90)
        self.body.append(segment)

    def add_segment_2_tail(self, x_cor=0, y_cor=0):
        if self.body.__len__() == 0:
            self.add_segment(x_cor, y_cor, True)
        else:
            last_segment_x = self.body[-1].xcor()
            last_segment_y = self.body[-1].ycor()
            self.add_segment(last_segment_x, last_segment_y - GAP_BETWEEN_CELLS)

    def set_xy_cor(self):
        self.xcor = self.head.xcor()
        self.ycor = self.head.ycor()

    def go_north(self):
        # self.head.forward(STEPS)
        self.move(True)

    def go_south(self):
        # self.head.backward(STEPS)
        self.move(False)




