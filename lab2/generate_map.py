from PIL import Image
import math
import numpy as np

GRAY = (127, 127, 127, 255)
BLUE = (75, 174, 234, 255)
YELLOW = (246, 193, 67, 255)
WHITE = (255, 255, 255, 255)
RED = (255, 0, 0, 255)
BORDER = (0, 0, 0, 255)

def generate_map1():

    map=[]
    im = Image.open('pic1.png')
    pix = im.load()
    width = im.size[0]
    height = im.size[1]
 
    start_x = int(width /(17*2))
    x_step = int(width / 17)
    start_y = int(height / (14*2))
    y_step = int(height / 14)
    for i in range(14):
        row = []
        y = start_y + i * y_step
        for j in range(17):
            x = start_x + j * x_step
            print(pix[x,y])
            '''
            if pix[x, y] == GRAY:
                row.append('g')
            elif pix[x, y] == BLUE:
                row.append('b')
            elif pix[x, y] == YELLOW:
                row.append('y')
            elif pix[x, y] == WHITE:
                row.append('w')
            else:
                print("error")'''
        game_map.append(row)
    return game_map

def generate_map2():

    game_map = [[0] * 41]
    im = Image.open('map.png')
    pix = im.load()
    width = im.size[0]
    height = im.size[1]
    """
    取样点坐标
    """
    start_x = int(math.floor(width / 40)) - 10
    x_step = int(round(width / 40))
    start_y = int(math.floor(height / 20)) - 10
    y_step = int(round(height / 20))
    for i in range(20):
        row = [0]
        y = start_y + i * y_step
        for j in range(40):
            x = start_x + j * x_step
            if pix[x, y] == GRAY:
                row.append('g')
            elif pix[x, y] == BLUE:
                row.append('b')
            elif pix[x, y] == YELLOW:
                row.append('y')
            elif pix[x, y] == WHITE:
                row.append('w')
            else:
                print("error")
        game_map.append(row)
    return game_map