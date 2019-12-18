import postgresql
import uuid

db = postgresql.open('pq://postgres:postgres@localhost:5432/contactdb')

def sel():
    with db.xact() as xact:
        return db.query("SELECT * FROM jc_contact")  # first_name


def inst(firstName, lastName, phone, email):
    with db.xact() as xact:
         db.query("INSERT INTO jc_contact (first_name, last_name, phone, email) VALUES ('%s', '%s', '%s', '%s')" % (firstName, lastName, phone, email))  # first_name

def dl(phone):
    with db.xact() as xact:
         db.query("DELETE FROM jc_contact WHERE phone = '%s'" % (phone))  # first_name

def upd(firstName, lastName, phone, email):
    with db.xact() as xact:
        db.query("UPDATE jc_contact SET phone = '%s', email = '%s' WHERE first_name = '%s' AND  last_name = '%s'" % (phone, email, firstName, lastName ))

print(uuid.uuid4())
#inst('Yan', 'Petrov', '+79775780983', 'yan@mail.ru')
#dl('+79775780983')
upd('Helga', 'Forte', '+79775780983', 'helga@mail.ru')

for user in sel():
    print(user)

