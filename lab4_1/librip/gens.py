import random


def field(items, *args):
    assert len(args) > 0
    for i in items:
        if len(args) <= 1 and i.get(args[0]) is not None:
            yield i[args[0]]
        elif len(args) <= 1 and i.get(args[0]) is None:
            continue
        else:
            yield {a: i.get(a) for a in args if i.get(a) is not None}


def gen_random(begin, end, num_count):
    for num in range(num_count):
        yield random.randint(begin, end)
