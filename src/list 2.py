students = ['Ivan', 'Masha', 'Sasha']
students += ['Olga']
students.append('Vitya');
students.insert(1, 'Nick');
students += ['Igor'];
id = students.index('Sasha');
students.remove('Igor');
ordered_stud = sorted(students);
students.sort();
name = min(students);
name1 = max(students);
rev_stud = students.reverse();
rev2 = reversed(students);

#for student in students:
print(students);


if 'Nick' in students:
    print('yes');
if 'Ann' not in students:
    print('no');
print(len(students));

