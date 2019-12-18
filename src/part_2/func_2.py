def h():
  print(12)

def f():
  g(h)

def g(a):
  a()

g(f)
x = print('1')
print(x is None)