import max7219.led as led

device = led.matrix()

def print_message(text):
    device.show_message(text)

def printScreen(array):
    for row in range(len(array)):
        for col in range(len(array[0])):
            device.pixel(row, col, array[row][col])

def invert(value):
    device.invert(value)

