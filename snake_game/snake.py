from turtle import Turtle, Screen

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
POSITIONS = [(0, 0), (0, -20), (0, -40)]


class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_body()
        self.head = self.snake_body[0]

    def create_body(self):
        for position in POSITIONS:
            self.add_part(position)

    def add_part(self, position):
        snake_part = Turtle(shape="square")
        snake_part.color("white")
        snake_part.penup()
        snake_part.goto(position)
        self.snake_body.append(snake_part)

    def reset(self):
        for parts in self.snake_body:
            parts.goto(1000, 1000)
        self.snake_body.clear()
        self.create_body()
        self.head = self.snake_body[0]

    def extend_part(self):
        self.add_part(self.snake_body[-1].position())

    def move(self):

        for i in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[i - 1].xcor()
            new_y = self.snake_body[i - 1].ycor()
            self.snake_body[i].goto(new_x, new_y)
            self.snake_body[i].color("white")
        self.snake_body[0].forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
