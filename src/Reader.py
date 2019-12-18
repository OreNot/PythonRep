import codecs

'''
    rb = xlrd.open_workbook(fileName)
    sheet = rb.sheet_by_index(0)
    print(sheet.nrows)
    for rownum in range(1, sheet.nrows):
        row = sheet.row_values(rownum)
        cotactRow = row[0]

        cotactRow = cotactRow.replace('АП ', '')
        if cotactRow.__contains__(','):
            cotactRow = cotactRow[cotactRow.find(',') + 2 : cotactRow.__len__()]
        elif cotactRow.__contains__(' '):
            print(cotactRow.rfind(' '))
            if cotactRow[cotactRow.rfind(' ') + 1 : cotactRow.__len__()].isdigit() and cotactRow[cotactRow.rfind(' ') + 1 : cotactRow.__len__()].__len__() > 1 :
                cotactRow = cotactRow[cotactRow.rfind(' ') + 1: cotactRow.__len__()]

        if cotactRow.__contains__('('):
            cotactRow = cotactRow[0 : cotactRow.find('(')]






        if ((not ("a" in cotactRow.lower())) and (not ("o" in cotactRow.lower()))) and ((not ("q" in cotactRow.lower())) and (not ("g" in cotactRow.lower()))):
            contacts.append(cotactRow)
        elif ("a" in cotactRow.lower() or "o" in cotactRow.lower()) and ("а" in cotactRow.lower() or "о" in cotactRow.lower() or "в" in cotactRow.lower() or "н" in cotactRow.lower() or "к" in cotactRow.lower()):
            contacts.append(cotactRow[0 : cotactRow.rfind(' ')])
        else:
            contactsEng.append(cotactRow)
'''


contacts = []
contactsW = []

f = codecs.open( "F:\\XLS\\Основная адресная книга.txt", "r", "utf_8_sig" )

# -*- coding: utf-8 -*-
#f = open('F:\\XLS\\Основная адресная книга.txt')
for line in f:
    if line.__contains__('FN') and not line.__contains__('АП'):
        if line.__contains__('\\'):
            line = line[0 : line.find('\\')]
        if line.__contains__('@'):
            line = line[line.find('@') + 1 : line.__len__()]
        if line[0 : line.find(' ')].__contains__('Гринатом') or line[line.rfind('.') : line.__len__()].__contains__('11296'):
            continue
        line = line.replace('[', '').replace(']', '').replace('FN:','')
        contacts.append(line)

for contact in contacts:
        contactsW.append(contact.replace('\n', ''))

print(contactsW.__len__())

for contact in contactsW:
    print(contact)