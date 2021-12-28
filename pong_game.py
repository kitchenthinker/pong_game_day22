import game_screen_and_graphic, game_ball, game_players, math, time, turtle, random

GAP_BETWEEN_CELLS = 20
TIME_SLEEP = 0.07
SNAKE_STEPS = 25
OPPOSITE_ANGLE = 180


def check_collisions_2_obj(f_obj: turtle.Turtle, s_obj: turtle.Turtle):
    x_collision = (math.fabs(f_obj.xcor() - s_obj.xcor()) * 2) < (f_obj.pensize() + s_obj.pensize())
    y_collision = (math.fabs(f_obj.ycor() - s_obj.ycor()) * 2) < (f_obj.pensize() + s_obj.pensize())
    return x_collision and y_collision


def check_collisions_2_obj_food(f_obj: turtle.Turtle, s_obj: turtle.Turtle):
    return f_obj.distance(s_obj) < s_obj.pensize()*2


class MainGame:

    def __init__(self):
        self.game_screen_and_graphic = game_screen_and_graphic.GameScreen()
        self.game_screen = self.game_screen_and_graphic.screen
        self.scoreboard = self.game_screen_and_graphic.scoreboard
        self.ball = game_ball.Ball()
        self.player = game_players.PlayerStick()
        self.opponent = game_players.PlayerStick(False)
        self.player.set_default_position(-game_screen_and_graphic.DEFAULT_SCREEN_WIDTH/2 + 20)
        self.opponent.set_default_position(-game_screen_and_graphic.DEFAULT_SCREEN_WIDTH/2 + 20)
        self.game_is_on = True
        self.game_screen.update()

    def start_game(self):
        self.game_screen.listen()
        self.game_screen.onkeypress(self.player.go_north, 'w')
        self.game_screen.onkeypress(self.player.go_south, 's')
        # self.game_screen.onkey(self.snake.turn_south, 's')
        # self.game_screen.onkey(self.snake.turn_west, 'a')
        # self.game_screen.onkey(self.snake.turn_east, 'd')
       # self.game_screen.screen.onkey(self.reset_game, 'c')

        while self.game_is_on:

            time.sleep(TIME_SLEEP)
            self.scoreboard.write_scoreboard()
            self.game_screen.update()
            self.check_collision_with_walls()
            self.check_collision_with_players()
            self.ball.move()
            self.opponent.ai_moving()
            # time.sleep(TIME_SLEEP)
            # self.write_game_score()
            # self.game_screen.update()
            # self.snake.move()
            # self.check_collisions_with_walls()
            # self.check_collisions_with_tail()
            # self.check_collision_with_apple()
            # self.check_game_is_over()

        self.game_screen.mainloop()

    def check_collision_with_walls(self):
        w_height = game_screen_and_graphic.DEFAULT_SCREEN_HEIGHT / 2
        w_width = game_screen_and_graphic.DEFAULT_SCREEN_WIDTH / 2
        wall_up = w_height - game_ball.DEFAULT_ALIGNMENT
        wall_down = -w_height + game_ball.DEFAULT_ALIGNMENT
        wall_left = -w_width + game_ball.DEFAULT_ALIGNMENT
        wall_right = w_width + game_ball.DEFAULT_ALIGNMENT
        heading = self.ball.heading()
        plain_angle = heading % 90 == 0
        x_cor = self.ball.xcor()
        y_cor = self.ball.ycor()

        if x_cor < wall_left:
            self.scoreboard.opponent_score.increase_score()
            self.ball.set_up_default_position()
        elif x_cor > wall_right:
            self.scoreboard.player_score.increase_score()
            self.ball.set_up_default_position()
        elif y_cor > wall_up or y_cor < wall_down:
            if plain_angle:
                if heading >= 180:
                    self.ball.setheading(heading - OPPOSITE_ANGLE)
                else:
                    self.ball.setheading(heading + OPPOSITE_ANGLE)
            else:
                self.ball.setheading(heading + 90)

    def check_collision_with_players(self):

        heading = self.ball.heading()
        plain_angle = heading % 90 == 0
        x_cor = self.ball.xcor()
        y_cor = self.ball.ycor()

        touch_player = False
        for segment in self.player.body:
            if self.ball.distance(segment) < 25:
                touch_player = True

        touch_opponent = False
        for segment in self.opponent.body:
            if self.ball.distance(segment) < 25:
                touch_opponent = True

        if touch_opponent or touch_player:
            if plain_angle:
                if heading >= 180:
                    self.ball.setheading(heading - OPPOSITE_ANGLE)
                else:
                    self.ball.setheading(heading + OPPOSITE_ANGLE)
            else:
                self.ball.setheading(heading + 90)
            # while x_cor < wall_left or x_cor > wall_right or y_cor > wall_up or y_cor < wall_down:
            #     self.ball.move(1)
            #     self.game_screen.update()
            #     x_cor = self.ball.xcor()
            #     y_cor = self.ball.ycor()
                # if heading >= 180:
          # w self.ball.move(10)    #     self.ball.setheading(heading - 90)
                # else:
                #     self.ball.setheading(heading + 90)

    # def check_collision_with_apple(self):
    #     if check_collisions_2_obj_food(self.snake.head, self.apple):
    #         self.apple.hide_up_apple()
    #         self.apple.set_is_eaten(True)
    #         self.apple.show_up_apple(self.game_screen.window_width(), self.game_screen.window_height())
    #         self.increase_game_point_counter()
    #         self.snake.add_segment_2_tail()

    # def check_game_is_over(self):
    #     if not self.snake.moving:
    #         self.game_is_on = False
    #         self.graphics.setposition(0, 0)
    #         self.graphics.write(f"GAME OVER:", False, align="center",
    #                             font=("Small fonts", 18, "bold"))
    #         return True
    #     return False

    # def reset_game(self):
    #     #self.snake.game_is_reset()
    #     self.game_screen.clear()
    #     self.__init__()
    #     self.start_game()
    #
    # def increase_game_point_counter(self):
    #     self.game_points += 1

    # def check_collisions_with_tail(self):
    #     snake = self.snake
    #     for segment in range(1, len(snake.body) - 1, 1):
    #         if check_collisions_2_obj(snake.head, snake.body[segment]):
    #             self.snake.set_moving_var(False)

    # def check_collisions_with_walls(self):
    #     x_cor = self.snake.head.xcor()
    #     y_cor = self.snake.head.ycor()
    #     w_width = self.game_screen.window_width()
    #     w_height = self.game_screen.window_height()
    #     ###
    #     left_wall = - (w_width/2)
    #     right_wall = (w_width/2)
    #     up_wall = (w_height/2)
    #     down_wall = - (w_height/2)
    #     ###
    #     if (x_cor >= right_wall) or (x_cor <= left_wall) or (y_cor >= up_wall) or (y_cor <= down_wall):
    #         self.snake.set_moving_var(False)