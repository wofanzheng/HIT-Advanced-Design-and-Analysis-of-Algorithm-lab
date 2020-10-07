from queue import PriorityQueue
import math
from block import Block

# 定义8个方向
direction = [[0, 1],
             [0, -1],
             [1, 0],
             [-1, 0],
             [1, 1],
             [-1, -1],
             [-1, 1],
             [1, -1]]

def bound(row, col, max_row, max_col):
    if row < 1 or row > max_row:
        return True
    if col < 1 or col > max_col:
        return True
    return False

def get_cost(kind):

    cost = {"y": 4, "b": 2, "g": -1, "w": 0}
    return cost[kind]

def heuristic(point, target):
    dis = math.sqrt(math.pow(target.coordinate_row - point.coordinate_row,2) +
           math.pow(target.coordinate_col - point.coordinate_col,2))
    return point.g + dis

def find_path(target_area_block):

    print(target_area_block.g)
    # 用栈存储路径
    stack = [target_area_block.get_coordinate()]
    father_area_block = target_area_block.father
    while father_area_block is not None:
        stack.append(father_area_block.get_coordinate())
        father_area_block = father_area_block.father
    return stack
def search2(game_map, start_pos, end_pos):

    # 确定边界
    max_row = len(game_map) - 1
    max_col = len(game_map[0]) - 1
    # 创建open表, close表
    opened_table1 = PriorityQueue()
    closed_table1 = set()
    opened_table2 = PriorityQueue()
    closed_table2 = set()
    # 初始化open表
    opened_table1.put(start_pos)
    opened_table2.put(end_pos)
    while True:
        if not opened_table1.empty() and not opened_table2.empty():
            a=opened_table1.get()
            b=opened_table2.get()
            if a.coordinate_row==b.coordinate_row and a.coordinate_col==b.coordinate_col:
                return find_path(a),find_path(b)
            opened_table1.put(a)
            opened_table2.put(b)
            
        if not opened_table1.empty():
            current_area_block = opened_table1.get()
            for direct in direction:
                col_index = current_area_block.coordinate_col + direct[0]
                row_index = current_area_block.coordinate_row + direct[1]
                # 边界检测, 如果它不可通过或者已经在关闭列表中, 跳过
                if (row_index, col_index) in closed_table1 or bound(row_index, col_index, max_row=max_row, max_col=max_col):
                    continue
                if game_map[row_index][col_index] == 'g':
                    continue
                # 计算移动代价
                move_cost = 1
                if math.fabs(direct[0]) == 1 and math.fabs(direct[1]) == 1:
                    move_cost *= math.sqrt(2)
                # 计算地形代价
                land_cost = get_cost(game_map[row_index][col_index])
                # 创建block
                next_area = Block(father=current_area_block,
                                  kind=game_map[row_index][col_index],
                                  g=current_area_block.g + move_cost + land_cost,  # 地形代价 + 移动代价
                                  row=row_index,
                                  col=col_index)
                # 检查该点是否在open表中
                result = None
                tmp_queue = []
                while not opened_table1.empty():
                    tmp_block = opened_table1.get()
                    if tmp_block.get_coordinate() == next_area.get_coordinate():
                        result = tmp_block
                        break
                    tmp_queue.append(tmp_block)
                while len(tmp_queue) != 0:
                    opened_table1.put(tmp_queue.pop())
                opened_table1.task_done()
                # 检查该点是否在open表中, 如果不在则加入, 同时计算启发值 F = G + H
                next_area.f = heuristic(next_area, end_pos)
                if result is None:
                    opened_table1.put(next_area)
                else:
                    """
                    用G值为参考检查新的路径是否更好。更低的G值意味着更好的路径。
                    """
                    if next_area.g < result.g:
                        opened_table1.put(next_area)
                    else:
                        opened_table1.put(result)
            closed_table1.add(current_area_block.get_coordinate())
        
        if not opened_table2.empty():
            current_area_block = opened_table2.get()
            for direct in direction:
                col_index = current_area_block.coordinate_col + direct[0]
                row_index = current_area_block.coordinate_row + direct[1]
                # 边界检测, 如果它不可通过或者已经在关闭列表中, 跳过
                if (row_index, col_index) in closed_table2 or bound(row_index, col_index, max_row=max_row, max_col=max_col):
                    continue
                if game_map[row_index][col_index] == 'g':
                    continue
                # 计算移动代价
                move_cost = 1
                if math.fabs(direct[0]) == 1 and math.fabs(direct[1]) == 1:
                    move_cost *= math.sqrt(2)
                # 计算地形代价
                land_cost = get_cost(game_map[row_index][col_index])
                # 创建block
                next_area = Block(father=current_area_block,
                                  kind=game_map[row_index][col_index],
                                  g=current_area_block.g + move_cost + land_cost,  # 地形代价 + 移动代价
                                  row=row_index,
                                  col=col_index)
                # 检查该点是否在open表中
                result = None
                tmp_queue = []
                while not opened_table2.empty():
                    tmp_block = opened_table2.get()
                    if tmp_block.get_coordinate() == next_area.get_coordinate():
                        result = tmp_block
                        break
                    tmp_queue.append(tmp_block)
                while len(tmp_queue) != 0:
                    opened_table2.put(tmp_queue.pop())
                opened_table2.task_done()
                # 检查该点是否在open表中, 如果不在则加入, 同时计算启发值 F = G + H
                next_area.f = heuristic(next_area, start_pos)
                if result is None:
                    opened_table2.put(next_area)
                else:
                    """
                    用G值为参考检查新的路径是否更好。更低的G值意味着更好的路径。
                    """
                    if next_area.g < result.g:
                        opened_table2.put(next_area)
                    else:
                        opened_table2.put(result)
            closed_table2.add(current_area_block.get_coordinate())