import numpy as np
GAP = "-"
MISMATCH= "*"
LEFT = "l"
UP = "u"
UP_LEFT = "c"
pos_moves = {LEFT:(0, -1), UP: (-1, 0), UP_LEFT:(-1, -1)}

def add_gap(s):
    return "*" + s

def init_arrays(s1, s2):
    s1 = add_gap(s1)
    s2 = add_gap(s2)
    return np.zeros( [len(s2), len(s1)], dtype=int), np.empty([len(s2), len(s1)], dtype=str)

def score(x,y, match = 1, mismatch = -1, gap = -2):
    if x == GAP or y == GAP:
        return gap
    elif x == y:
        return match
    else:
        return mismatch

def possible_moves(i, j):
    possibilities = [(0, -1, LEFT), (-1, -1, UP_LEFT), (-1, 0, UP)]
    moves = []
    for move in possibilities:
        if (i + move[0]) >= 0 and (j + move[1] >=0):
            moves.append(move)
    return moves


def calculate_best_move_value(i, j, alignment_array,s1="CAAGAC", s2="GAAC"):
    moves = possible_moves(i, j)
    scores = []
    for move in moves:
        if move[2] == LEFT:
            scores.append((score(s1[j + move[1]], GAP), LEFT))
        if move[2] == UP_LEFT:
            scores.append((score(s1[j + move[1]], s2[i + move[0]]), UP_LEFT))
        if move[2] == UP:
            scores.append((score(s2[i + move[0]], GAP), UP))

    values = [alignment_array[i + move[0]][j + move[1]] + scores[it][0] for it, move in enumerate(moves)]
    best = (max(values), moves[values.index(max(values))][2])
    return best


def make_move(i, j, m):
    return i + pos_moves[m][0], j + pos_moves[m][1]


def read_final_alignment(s1, s2, direction_array):
    i = len(s2)
    j = len(s1)
    line = result = ''
    while direction_array[i][j] != '':
        m = direction_array[i][j]
        i, j = make_move(i, j, m)
        result = result + m
        if m != UP_LEFT:
            line = GAP + line
        else:
            if s2[i] == s1[j]:
                line = s1[j] + line
            else:
                line = MISMATCH + line
    return line


def global_needleman_wunsch(s1, s2):
    alignment_array, direction_array = init_arrays(s1, s2)
    for i in range(0, alignment_array.shape[0]):
        for j in range(0, alignment_array.shape[1]):
            if i == 0 and j == 0:
                continue
            else:
                alignment_array[i][j], direction_array[i, j] = calculate_best_move_value(i, j, alignment_array, s1, s2)
    print(alignment_array)
    print(direction_array)

    return read_final_alignment(s1, s2, direction_array)


s1 = "CAAGAC"
s2 = "GAAC"

line = global_needleman_wunsch(s1, s2)
print(s1)
print(line)