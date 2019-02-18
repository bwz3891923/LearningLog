def vfunc(a,*b):
    print(type(b))
    for n in b:
        a += n

    return a

print(vfunc(1,2,3,4,5))
