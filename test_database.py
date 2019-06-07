import datetime as dt
import peewee as pw

db = pw.SqliteDatabase('people1.db')

class Person(pw.Model):
    name = pw.CharField()
    birthday = pw.DateField(formats=['%Y-%m-%d'])
    class Meta:
        database = db # This model uses the "people.db" database.

db.create_tables([Person])


Person.create(name='Bob0', birthday=dt.date(1940, 4, 13))
Person.create(name='Bob1', birthday=dt.date(1950, 5, 13))
Person.create(name='Bob2', birthday=dt.date(1960, 3, 13))
Person.create(name='Bob3', birthday=dt.date(1970, 3, 13))
Person.create(name='Bob4', birthday=dt.date(1980, 3, 13))
Person.create(name='Bob5', birthday=dt.date(1990, 3, 13))

base = Person.create(name="base", birthday=dt.date(1960, 3, 13))

for item in Person.select().where(Person.birthday > base.birthday):
    print (item.name , item.birthday)