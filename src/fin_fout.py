inf = open('file.txt', 'r');
s1 = inf.readline();
s2 = inf.readline();
inf.close();
print(s1);
print(s2);
#os.path.join('.', 'dir', 'file');

with open('text.txt') as inf:
    s1 = inf.readline().strip(); # ubrat \n
    s2 = inf.readline();

print(s1);
print(s2);