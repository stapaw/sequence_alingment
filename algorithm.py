import numpy as np
from tqdm import tqdm

GAP = "-"
MISMATCH = "*"
LOCAL = "local"
GLOBAL = "global"
LEFT = "l"
UP = "u"
UP_LEFT = "c"

pos_moves = {LEFT: (0, -1), UP: (-1, 0), UP_LEFT: (-1, -1)}


def add_gap(s):
    return "*" + s

# inicjalizacja macierzy wartości i kierunków
def init_arrays(s1, s2):
    s1 = add_gap(s1)
    s2 = add_gap(s2)
    return np.zeros([len(s2), len(s1)], dtype=int), np.empty([len(s2), len(s1)], dtype=str)

# obliczanie score wedle podanych parametrów obliczeń match, mismatch i gap
def score(x, y, scores):
    match, mismatch, gap = scores[0], scores[1], scores[2]
    if x == GAP or y == GAP:
        return gap
    elif x == y:
        return match
    else:
        return mismatch

def possible_moves(i, j):
    moves = []
    for key, move in pos_moves.items():
        if (i + move[0]) >= 0 and (j + move[1] >= 0):
            moves.append(key)
    return moves

# Centralna funkcja obliczająca wartości dla wszystkich możliwych ruchów w danym momencie
def calculate_values_for_moves(i, j, alignment_array, s1, s2, scores):
    values = []
    moves = possible_moves(i, j)
    for move in moves:
        value = alignment_array[i + pos_moves[move][0]][j + pos_moves[move][1]]
        if move == LEFT:
            value += score(s1[j + pos_moves[LEFT][1]], GAP, scores)
        if move == UP_LEFT:
            value += score(s1[j + pos_moves[UP_LEFT][1]], s2[i + pos_moves[UP_LEFT][0]], scores)
        if move == UP:
            value += score(s2[i + pos_moves[UP][0]], GAP, scores)
        values.append(value)
    return values, moves

# poprawka dla trybu local alignment
def calculate_best_move_value_local(i, j, alignment_array, s1, s2, score):
    best = calculate_best_move_value(i, j, alignment_array, s1, s2, score)
    if best[0] <= 0:
        best = (0, '')
    return best


def calculate_best_move_value(i, j, alignment_array, s1, s2, score):
    values, moves = calculate_values_for_moves(i, j, alignment_array, s1, s2, score)
    return max(values), moves[values.index(max(values))]

# główna funkcja wypełniająca tablicę wartości uliniowienia
def fill_alignment_tables(alignment_array, direction_array, s1, s2, score, type):
    for i in tqdm(range(0, alignment_array.shape[0])):
        for j in range(0, alignment_array.shape[1]):
            if i == 0 and j == 0:
                continue
            else:
                if type == LOCAL:
                    cells = calculate_best_move_value_local(i, j, alignment_array, s1, s2, score)
                else:
                    cells = calculate_best_move_value(i, j, alignment_array, s1, s2, score)
                alignment_array[i, j], direction_array[i, j] = cells
    return alignment_array, direction_array


def calculate_alignment(s1, s2, score, type=GLOBAL):
    alignment_array, direction_array = init_arrays(s1, s2)
    alignment_array, direction_array = fill_alignment_tables(alignment_array, direction_array, s1, s2, score, type)

    print(alignment_array)
    print(direction_array)

    return read_final_alignment(s1, s2, alignment_array, direction_array, type)


def read_final_alignment(s1, s2, alignment_array, direction_array, type):
    i, j = find_final_cell_indexes(alignment_array, type)
    final_score = alignment_array[i,j]
    return get_alignment(i, j, s1, s2, direction_array, final_score)


def find_final_cell_indexes(alignment_array, type):
    if type == LOCAL:
        return np.unravel_index(np.argmax(alignment_array, axis=None), alignment_array.shape)
    else:
        return alignment_array.shape[0] - 1, alignment_array.shape[1] - 1

# funkcja odczytująca uliniowienie z tablicy kierunków i zwracająca final score dla uliniowienia
def get_alignment(i, j, s1, s2, direction_array, final_score):
    line = ''
    while direction_array[i, j] != '':
        m = direction_array[i, j]
        i = i + pos_moves[m][0]
        j = j + pos_moves[m][1]
        if m != UP_LEFT:
            line = GAP + line
        else:
            if s2[i] == s1[j]:
                line = s1[j] + line
            else:
                line = MISMATCH + line
    return line, j, final_score



