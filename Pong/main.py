import turtle

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#pontos
ponto1 = 0
ponto2 = 0


#esquerda
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.color("green")
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
paddle_1.penup()
paddle_1.goto(-355, 0)


#direita
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.color("green")
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
paddle_2.penup()
paddle_2.goto(+355, 0)


#bola
bola = turtle.Turtle()
bola.speed(0)
bola.shape("square")
bola.color("green")
bola.penup()
bola.goto(0, 0)
bola.dx = 0.2
bola.dy = 0.2


#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)




#funcao
def paddle_1_up():
    y = paddle_1.ycor()
    y += 20
    paddle_1.sety(y)

def paddle_1_down():
    y = paddle_1.ycor()
    y -= 20
    paddle_1.sety(y)

def paddle_2_up():
    y = paddle_2.ycor()
    y += 20
    paddle_2.sety(y)

def paddle_2_down():
    y = paddle_2.ycor()
    y -= 20
    paddle_2.sety(y)


#binding teclado
wn.listen()
wn.onkeypress(paddle_1_up, "w")
wn.onkeypress(paddle_1_down, "s")
wn.onkeypress(paddle_2_up, "Up")
wn.onkeypress(paddle_2_down, "Down")

#loop
while True:
    wn.update()

    #movimento bola
    bola.setx(bola.xcor() + bola.dx)
    bola.sety(bola.ycor() + bola.dy)

    #borda
    if bola.ycor() > 290:
        bola.sety(290)
        bola.dy *= -1

    if bola.ycor() < -290:
        bola.sety(-290)
        bola.dy *= -1

    if bola.xcor() > 390:
        bola.goto(0, 0)
        bola.dx *= -1
        ponto1 += 1
        pen.clear()
        pen.write("Jogador 1: {} Jogador 2: {} ".format(ponto1, ponto2), align="center", font=("Courier", 24, "normal"))

    if bola.xcor() < -390:
        bola.goto(0, 0)
        bola.dx *= -1
        ponto2 += 1
        pen.clear()
        pen.write("Jogador 1: {} Jogador 2: {} ".format(ponto1, ponto2), align="center", font=("Courier", 24, "normal"))

#colisao paddle
    if (bola.xcor() > 340 and bola.xcor() < 350 and bola.ycor() < paddle_2.ycor() + 40 and bola.ycor() > paddle_2.ycor() -50):
        bola.setx(340)
        bola.dx *= -1

    if (bola.xcor() < -340 and bola.xcor() > -350 and bola.ycor() < paddle_1.ycor() + 40 and bola.ycor() > paddle_1.ycor() -50):
        bola.setx(-340)
        bola.dx *= -1