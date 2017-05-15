import max7219.led as led

device = led.matrix()
device.brightness(15)

# prints a message to the LED Display
def print_message(text):
    device.show_message(text)

# prints a 2D int array to the LED Display. Array must contain only 0's or 1's
def printScreen(array):
    for row in range(len(array)):
        for col in range(len(array[0])):
            device.pixel(row, col, array[row][col])

# inverts the value of a 2D array
def invert(value):
    device.invert(value)

