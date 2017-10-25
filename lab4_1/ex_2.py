
from gens import gen_random
from iterators import Unique

data0 = [1, 1 ,'a', 1, 1, 1, 2, 2, 2, 2, 2]
data1 = gen_random(1, 3, 10) data2= ['a', 'A', 'A', 'a', 'C', 'a', 'a', 'b', 'b', 'b', 'b', 'b']

d0 = Unique(data0)
for x in d0:
    print(x, )

d1 = Unique(list(data1))
for x in d1:
    print(x, )

d2 = Unique(data2, ignore_case=True)
for x in d2:
    print(x, )
