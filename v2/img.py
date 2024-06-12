import pandas as pd
import seaborn as sns
from typing import Tuple
from matplotlib import *
import matplotlib.pyplot as plt
import numpy as np

from type import *
import tkinter as tk
from tkinter.filedialog import askopenfilename



class Img:
    def __init__(self):
        self.x_movement: int = 0
        self.y_movement: int = 0
        self.blue_path:str = 'sample/default_blue.csv'
        self.red_path:str = 'sample/default_red.csv'
        self.red: np.ndarray = np.genfromtxt(self.red_path, delimiter=',', skip_header=0)
        self.blue: np.ndarray = np.genfromtxt(self.blue_path, delimiter=',', skip_header=0)
        self.red_result: np.ndarray = None
        self.blue_result: np.ndarray = None
        self.result: np.ndarray = None
        self.size_blue: int = None
        self.size_red: int = None

    def set_blue_path(self) -> None:
        self.blue_path = askopenfilename()

    def move(self, amount: int, type: type) -> None:

        if type == Type.Y:
            self.y_movement += amount
        elif type == Type.X:
            self.x_movement += amount

        blue_copy = self.blue.copy()
        red_copy = self.red.copy()

        if self.x_movement > 0:
            for _ in range(self.x_movement):
                nan_column = np.full((self.blue.shape[0], 1), np.NaN)
                blue_copy = np.append(blue_copy, nan_column, axis=1)
                red_copy = np.insert(red_copy, 0, np.NaN , axis=1)
        elif self.x_movement < 0:
            for _ in range(abs(self.x_movement)):
                nan_column = np.full((self.red.shape[0], 1), np.NaN)
                red_copy = np.append(red_copy, nan_column, axis=1)
                blue_copy = np.insert(blue_copy, 0, np.NaN , axis=1)

        if self.y_movement > 0:
            for _ in range(self.y_movement):
                NaN_row = np.full((1, red_copy.shape[1]), np.NaN)
                blue_copy = np.append(blue_copy, NaN_row, axis=0)
                red_copy = np.insert(red_copy, 0, np.NaN , axis=0)
        elif self.y_movement < 0:
            for _ in range(abs(self.y_movement)):
                NaN_row = np.full((1, blue_copy.shape[1]), np.NaN)
                red_copy = np.append(red_copy, NaN_row, axis=0)
                blue_copy = np.insert(blue_copy, 0, np.NaN , axis=0)
        
        self.blue_result = blue_copy
        self.red_result = red_copy

    def set_blue(self) -> None:
        self.blue = np.genfromtxt('sample/default_blue.csv', delimiter=',', skip_header=0)
        self.size_blue = self.blue.shape[0]
        self.blue_result = self.blue

    def set_red(self) -> None:
        self.red = np.genfromtxt('sample/default_red.csv', delimiter=',', skip_header=0)
        self.size_red = self.red.shape[0]
        self.red_result = self.red

    def crop(self) -> None:
        self.result = np.subtract(self.red_result,self.blue_result)
        self.result = self.result[abs(self.y_movement):self.size_blue - abs(self.y_movement), abs(self.x_movement):self.size_blue - abs(self.x_movement)]

    
        

        
    






    


        
        
