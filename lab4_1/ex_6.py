import json
import sys
from ctxmngrs import timer
from decorators import print_result
from gens import field, gen_random
from iterators import Unique

path = "data_light_cp1251.json"

with open(path, encoding="ISO-8859-1") as f:
    data = json.load(f)


@print_result
def f1(arg):
    return sorted((x for x in Unique(list(field(arg, "job-name")), ignore_case=True)))


@print_result
def f2(arg):
    return list(filter(lambda x: x[0:11] == "Ïðîãðàììèñò", arg))


@print_result
def f3(arg):
    return list(map(lambda x: x + " с опытом Python", arg))


@print_result
def f4(arg):
    salaries = list(gen_random(100000, 200000, len(arg)))
    for name, salary in zip(arg, salaries):
        print(name, ", зарплата ", salary)


with timer():
    f4(f3(f2(f1(data))))
