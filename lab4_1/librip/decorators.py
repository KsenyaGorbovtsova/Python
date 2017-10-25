def print_result(a_func_to_decorate):
    def the_wrapper(*args, **kwargs):
        print(a_func_to_decorate.__name__)
        item = a_func_to_decorate(*args, **kwargs)
        if type(item) == list:
            for i in item:
                print(i)
        elif type(item) == dict:
            for key in item:
                print('%s = %s' % (key, item[key]))
        else:
            print(item)
        return item

    return the_wrapper


""""@print_result
def test_3():
    return {'a': 1, 'b': 2}
"""
