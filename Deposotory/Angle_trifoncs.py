import math
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import keyboard

# I know I should probably just use either numpy or math, but it's way too late to change

window = tk.Tk()
window.title("TRIGONOMETRIC FUNCTIONS")
window.geometry("900x600")

canvas = tk.Canvas(window, width=1000, height=1000, bg="white")
canvas.pack(side="left")

arc_center = (300, 300)
arc_radius = 250

arc = canvas.create_arc((50, 50), (550, 550), extent=359.9, start=0, width=2)
line = canvas.create_line(arc_center[0], arc_center[1], 550, 50, fill="blue", width=2)
ninety_line = canvas.create_line(arc_center[0], arc_center[1], arc_center[0], 50, width=2)
pi_line = canvas.create_line(arc_center[0], arc_center[1], 50, arc_center[1], width=2)
third_line = canvas.create_line(arc_center[0], arc_center[1], arc_center[0], 550, width=2)

rad_text = canvas.create_text(700, 50, text="Lorem", fill="black", font=10)
sin_text = canvas.create_text(700, 130, text="Ipsum", fill="black", font=10)
cos_text = canvas.create_text(700, 220, text="Dolor", fill="black", font=10)
tan_text = canvas.create_text(700, 300, text="Sit", fill="black", font=10)
cot_text = canvas.create_text(700, 380, text="Amet", fill="black", font=10)
sec_text = canvas.create_text(700, 460, text="Consectatur", fill="black", font=10)
cosec_text = canvas.create_text(700, 540, text="Adipiscing", fill="black", font=10)


def main(event):
    # noinspection PyGlobalUndefined
    global angle
    line_x = event.x - arc_center[0]
    line_y = event.y - arc_center[1]
    angle_rad = math.atan2(line_y, line_x)
    angle = angle_rad * 180/math.pi * -1
    if angle < 0:
        angle += 360
        if angle == 360:
            angle = 0

    line_end_x = arc_center[0] + arc_radius * math.cos(angle_rad)
    line_end_y = arc_center[1] + arc_radius * math.sin(angle_rad)

    canvas.coords(line, arc_center[0], arc_center[1], line_end_x, line_end_y)

    try:
        sin = math.sin(angle_rad)
        sin = -1 * sin
        if angle == 0 or angle == 90 or angle == 180 or angle == 270 or angle == 360:
            sin = round(sin)
    except:
        sin = "undefined"
    try:
        cos = math.cos(angle_rad)
        if angle == 0 or angle == 90 or angle == 180 or angle == 270 or angle == 360:
            cos = round(cos)
    except:
        cos = "undefined"
    try:
        tan = sin/cos
        if angle == 90 or angle == 270:
            tan = "undefined"
        elif angle == 0 or angle == 180:
            tan = 0
    except:
        tan = "undefined"
    try:
        cot = cos/sin
        if angle == 0 or angle == 180:
            cot = "undefined"
        if angle == 90 or angle == 270:
            cot = 0
    except:
        cot = "undefined"
    try:
        sec = 1/cos
        if angle == 90 or angle == 270:
            sec = "undefined"
    except:
        sec = "undefined"
    try:
        cosec = 1/sin
        if angle == 0 or angle == 180:
            cosec = "undefined"
    except:
        cosec = "undefined"

# math.tan()/.cot()/.sec()/.cosec() can go ..... themselves

    def update_text():
        canvas.itemconfig(rad_text, text=f"Angle: {angle}°")
        canvas.itemconfig(sin_text, text=f"Sin: {sin}")
        canvas.itemconfig(cos_text, text=f"Cos: {cos}")
        canvas.itemconfig(tan_text, text=f"Tan: {tan}")
        canvas.itemconfig(cot_text, text=f"Cot: {cot}")
        canvas.itemconfig(sec_text, text=f"Sec: {sec}")
        canvas.itemconfig(cosec_text, text=f"Cosec: {cosec}")

    update_text()

    def graph():
        Fs = 360
        f = 5
        sample = 360
        phi = angle * np.pi/180
        x_sin = np.arange(sample)
        y_sin = np.sin(2 * np.pi * f * x_sin / Fs + phi)
        plt.plot(x_sin, y_sin, color="blue")

        plt.show()

    for i in range(10):  # If I put this and the graph() outside of the main loop, this for loop only goes off once. I cannot fix it, I'm way too tired its 3am. If you press "g" while moving your mouse, it works. Goodbye thank you for reading. I hope you had a good day. This thing has beaten me. Maybe one day I'll return here. Maybe...
        if keyboard.is_pressed("g"):
            graph()


window.bind("<Motion>", main)

window.mainloop()
