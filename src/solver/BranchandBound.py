import node as nd
import prioQueue as prio
from numpy import append
import copy

n = 4
row_and_cols = [[1, 0], [0, -1], [-1, 0], [0, 1]]

#untuk mengecek apakah kolom dan baris valid
def isValid(row, cols):
    next_state = False
    if(row >= 0 and row < n) and (cols >= 0 and cols < n):
        next_state = True
    return next_state

#mencetak matriks yang diinginkan ke terminal
def show_path_matrix(dict):
    len_dict = len(dict)
    for i in range(1, len_dict):
        print("Langkah ke - " + str(i))
        for j in range(n):
            for k in range(n):
                print(dict[i][j][k], end = " ")
            print()
        print()
        

#fungsi utama untuk menyelesaikan puzzle
def solve_puzzle(initial, blank_space, target):
    pq = prio.prioQueue()
    cost = total_cost(initial, target)
    root = nd.node(None, initial,blank_space, cost, 0)
    pq.enqueue(root)

    while not pq.empty():
        min_node = pq.dequeue()
        if min_node.cost == 0:
            dict = []
            dict = createPath(min_node)
            return dict
        for i in range(n):
            new_tile_pos = [min_node.blank_space[0] + row_and_cols[i][0], min_node.blank_space[1] + row_and_cols[i][1]]
            if isValid(new_tile_pos[0], new_tile_pos[1]):
                child = nd.create_node(min_node.storedmat, min_node.blank_space, new_tile_pos, min_node.level + 1, min_node, target)
                pq.enqueue(child)
    return None

#menghitung total cost untuk mencapai ke kondisi ideal/target
def total_cost(currentMat, target):
    count = 0
    for i in range(n):
        for j in range(n):
            if ((currentMat[i][j]) and (currentMat[i][j] != target[i][j])):
                count += 1  
    return count

# menyimpan seluruh path mulai dari node itu sendiri hingga ke node parent secara rekursif
def createPath(root):
    dict = []
    if root == None:
        init =  [[ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ], [0, 0, 0, 0]]
        dict.append(init)
        return dict
    else:
        dict = createPath(root.parent)
        dict.append(root.storedmat)
        return dict