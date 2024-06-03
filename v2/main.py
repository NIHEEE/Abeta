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

        # Initialize the figure and axes as instance variables
        self.fig, (self.ax1, self.ax2) = plt.subplots(1, 2, figsize=(15, 5))
        
        y, x, _ = self.ax2.hist(self.img.result.ravel(), bins=100)
        
        x = x[np.where(y == y.max())][0]
        
        self.img.result = np.subtract(self.img.result, x)

        self.ax1.imshow(self.img.result, cmap='bwr')
        
        # Connect the on_press function to the key_press_event
        self.fig.canvas.mpl_connect('key_press_event', self.on_press)

        plt.show()

    def on_press(self, event):
        if event.key == 'left':
            self.img.move(1, Type.X)
        elif event.key == 'right':
            self.img.move(-1, Type.X)
        elif event.key == 'up':
            self.img.move(1, Type.Y)
        elif event.key == 'down':
            self.img.move(-1, Type.Y)
        self.img.crop()

        print("X: ", self.img.x_movement, "Y: ", self.img.y_movement)
        
        # Clear the axes
        self.ax1.clear()
        self.ax2.clear()

        # Redraw the updated image and histogram
        y, x, _ = self.ax2.hist(self.img.result.ravel(), bins=100)

        x = x[np.where(y == y.max())][0]
        

        self.img.result = np.subtract(self.img.result, x)
        
        self.ax1.imshow(self.img.result, cmap='bwr')
        # Update the canvas
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()

if __name__ == '__main__':
    Plot()
