students = ['Ivan', 'Masha', 'Sasha'];
students = students[::-1];
students[1] = 'Vitya';
for student in students:
    print('Hello', student, end='!\n');

print(len(students));