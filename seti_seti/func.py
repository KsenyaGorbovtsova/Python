import numpy as np


# implemeting matrix
def gen_matrix(matrix, n):
    r_matrix = []
    for row in np.column_stack((matrix, np.eye(n))):
        r_matrix.append(list(map(int, row)))
    return np.array(r_matrix)


# 2mod
def multiplier(matrix1, matrix2):
    y = np.dot(matrix1, matrix2)
    for item in range(len(y)):
        if y[item] % 2 == 0:
            y[item] = 0
        else:
            y[item] = 1
    return y


# correction
def correction(r, matrix, spoiled_word):
    if np.array_equal([0, 0, 0, 0], r):
        # print('no error')
        counter = 0
        a = 'ne'
        return spoiled_word[4:], a
    else:
        a = 'e'
        counter = 1
        for counter, row in enumerate(matrix.transpose()):

            if np.array_equal(row, r):
                break
                # print('founded spoiled bit:', counter + 1)
        spoiled_word[counter] = 1 - spoiled_word[counter]
    return spoiled_word[4:], a


def Nk(c_word, res, a):
    nk = 0
    if np.array_equal(c_word, res) and a == 'e':
        nk += 1

    return nk
