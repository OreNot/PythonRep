def closest_mod_5(x):
    y = x
    while True:
     if y % 5 == 0 and y >= x:
        return y
        break
     else:
        y += 1

def printab(a, b = 10, *args):
    print(a)
    print(b)
    for i in args:
        print(i)

def printab_map(a, b, **args):
    print(a)
    print(b)
    for i in args:
        print(i, args[i])

print(closest_mod_5(6))