import random
def mini_med(arr):
    i=arr[0]
    for j in arr:
        if j<i:
            i=j
    s=sum(t for t in arr) / len(arr)
    print ("min = %d sredn = %.2f" % (i, s))

a=[ float(random.randint(0,100)) for i in range(0,10)]
print a
print mini_med(a)
