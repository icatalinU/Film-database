import sqlite3 as sql
from sqlite3 import connect, Cursor

dbCon = sql.connect("dfe2.db")


dbCursor = dbCon.cursor()