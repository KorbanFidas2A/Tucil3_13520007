def iomanage(string):
    with open(string) as textFile:
        lines = [line.split() for line in textFile]
    first_mat = [[0 for i in range(4)] for j in range(4)]
    for i in range (4):
        for j in range(4):
            first_mat[i][j] = int(lines[i][j])
    return first_mat

