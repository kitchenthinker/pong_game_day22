import turtle
from turtle import Turtle, TurtleScreen, _Screen

PEN_SIZE = 10
DRAWING_SPEED = 0
DEFAULT_OBJECTS_COLOUR = 'white'
DEFAULT_SCREEN_COLOUR = 'black'
DEFAULT_ALIGNMENT = 50
DEFAULT_SCREEN_WIDTH = 600
DEFAULT_SCREEN_HEIGHT = 500
DEFAULT_SCOREBOARD_FONT = ("Small fonts", 30, "bold")


class GameScreen(Turtle):

    def __init__(self):
        super().__init__()
        self.screen = turtle.Screen()
        self.screen.title("PONG GAME")
        self.screen.setup(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)
        self.screen.bgcolor(DEFAULT_SCREEN_COLOUR)
        self.screen.tracer(0)
        self.screen.update()
        self.game_field = GameField(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)
        self.scoreboard = ScoreBoard(DEFAULT_SCREEN_WIDTH/2, DEFAULT_SCREEN_HEIGHT/2)
        self.scoreboard.write_scoreboard()

    def update_graphic(self):
        self.scoreboard.write_scoreboard()


class GameField(Turtle):

    def __init__(self, v_screen_width, v_screen_height):
        super().__init__()
        self.color(DEFAULT_OBJECTS_COLOUR)
        self.speed(DRAWING_SPEED)
        self.pensize(PEN_SIZE)
        self.hideturtle()
        self.setheading(270)
        self.screen_width = v_screen_width
        self.screen_height = v_screen_height
        self.draw_the_line()

    def draw_the_line(self):
        self.clear()
        abs_screen_height = self.screen_height/2
        self.penup()
        self.setposition(0, abs_screen_height)
        while self.ycor() > -abs_screen_height:
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)


class ScoreBoard:

    def __init__(self, v_screen_width, v_screen_height):
        self.player_score = ScoreObject(v_screen_width, v_screen_height, -100)
        self.opponent_score = ScoreObject(v_screen_width, v_screen_height, 100)
        self.screen_width = v_screen_width
        self.screen_height = v_screen_height

    def write_scoreboard(self):
        self.player_score.write_score()
        self.opponent_score.write_score()


class ScoreObject(Turtle):

    def __init__(self, v_screen_width, v_screen_height, offset):
        super().__init__()
        self.color(DEFAULT_OBJECTS_COLOUR)
        self.speed(DRAWING_SPEED)
        self.pensize(PEN_SIZE)
        self.penup()
        self.hideturtle()
        self.score = 0
        self.x_offset = offset
        self.screen_width = v_screen_width
        self.screen_height = v_screen_height

    def write_score(self):
        self.clear()
        self.setposition(self.x_offset, self.screen_height - DEFAULT_ALIGNMENT)
        self.write(f"{self.score}", False, align="center", font=DEFAULT_SCOREBOARD_FONT)

    def increase_score(self):
        self.score += 1
