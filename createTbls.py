
from connect import *  # Import the connect.py module

dbCursor.execute("""
    CREATE TABLE IF NOT EXISTS tblfilms (
        filmID INTEGER PRIMARY KEY,
        title TEXT,
        yearReleased INTEGER,
        rating TEXT,
        duration INTEGER,
        genre TEXT
    )
""")

# Commit the changes to the database
dbCon.commit()
