import numpy as np
from PIL import Image
import math


GRAY = (127, 127, 127, 255)
BLUE = (75, 174, 234, 255)
YELLOW = (246, 193, 67, 255)
WHITE = (255, 255, 255, 255)
RED = (255, 0, 0, 255)
BORDER = (0, 0, 0, 255)

def save_result2(game_map, path1,path2):
    
    pix = convert_array_to_pixel(game_map, path1,path2)
    array = np.asarray(pix, dtype=np.uint8)
    image = Image.fromarray(array, 'RGBA')
    image.save("result2.png")

def convert_array_to_pixel(arr, path1,path2):
    """
    将字符数组转化为像素
    :param arr:
    :param path:
    :return:
    """
    width = 20
    height = 20
    pixels = []
    for i in range(1, len(arr)):
        line = []
        for j in range(1, len(arr[i])):
            if arr[i][j] == 'g':
                line.append(GRAY)
            elif arr[i][j] == 'b':
                line.append(BLUE)
            elif arr[i][j] == 'y':
                line.append(YELLOW)
            elif arr[i][j] == 'w':
                line.append(WHITE)
        pixels.append(line)
    # 绘制路径
    for point in path1:
        x, y = point
        pixels[x - 1][y - 1] = RED
    for point in path2:
        x, y = point
        pixels[x - 1][y - 1] = RED
    # 处理分辨率，放大
    result = [[BORDER] * ((len(pixels[0])) * width + (len(pixels[0]) + 1))]
    for i in range(len(pixels)):
        line = [BORDER]
        for j in range(len(pixels[i])):
            line.extend([pixels[i][j]] * width)
            line.append(BORDER)
        for j in range(height):
            result.append(line)
        result.append([BORDER] * len(line))
    del pixels
    return result