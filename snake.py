from turtle import Turtle,Screen

class Snake:
    def __init__(self):
        self.squares = []
        self.create_snake()
        self.head = self.squares[0]
        # self.Left()
        # self.Right()
        # self.Up()
        # self.Down()
        #self.direction()

    # def Left(self):
    #     self = Turtle()
    #     self.setheading(180)
    #     self.forward(10)
    #
    #
    # def Right(self):
    #     self = Turtle()
    #     self.setheading(0)
    #     self.forward(10)
    #
    #
    # def Up(self):
    #     self = Turtle()
    #     self.setheading(90)
    #     self.forward(10)
    #
    #
    # def Down(self):
    #     self = Turtle()
    #     self.setheading(270)
    #     self.forward(10)

    def create_snake(self):
        for i in range(3):
            ali = Turtle()
            ali.shape("square")
            ali.color("green")
            ali.up()
            ali.goto(0 - 20 * i, 0)
            self.squares.append(ali)


    def move(self):
        for elemnt in range(len(self.squares) - 1, 0, -1):
            self.squares[elemnt].goto(self.squares[elemnt - 1].pos())

        self.squares[0].forward(20)


    def reset(self):
        for square in self.squares:
            square.goto(1000,1000)
        self.squares.clear()
        self.create_snake()
        self.head = self.squares[0]


    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:

            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:

            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:

            self.head.setheading(0)


    def increase_snake(self):
        ali = Turtle()
        ali.shape("square")
        ali.color("green")
        ali.up()
        ali.goto((self.squares[-1]).pos())
        self.squares.append(ali)

