from gens import *

goods = [
    {'title': 'Kover', 'price': 2000, 'color': 'green'},
    {'title': 'Coach for rest', 'price': 5300, 'color': 'black'},
    {'title': 'Stellag', 'price': 7000},
    {'title': 'veshalka dla odegda', 'price': 800, 'color': 'white'}
]

for i in field(goods, 'title', 'color'):
    print(i, ',', )
print('\n')
for i in gen_random(1, 3, 5):
    print(i, ',', )
