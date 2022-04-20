import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg
import numpy as np
from PIL import ImageTk, Image
from matplotlib.patches import Rectangle
import time
from random import *

fensterbreite = 1440
fensterhoehe = 200
running = True
schritt = 0.01

street = np.zeros(2000, dtype=bool)

class Fahrzeug():
    liste = []
    def __init__(self, max_speed, pos):
        self.max_speed = max_speed
        self.speed = 1
        self.pos = pos
        street[pos] = True
        self.liste.append(self)
        self.checke_zustand()
        self.color = "green"
        self.zustand = 1

    def drive(self):

        if self.zustand == -1:
            if randint(1, 3) == 2:
                return self.pos

        self.checke_zustand()

        if self.zustand == 1:
            self.speed += 1
            self.color = "green"
        elif self.zustand == -1:
            self.speed = 0
            self.color = "red"
        else:
            self.color = "blue"

        street[self.pos] = False
        self.pos += self.speed

        if self.pos > 2000-1:
            self.pos = self.pos - 2000
        street[self.pos] = True

        return self.pos


    def checke_zustand(self):


        if True in street[self.pos+1:self.pos+1+self.max_speed]:
            self.zustand = -1

        else:
            if self.speed < self.max_speed:
                self.zustand = 1
            elif self.speed == self.max_speed:
                self.zustand = 0
            #else:
                #self.zustand = -1



def start_simulation():

    global street

    while running:
        fig = Figure(figsize=(11, 3))
        canvas = FigureCanvasAgg(fig)
        ax = fig.add_subplot()
        ax.set_axis_off()
        ax.set_xlim([0, 2000])
        ax.set_ylim([0, 100])

        for i in Fahrzeug.liste:
            pos = i.drive()

            aaa = street
            #aa = np.where(True, aaa)
            ax.add_patch(Rectangle((pos, 0), 10, 5, facecolor=i.color))

        canvas.draw()
        buf = canvas.buffer_rgba()
        X = np.asarray(buf)
        im = Image.fromarray(X)

        test = ImageTk.PhotoImage(im)
        label1 = tk.Label(image=test)
        label1.image = test
        label1.place(x=10, y=30)

        time.sleep(0.1)
        window.update()


    s = 8

if __name__ == '__main__':
    f1 = Fahrzeug(9, 600)
    f2 = Fahrzeug(8, 590)
    f3 = Fahrzeug(17, 573)
    f4 = Fahrzeug(19, 400)
    f5 = Fahrzeug(11, 380)
    f6 = Fahrzeug(13, 323)
    f7 = Fahrzeug(16, 250)
    f8 = Fahrzeug(20, 190)
    f9 = Fahrzeug(21, 180)
    f10 = Fahrzeug(9, 672)
    f11 = Fahrzeug(8, 720)
    f12 = Fahrzeug(17, 773)
    f13 = Fahrzeug(19, 800)
    f14 = Fahrzeug(11, 980)
    f15 = Fahrzeug(13, 1023)
    f16 = Fahrzeug(16, 1150)
    f17 = Fahrzeug(20, 1290)
    f18 = Fahrzeug(21, 1380)


    window = tk.Tk()
    window.title('Test')
    window.geometry("1080x400")

    simulate = tk.Button(window, text='start simulation', font='Calibri 12', command=start_simulation)
    simulate.place(x=50, y=310)

    window.mainloop()