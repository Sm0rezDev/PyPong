from tkinter import *
import time
import keyboard

WIDTH = 800
HEIGHT = 500
GAME_SPEED = 0.005
ballSpeedX = 0
ballSpeedY = 0
PADDLE_SPEED = 2
BG = "Black"

tk = Tk()

canvas = Canvas(tk, width=WIDTH, height=HEIGHT, bg=BG)

tk.title("PyPong")
tk.resizable(0,0)

canvas.pack()

paddleStartPos = (HEIGHT/2)-120

paddle1 = canvas.create_rectangle(25, paddleStartPos, 40, 120+paddleStartPos, fill="White", outline="White")
paddle2 = canvas.create_rectangle(WIDTH-40, paddleStartPos, WIDTH-25, 120+paddleStartPos, fill="White", outline="White")
ball = canvas.create_oval((WIDTH/2)-10, (HEIGHT/2)-10, (WIDTH/2)+10, (HEIGHT/2)+10, fill="White", outline="White")

isActive = True

while True:
    time.sleep(GAME_SPEED)
    
    if isActive == True:
        if keyboard.is_pressed('w') or keyboard.is_pressed('s'):
            isActive = False
            ballSpeedX = -2
        elif keyboard.is_pressed('up arrow') or keyboard.is_pressed('down arrow'):
            isActive = False
            ballSpeedX = 2

    paddle1coords = canvas.coords(paddle1)
    paddle2coords = canvas.coords(paddle2)

    # Paddle 1
    if paddle1coords[1] >= 0:
        if keyboard.is_pressed('w'):
            canvas.move(paddle1, 0, -PADDLE_SPEED)
    else:
        canvas.coords(paddle1, paddle1coords)

    if paddle1coords[3] <= HEIGHT:
        if keyboard.is_pressed('s'):
            canvas.move(paddle1, 0, PADDLE_SPEED)

    # Paddle 2
    if paddle2coords[1] >= 0:
        if keyboard.is_pressed('up arrow'):
            canvas.move(paddle2, 0, -PADDLE_SPEED)
    else:
        canvas.coords(paddle2, paddle2coords)

    if paddle2coords[3] <= HEIGHT:
        if keyboard.is_pressed('down arrow'):
            canvas.move(paddle2, 0, PADDLE_SPEED)

    p1bbox = canvas.bbox(paddle1)
    p2bbox = canvas.bbox(paddle2)
    ballBBox = canvas.bbox(ball)

    if ballBBox[0] < p1bbox[2] < ballBBox[2]:
        ballSpeedX = 2
    elif ballBBox[0] < p2bbox[2] < ballBBox[2]:
        ballSpeedX = -2

    canvas.move(ball, ballSpeedX, ballSpeedY)
    canvas.update()