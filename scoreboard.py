from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.score = 0

        with open("score_file.txt") as file:
            self.high_score = int(file.read())
        self.up()

        self.goto(0, 350)
        self.write("Score ={}  High_Score = {} ".format(self.score, self.high_score), align="center",font=("Arial", 27, "normal"))
        self.hideturtle()

    def increase_score(self):
        self.clear()
        self.score += 1
        self.high_score += 1
        self.write("Score ={}  High_Score = {} ".format(self.score,self.high_score), align="center", font=("Arial", 27, "normal"))



    def reset(self):
        if self.score > self.high_score:



            self.high_score = self.score

            with open("score_file.txt","w") as file:
                file.write(f"{self.high_score}")



        self.score = 0
        self.clear()
        self.goto(0,350)
        self.write("Score ={}  High_Score = {} ".format(self.score,self.high_score), align="center", font=("Arial", 27, "normal"))




    def game_over(self):
        self.goto(0,0)
        self.up()
        self.write("GAME OVER ", align="center", font=("Arial", 30, "normal"))