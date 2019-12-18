s = set();
basket = {'apple', 'orange', 'pear'};
s.add('apple');
s.remove('apple');
print(len(basket));

s.discard('apple');
s.clear();
print(basket);

print('orange' in basket);
for x in basket:
    print(x);