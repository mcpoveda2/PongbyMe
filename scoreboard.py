from turtle import Turtle


ALIGNMENT = "center"
FONT = ('Arial', 40, 'normal')
COLOR = "white"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.derecho = 0
        self.izquierdo = 0
        self.penup()  # Levantar el bolígrafo para que la tortuga no dibuje mientras se mueve
        self.goto(0, 230)
        self.color(COLOR)
        self.hideturtle()
        self.crearScoreboard()

    def crearScoreboard(self):
        self.write(f"{self.izquierdo}        {self.derecho}", False, ALIGNMENT, font=FONT)

    def increseDerecha(self):
        self.derecho += 1
        self.clear()
        self.crearScoreboard()

    def increseIzquierda(self):
        self.izquierdo += 1
        self.clear()
        self.crearScoreboard()