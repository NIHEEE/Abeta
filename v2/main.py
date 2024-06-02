from img import *
import pygame
import matplotlib.pyplot as plt
from type import *

class Plot:

    def __init__(self):
        self.img = Img()
        self.img.set_blue()
        self.img.set_red()
        self.img.crop()

        fig,ax=plt.subplots()
        ax.imshow(self.img.result, cmap='bwr')
        fig.canvas.mpl_connect('key_press_event',self.on_press)
        plt.show()

    def on_press(self,event):
        if event.key == 'left':
            self.img.move(1, Type.X)
        elif event.key == 'right':
            self.img.move(-1, Type.X)
        elif event.key == 'up':
            self.img.move(1, Type.Y)
        elif event.key == 'down':
            self.img.move(-1, Type.Y)

        self.img.crop()
        plt.clf()
        plt.imshow(self.img.result, cmap='bwr')
        plt.draw()
        plt.pause(0.001)

if __name__ == '__main__':
    Plot()
    


