from PIL import Image
from generate_map import *
from block import Block
from search import *
from generatepicture import *
from search2 import *
from generpicture2 import *


#generate_map1()
map2=generate_map2()
startPoint = Block(None, 'w', g=0, row=11, col=5)
endPoint = Block(None, 'y', g=0, row=1, col=36)
#path=search(map2,startPoint,endPoint)
path=search(map2,endPoint,startPoint)
save_result(map2, path)

path1,path2=search2(map2,startPoint,endPoint)
save_result2(map2, path1,path2)


