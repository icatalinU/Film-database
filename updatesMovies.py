 
from connect import *

def update_movies():
    idField = input("Enter the filmID of the records to be updated: ")
    
    fieldName = input("Enter the field name to update (Title, YearReleased, Rating, Duration, Genre): ").title()

    # Ask the user to provide the data/value for the field they want to update
    fieldValue = input(f"Enter the new value for the {fieldName} field: ")

    # Add single quotes around the field value
    fieldValue = f"'{fieldValue}'"

    # Update a specific record
    update_query = f"UPDATE tblfilms SET {fieldName} = {fieldValue} WHERE filmID = {idField}"
    
    dbCursor.execute(update_query)
    dbCon.commit()
   
    print(f"Record {idField} updated in tblfilms table")
    
if __name__ == "__main__":
    update_movies()
    
    "UPDATE movies SET title  ="
