
 

from connect import *

# create subroutine
def insert_movies():
    # filmID field is autoincrement (no data input is required)
    # ask user input for Title, yearreleased, duration, genre
    movieTitle = input("Please enter the movie title: ")
    yearReleased = input("Please add the movie released year: ")
    movieRating = input("Please add your rating (1-10): ")
    movieDuration = input("Please add the movie duration: ")
    movieGenre = input("Please add the movie genre: ")

    # add data into the respective fields in the movie table
    dbCursor.execute("INSERT INTO tblfilms (title, yearReleased, rating, duration, genre) VALUES (?, ?, ?, ?, ?)",
                     (movieTitle, yearReleased, movieRating, movieDuration, movieGenre))

    # commit the changes to the database
    dbCon.commit()

    print(f"{movieTitle} inserted in the tblfilms table")

if __name__ == "__main__":
    insert_movies()  # call the function
