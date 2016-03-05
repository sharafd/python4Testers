# -*- coding: utf-8 -*-

# Класс для работы с БД

from model import Group

class DbHelper:

  def __init__(self, db):
     self.database = db

  # Cписок групп
  def get_groups_list(self):
    list=[]
    cursor = self.database.connection.cursor()
    try:
      cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
      for row in cursor:
        (id, name, header, footer) = row
        list.append(Group(id=str(id), name=name, header=header, footer=footer))
    finally:
        cursor.close()
    return list
