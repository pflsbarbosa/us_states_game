from turtle import Turtle
FONT = ("Arial", 25, "bold")
ALIGN = "center"
TEXT_COLOR = "blue"
STARTING_POSITION = (20, -200)


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color(TEXT_COLOR)
        self.penup()
        self.goto(STARTING_POSITION)
        self.fillcolor("white")
        self.write(f"Score:{self.score}/50", align=ALIGN, font=FONT)
        self.hideturtle()

    def update_score(self):
        self.write(f"Score:{self.score}/50", align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
