import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

main_screen = Screen()
main_screen.setup(width=800, height=600)
main_screen.bgcolor("black")
main_screen.title("Pong")
main_screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

main_screen.listen()
main_screen.onkey(r_paddle.go_up, "Up")
main_screen.onkey(r_paddle.go_down, "Down")
main_screen.onkey(l_paddle.go_up, "w")
main_screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    main_screen.update()
    ball.move()
    # detect  collision with top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # detect L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

main_screen.exitonclick()
