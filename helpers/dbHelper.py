# -*- coding: utf-8 -*-

# Класс для работы с БД

from model import Group, Contact


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
  
  # Cписок контактов
  def get_contacts_list(self):
    list=[]
    cursor = self.database.connection.cursor()
    try:
      cursor.execute("select id, address, firstname, middlename, lastname, nickname, bday, bmonth, byear," +
        " aday, amonth, ayear, photo, title, company, home, mobile, work, fax, email2, email3, homepage," +
        " address2, phone2, notes, domain_id, email from addressbook where deprecated = '0000-00-00 00:00:00'")
      for row in cursor:
        (id,
        address,
        firstname,
        middlename,
        lastname,
        nickname,
        bday,
        bmonth,
        byear,
        aday,
        amonth,
        ayear,
        photo,
        title,
        company,
        home,
        mobile,
        work,
        fax,
        email2,
        email3,
        homepage,
        address2,
        phone2,
        notes,
        domain_id,
        email) = row
        list.append(Contact(
        id=str(id),
        address = address,
        firstname= firstname,
        middlename = middlename,
        lastname = lastname,
        nickname = nickname,
        bday = bday,
        bmonth = bmonth,
        byear= byear,
        aday = aday,
        amonth = amonth,
        ayear = ayear,
        photo = photo,
        title = title,
        company = company,
        home = home,
        mobile = mobile,
        work = work,
        fax = fax,
        email2 = email2,
        email3 = email3,
        homepage = homepage,
        address2 = address2,
        phone2 = phone2,
        notes = notes,
        group= domain_id,
        email = email,
        all_phones_from_home_page = None,
        all_emails_from_home_page = None
      ))
    finally:
      cursor.close()
    return list
