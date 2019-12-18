genome = 'ASADF';
a = 0;
for i in genome:
    if i == 'A':
        a += 1;
    else:
        continue;

print(genome.count('A'));
print(genome.upper());
print(genome.lower());
print(genome.find('S'));
print(genome.replace('A', 'X'));
print(a);
print(genome[1]);
print(genome[1:4]);
print(genome[:4]);
print(genome[4:]);
print(genome[-4:]);
print(genome[1:-1]);
print(genome[1:-1:2]);
print(genome[::-1]);