import sys
import tkinter as tk

from img import *
from plot import *
from type import * 

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Image Analysis")

    img = Img()
    img.set_blue()
    img.set_red()
    img.crop()

    plot = Plot()

    root.mainloop()
    

