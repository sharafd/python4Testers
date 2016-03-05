# -*- coding: utf-8 -*-

# Работа с БД
import mysql.connector
from helpers.dbHelper import DbHelper

class DbFixture:

  def __init__(self, host, database, user, password):
    self.host = host
    self.database = database
    self.user = user
    self.password =password
    self.connection = mysql.connector.connect(host = host, database=database,
                                              user = user, password = password)
    self.connection.autocommit = True
    self.database = DbHelper(self)

  def destroy(self):
    self.connection.close()
