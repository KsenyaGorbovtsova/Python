import math

data = [4, -30, 100, -100, 123, 1, 0, -1, -4]


def mod_sort(elem):
    return math.fabs(elem)


data1 = sorted(data, key=mod_sort)
print(data1, data)
