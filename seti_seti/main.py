import random
from func import *
import itertools
from scipy.special import comb
import pandas as pd

b = np.array(
    ([[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 1], [1, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1], [1, 1, 1, 0], [0, 1, 1, 1],
      [1, 1, 1, 1], [1, 0, 1, 1], [1, 0, 0, 1]]))
b1 = np.array(([[1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1], [1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0], [0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0],
                [0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1]]))

g_matrix = gen_matrix(b, 11)
h_matrix1 = gen_matrix(b1, 4)

# check
print(g_matrix)
print("check!\n", h_matrix1.transpose())

# generating a code word
code_word = np.array(([random.choice([1, 0]) for k in range(11)]))
print('code word is: %s.' % code_word)

# encoding the code word
enc_word = multiplier(code_word, g_matrix)
print("encoded word", enc_word)

# generating an error
# a- amount of bits
# q- number of bit
# a = random.randint(0, 11)


list_C_n_i = list()
list_N_k = list()
list_C_k = list()

y1 = np.copy(enc_word)

for x in range(0, 16, 1):
    counter_nk = 0
    if x > 0:
        w = list(itertools.combinations(range(1, 16, 1), x))

        for y in w:
            q = np.array(y)  # bits with err
            for bit in q:
                y1[bit - 1] = 1 - y1[bit - 1]
            # print('spoiled encoded word:', y1)
            # finding spoiled bits
            spoiled_bit = multiplier(y1, h_matrix1.transpose())
            # print('bit with error:%s' % spoiled_bit)
            result, a = correction(spoiled_bit, h_matrix1, y1)
            # print("result:", result, " founded spoiled bit:", s_bit)

            nk = Nk(code_word, result, a)

            # print(nk)
            counter_nk += nk

            y1 = np.copy(enc_word)

    list_N_k.append(counter_nk)
    list_C_n_i.append(comb(15, x))
    list_C_k.append((counter_nk / comb(15, x)))

C_N_I = pd.Series(list_C_n_i,
                  index=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15'])
N_K = pd.Series(list_N_k, index=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15'])
C_K = pd.Series(list_C_k, index=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15'])
stats = pd.DataFrame({
    'CNI': C_N_I,
    'NK': N_K,
    'CK': C_K
})
print(stats)
print(enc_word)
