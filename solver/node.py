import copy
import BranchandBound as bb

#class untuk membuat struktur data node
class node:
    def __init__(self, parent, storedmat, blank_space, cost, level):
        self.parent = parent
        self.storedmat = storedmat
        self.blank_space = blank_space
        self.cost = cost
        self.level = level
    def __lt__(self, nextnode):
        return self.cost < nextnode.cost

#membuat node baru
def create_node(parent_matrix, blank_space, new_blank_space, level, parent_node, target):
    new_matrix = copy.deepcopy(parent_matrix)
    x1, y1, x2, y2 = blank_space[0], blank_space[1], new_blank_space[0], new_blank_space[1]
    new_matrix[x1][y1], new_matrix[x2][y2] = new_matrix[x2][y2], new_matrix[x1][y1]
    cost = bb.total_cost(new_matrix, target)
    new_node = node(parent_node, new_matrix, new_blank_space, cost, level)
    return new_node