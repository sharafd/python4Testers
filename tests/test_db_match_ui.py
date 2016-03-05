# -*- coding: utf-8 -*-
from model import Group

def test_groups_list(app, db):
    # Запоминаем список групп
    ui_list = app.group.get_groups_list()
    #  Получаем список групп из БД
    db_list = map(app.group.format_groups_as_from_ui, db.database.get_groups_list())

    assert(sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max))