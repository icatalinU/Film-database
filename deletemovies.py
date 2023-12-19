from connect import *

#create subroutine

def delete_movies():
    
    #use primary key to delete a record
    
    idField = input("Enter a filmID of the record to be deleted: ")
    
    #DELETE from movies where filmID = 1/2/3/4/ ......
    
    dbCursor.execute(f"DELETE FROM movies wheere filmID ={idField}")
    dbCon.commit()
    
    print(f"Record{idField}Delete the movies table")
    
if __name__ == "__main__":
     delete_movies()
    