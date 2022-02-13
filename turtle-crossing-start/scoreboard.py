from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(-200,240)
        self.write(arg='Level: '+str(self.level),align='center',font=FONT)
        
    
    def update_scoreboard(self):
        self.clear()
        self.level += 1
        self.goto(-200,240)
        self.write(arg='Level: '+str(self.level),align='center',font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(arg='GAME OVER',align='center',font=FONT)