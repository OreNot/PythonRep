ouf = open('text.txt', 'w')
ouf.write('!!!\n');
ouf.write(str(25));
ouf.close();

with open('text.txt', 'w') as ouf:
    ouf.write('CooCoo\n');
    ouf.write(str(25));