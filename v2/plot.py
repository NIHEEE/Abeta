from img import *
import matplotlib.pyplot as plt
from type import *
from matplotlib.widgets import Button
from tkinter import Tk

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
        
        # Add buttons for setting red and blue values
        self.ax_button_red = plt.axes([0.0, 0.95, 0.125, 0.05])
        self.ax_button_blue = plt.axes([0.0, 0.9, 0.125, 0.05])

        self.button_red = Button(self.ax_button_red, 'Select Red Spectrum')
        self.button_blue = Button(self.ax_button_blue, 'Select Blue Spectrum')

        

        self.button_red.on_clicked(self.set_red)
        self.button_blue.on_clicked(self.set_blue)

        self.img.crop()
        self.update_plot()

        # Connect the on_press function to the key_press_event
        self.fig.canvas.mpl_connect('key_press_event', self.on_press)

        plt.show()

    def set_blue(self, event):
        # self.img.blue = np.genfromtxt('sample/blue.csv', delimiter='\t', skip_header=0)
        # self.img.size_blue = self.img.blue.shape[0]
        # self.img.blue_result = self.img.blue
    
    def set_red(self, event):
        # filepath:str = self.get_filepath()
        # self.img.red = np.genfromtxt(filepath, delimiter='\t', skip_header=0)
        # self.img.size_red = self.img.red.shape[0]
        # self.img.red_result = self.img.red

    
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
        
        self.update_plot()

    def update_plot(self):
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
