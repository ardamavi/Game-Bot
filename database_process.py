# Arda Mavi
import os
import sqlite3

def set_sql_connect(database_name):
    return sqlite3.connect(database_name)
def set_sql_cursor(database_connect):
    return database_connect.cursor()

def close_connect(vt):
    if vt:
        vt.commit()
        vt.close

def set_connect_and_cursor(path='Data/database.sqlite'):
    vt = set_sql_connect(path)
    db = set_sql_cursor(vt)
    return vt, db

def create_table(table_name, columns):
    vt, db = set_connect_and_cursor()
    db.execute("CREATE TABLE IF NOT EXISTS {0} ({1})".format(table_name, columns))
    close_connect(vt)

def get_data(sql_command):
    vt, db = set_connect_and_cursor()
    db.execute(sql_command)
    gelen_veri = db.fetchall()
    close_connect(vt)
    return gelen_veri

def add_data(table, adding):
    vt, db = set_connect_and_cursor()
    db.execute("INSERT INTO '{0}' VALUES ({1})".format(table, adding))
    close_connect(vt)
