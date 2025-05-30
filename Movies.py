import sqlite3
import time
import os

con = sqlite3.connect("Movies.db")
cur = con.cursor()
userInput = ""

print("Welcome to the Movie Database What would You like to do")

# Loops through Main Menu until quit is chosen
while(userInput != "5"):
    
    print("1. Read Database")
    print("2. Add new Entry")
    print("3. Edit an Entry")
    print("4. Delete Existing Entry")
    print("5. Quit")

    userInput = input("What is your Choice?\n")

    os.system('clear')

###############    READ Database    #######################

    if userInput == "1":
        print("How would you like to See the Data?")
        userRead = ""
        while(userRead != "4"):
            print("1. All Movies")
            print("2. Movie Ratings")
            print("3. Stars You Gave")
            print("4. Main Menu")
        
            userRead = input("Your Choice: ")
            
            os.system('clear')

            if userRead == "1":
                for row in cur.execute('SELECT name, rating, stars FROM movies'):
                    print(row)
            
            elif userRead == "2":
                userReadRating = input("What Rating ('G' 'PG' 'PG-13'): ")
                for row in cur.execute('SELECT name, rating, stars FROM movies WHERE rating = ?', (userReadRating,)):
                    print(row)

###############    WRITE to Database    #####################
    
    elif userInput == "2":
        print("ADD NEW MOVIE")

###############    MODIFY Database    #######################
    
    elif userInput == "3":
        print("EDIT EXISTING MOVIE")

###########   DELETE Item from Database   ##################
    
    elif userInput == "4":
        print("DELETE MOVIE")

########################  QUIT  ###########################
    
    elif userInput == "5":
        print(userInput, "Goodbye :)")
    

# INCORRECT INPUT
    
    else:
        print("OOPS You didn't put in a number 1-5 please put in a number.")
    time.sleep(5)