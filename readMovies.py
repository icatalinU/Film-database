from connect import *

# create subroutine
def readMovies():
    dbCursor.execute("SELECT * FROM tblfilms")
    
    # fetch/get all the movies from the movie table
    allRecords = dbCursor.fetchall()
    
    # loop through all the movies from the table
    for eachRecord in allRecords:
        print(eachRecord)

if __name__ == "__main__":
    readMovies()
