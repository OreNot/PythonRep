dict, {}
d = {'a' : 239, 10 : 100}
print(d['a']);
print(d[10]);
print('a' in d);
d['a'] = 500;
print(d.get('a'));
del d[10];
print(d);
for key in d.keys():
    print(key, end='')

for value in d.values():
    print(value, end='')

for key, value in d.items():
    print(key, value, end=';')