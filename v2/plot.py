import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.widgets import Button
from skimage import exposure
from tkinter.filedialog import askopenfilename
import tkinter as tk
from type import *
from img import Img

class Plot:
    def __init__(self):
        self.img = Img()
        self.img.size_blue = self.img.blue.shape[0]
        self.img.size_red = self.img.red.shape[0]
        self.img.blue_result = self.img.blue
        self.img.red_result = self.img.red
        self.img.crop()

        self.correct_dimension = True
        
        self.fig, (self.ax1, self.ax2) = plt.subplots(1, 2, figsize=(15, 5))
        
        y, x, _ = self.ax2.hist(self.img.result.ravel(), bins=100)
        x = x[np.where(y == y.max())][0]
        self.img.result = np.subtract(self.img.result, x)

        self.ax1.imshow(self.img.result, cmap='bwr')
        
        self.ax_button_red = plt.axes([0.0, 0.95, 0.125, 0.05])
        self.ax_button_blue = plt.axes([0.0, 0.9, 0.125, 0.05])
        self.ax_button_reset = plt.axes([0.0, 0.85, 0.125, 0.05])
        self.ax_button_export = plt.axes([0.0, 0.8, 0.125, 0.05])

        self.button_red = Button(self.ax_button_red, 'Select Red Spectrum')
        self.button_blue = Button(self.ax_button_blue, 'Select Blue Spectrum')
        self.button_reset = Button(self.ax_button_reset, 'Reset Position')
        self.button_export = Button(self.ax_button_export, 'Export as CSV')

        self.x_label = self.fig.text(0.001, 0.75, f'Relative X offset: {self.img.x_movement}', fontsize=11)
        self.y_label = self.fig.text(0.001, 0.7, f'Relative Y offset: {self.img.y_movement}', fontsize=11)

        self.button_reset.on_clicked(self.reset)
        self.button_red.on_clicked(self.set_red)
        self.button_blue.on_clicked(self.set_blue)
        self.button_export.on_clicked(self.export)

        # self.cmap = mpl.cm.bwr
        # self.norm = mpl.colors.Normalize(vmin=-1, vmax=1)

        self.update_plot()

        self.fig.canvas.mpl_connect('key_press_event', self.on_press)

        plt.show()

    def export(self, event):
        filepath = askopenfilename()
        np.savetxt(filepath, self.img.result, delimiter='\t')

    def set_blue(self, event):
        filepath = askopenfilename()
        self.img.blue = np.genfromtxt(filepath, delimiter='\t', skip_header=0)
        self.img.size_blue = self.img.blue.shape[0]
        self.img.blue_result = self.img.blue
        self.update_plot()
    
    def set_red(self, event):
        filepath = askopenfilename()
        self.img.red = np.genfromtxt(filepath, delimiter='\t', skip_header=0)
        self.img.size_red = self.img.red.shape[0]
        self.img.red_result = self.img.red
        self.update_plot()

    def reset(self, event):
        self.img.x_movement = 0
        self.img.y_movement = 0

        self.x_label.set_text(f'Relative X offset: {self.img.x_movement}')
        self.y_label.set_text(f'Relative Y offset: {self.img.y_movement}')

        self.img.blue_result = self.img.blue
        self.img.red_result = self.img.red
        self.img.crop()
        self.update_plot()

    def on_press(self, event):
        if self.img.blue.shape != self.img.red.shape:
            self.correct_dimension = False
            self.update_plot()
            return

        self.correct_dimension = True

        if event.key == 'left':
            self.img.move(1, Type.X)
        elif event.key == 'right':
            self.img.move(-1, Type.X)
        elif event.key == 'up':
            self.img.move(1, Type.Y)
        elif event.key == 'down':
            self.img.move(-1, Type.Y)
        self.img.crop()

        self.x_label.set_text(f'Relative X offset: {self.img.x_movement}')
        self.y_label.set_text(f'Relative Y offset: {self.img.y_movement}')
        
        self.update_plot()

    def update_plot(self):
        self.ax1.clear()
        self.ax2.clear()

        if not self.correct_dimension:
            self.ax1.title.set_text('Error: Dimensions of spectra do not match')
        else:
            self.ax1.title.set_text('Spectra Overlay')

        y, x, _ = self.ax2.hist(self.img.result.ravel(), bins=100)
        x = x[np.where(y == y.max())][0]
        self.img.result = np.subtract(self.img.result, x)

        # Apply contrast stretching
        # self.img.result = exposure.rescale_intensity(self.img.result, in_range=(-1, 1), out_range=(0, 1))

        self.ax1.imshow(self.img.result, cmap='bwr')

        self.fig.canvas.draw()
        self.fig.canvas.flush_events()

if __name__ == '__main__':
    Plot()
