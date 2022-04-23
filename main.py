import linecache
import matplotlib
from matplotlib import pyplot
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

red, blue, slicedresult, np1, np2 = [], [], [], [], []
x_movement, y_movement = 0, 0

def formatting(txtfile_name , array):
    imported_array = linecache.getlines(txtfile_name)
    for line in imported_array:
        line = line.replace('\n', '')
        oneD = line.split('\t')
        array.append(oneD)

    for i in range(len(array)):
        for j in range(len(array[i])):
            array[i][j] = float(array[i][j])

    return array

def moveX(arrayMoving, arrayStatic, pixelsAmount):
    for i in range(len(arrayStatic)):
        for c in range(pixelsAmount):
            arrayStatic[i].insert(0, 0)

    for a in range(len(arrayMoving)):
        for z in range(pixelsAmount):
            arrayMoving[a].append(0)

def moveY(arrayMoving, arrayStatic, pixelsAmount):
    for a in range(pixelsAmount):
        arrayMoving.append([])
        for i in range(len(arrayMoving[0])):
            arrayMoving[len(arrayMoving) - 1].append(0)

    for b in range(pixelsAmount):
        arrayStatic.insert(0, [])
        for i in range(len(arrayStatic[50])):
            arrayStatic[0].append(0)

def subtraction(array1, array2, resultArray):
    for i in range(len(array1)):
        for j in range(len(array1[i])):
            difference = array1[i][j] - array2[i][j]
            resultArray[i].append(difference)

def writetext(array, filename):
    with open(filename, 'w') as f:
        for i in range(len(array)):
            if i > 0:
                f.write('\n')
            for j in range(len(array[i])):
                f.write(str(array[i][j]))
                if j < len(array[i]) - 1:
                    f.write('\t')


def calculate_perxentages(input_array):
    b = len(input_array)
    a = np.array(input_array)
    a[a > 0] = 0
    a = a[a != 0]
    print(f'Amount of pixels > 0: {len(a)}')
    print(f'Amount of pixels in total {((b-x_movement)*(b-y_movement))}')
    print(f'{len(a)/((b-x_movement)*(b-y_movement))*100}%')





def create_results(base, subtract):
    result = np.subtract(np.array(subtract, dtype=float), np.array(base, dtype=float), dtype=float)
    slicedresult = result[y_movement:len(blue), x_movement:len(blue)]

    calculate_perxentages(slicedresult)

    fig = pyplot.figure()
    cmap2 = matplotlib.colors.LinearSegmentedColormap.from_list('my_colormap', ['blue', 'white', 'red'], 256)
    img2 = pyplot.imshow(slicedresult, cmap=cmap2, clim=(-0.1, 0.1))
    pyplot.colorbar(img2, cmap=cmap2)
    pyplot.xlabel('Amount of Pixels Horizontally')
    pyplot.ylabel('Amount of Pixels Vertically')
    fig.show()
    canvas = FigureCanvasTkAgg(fig)
    canvas.draw()
    canvas.get_tk_widget().place(height=720, x=600, y=0)

def main():
    formatting('blue.txt', blue)
    formatting('red.txt', red)

    moveX(blue, red, x_movement)
    moveY(blue, red, y_movement)

    create_results(blue,red)


main()










