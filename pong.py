from tkinter import *
import time
import keyboard

WIDTH = 800
HEIGHT = 500
PADDLE_SPEED = 2
BG = "Black"

tk = Tk()

canvas = Canvas(tk, width=WIDTH, height=HEIGHT, bg=BG)

tk.title("PyPong")
tk.resizable(0,0)

canvas.pack()

ball = canvas.create_oval((WIDTH/2)-10, (HEIGHT/2)-10, (WIDTH/2)+10, (HEIGHT/2)+10, fill="White")

paddle1Y = (HEIGHT/2)-60
paddle2Y = (HEIGHT/2)-60

paddle1 = canvas.create_rectangle(25, paddle1Y, 40, 120+paddle1Y, fill="White")
paddle2 = canvas.create_rectangle(WIDTH-40, paddle2Y, WIDTH-25, 120+paddle2Y, fill="White")

while True:
    time.sleep(0.005)

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

    canvas.update()