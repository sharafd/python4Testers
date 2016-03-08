
import mysql.connector

from pony import orm

from fixtures import ORMFixture



# db = ORMFixture(host = "192.168.1.25", database = "addressbook",
 #         user = "root", password = "")


# l = db.get_contacts_list()

# for item in l:
  #  print(item)
from model import Group

connection = mysql.connector.connect(host = "192.168.1.25", database = "addressbook",
          user = "root", password = "")

try:
    cursor = connection.cursor()
    cursor.execute("select * from group_list")
    for row in cursor.fetchall():
        print(row)
finally:
    connection.close


db = ORMFixture(host = "192.168.1.25", database = "addressbook",
          user = "root", password = "")

l = db.get_groups_list()

print("--------------")

for item in l:
    print(item)

l = db.get_contacts_list()

for item in l:
    print(item)

print("--------------")
print("contact in groups")
print("--------------")


l = db.get_contacts_in_groups(Group(id="759"))

for item in l:
    print(item)