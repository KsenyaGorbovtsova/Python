def rotate(str):
    new_str=''
    for count, letter in enumerate(str):
        new_str=new_str+str[len(str)-1-count]
    print new_str

str='Hello, world!'
rotate(str)