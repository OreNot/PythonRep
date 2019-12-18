def min(*a):
    m = a[0]
    for x in a:
        if m > x:
            m = x
    return m

print(min (5, 4, 2));

def my_range(start, stop, step = 1):
    res = []
    if step > 0:
        x = start
        while x < stop:
            res += [x]
            x += step
    elif step < 0:
        x = start
        while x > stop:
            res += [x]
            x += step
    return res

print(my_range(2,5));