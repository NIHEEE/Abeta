import linecache
import matplotlib
from matplotlib import pyplot
import numpy as np

# The horizontal (x) and vertical (y) movement of the pictures.
# Negative values are possible for movement into opposite direction.
# Red is moved down for positive values of y_movement.
# Red is moved to the right for positive values of x_movement.

x_movement = 0
y_movement = 0

# Insert input file directories below for red and blue respectively
file_red = 'C:/Users/Nihee/Code/ABeta/sample/red.txt'
file_blue = 'C:/Users/Nihee/Code/ABeta/sample/blue.txt'

# If the resulting textfile is not wanted, change receive_textfile to False
# The name of the resulting textfile is changeable, enter the wished name
# between the '', such as 'result1'

# Having two identical names for a textfile will overwrite the original textfile
receive_textfile = True
textfile_name = 'hello.txt'

# Do not edit below!
# ---------------------------------------------------------------

red, blue = [], []


# First for-loop, removes unnecessary whitespace
# Second for-loop creates array matching the dimension of the textfile
def file_formatting(txtfile_name, array):
    imported_array = linecache.getlines(txtfile_name)
    for line in imported_array:
        line = line.replace('\n', '')
        oneD = line.split('\t')
        array.append(oneD)

    for i in range(len(array)):
        for j in range(len(array[i])):
            array[i][j] = float(array[i][j])

    return array


# Movement of arrays horizontally where one of the arrays stays static
# Zeros are appended into the array at index 0, moving the rest of the array by the amount of zeros.
def moveX(arrayMoving, arrayStatic, pixelsAmount):
    for i in range(len(arrayStatic)):
        for c in range(pixelsAmount):
            arrayStatic[i].insert(0, 0)

    for a in range(len(arrayMoving)):
        for z in range(pixelsAmount):
            arrayMoving[a].append(0)


# Movement of arrays vertically where one of the arrays stays static
# Same concept as moveX
def moveY(arrayMoving, arrayStatic, pixelsAmount):
    for a in range(pixelsAmount):
        arrayMoving.append([])
        for i in range(len(arrayMoving[0])):
            arrayMoving[len(arrayMoving) - 1].append(0)

    for b in range(pixelsAmount):
        arrayStatic.insert(0, [])
        for i in range(len(arrayStatic[50])):
            arrayStatic[0].append(0)


# Converting the image to a .txt file that has the same format as input text files
def writetext(array, filename):
    with open(filename, 'w') as f:
        for i in range(len(array)):
            if i > 0:
                f.write('\n')
            for j in range(len(array[i])):
                f.write(str(array[i][j]))
                if j < len(array[i]) - 1:
                    f.write('\t')


# Calculating percentage of pixels that are blue + print it to terminal
def calculate_percentages(input_array):
    b = len(input_array)
    a = np.array(input_array)
    a[a > 0] = 0
    a = a[a != 0]
    print(f'Amount of pixels in total {((b - abs(x_movement)) * (b - abs(y_movement)))}')
    print(f'Amount of pixels > 0: {len(a)}')
    print(f'This corresponds to: {len(a) / ((b - abs(x_movement)) * (b - abs(y_movement))) * 100}%')


# Creating result image and displaying it.
def create_image(array):
    fig = pyplot.figure()
    colormap = matplotlib.colors.LinearSegmentedColormap.from_list('my_colormap', ['blue', 'white', 'red'], 256)
    img2 = pyplot.imshow(array, cmap=colormap, clim=(-0.1, 0.1))
    pyplot.colorbar(img2, cmap=colormap)
    pyplot.xlabel('Amount of Pixels Horizontally')
    pyplot.ylabel('Amount of Pixels Vertically')
    fig.show()
    return fig



# Create results array and calling functions to display graphical image.
def create_results(blue, red):
    result = np.subtract(np.array(red, dtype=float), np.array(blue, dtype=float), dtype=float)
    slicedresult = result[abs(y_movement):len(blue) - abs(y_movement), abs(x_movement):len(blue[0]) - abs(x_movement)]

    calculate_percentages(slicedresult)
    create_image(slicedresult)

    if receive_textfile == True :
        writetext(slicedresult, textfile_name)


# Executing functions
def main():

    file_formatting(f'{file_blue}', blue)
    file_formatting(f'{file_red}', red)

    # If statements below regulate positive and negative movement.
    if x_movement >= 0:
        moveX(blue, red, abs(x_movement))
    else:
        moveX(red, blue, abs(x_movement))

    if y_movement >= 0:
        moveY(blue, red, abs(y_movement))
    else:
        moveY(red, blue, abs(y_movement))

    create_results(blue, red)


# Runs program
main()
