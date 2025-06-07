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
        while(userRead != "5"):
            print("1. All Movies")
            print("2. Movie Ratings")
            print("3. Stars You Gave")
            print("4. Fun Facts about your Database")
            print("5. Quit")
        
            userRead = input("Your Choice: ")
            
            os.system('clear')

    # READ All movies 
            if userRead == "1":
                for row in cur.execute('SELECT id, name, rating, stars FROM movies'):
                    print(row)                

    # READ Ratings        
            elif userRead == "2":
                userReadRating = input("What Rating ('G' 'PG' 'PG-13'): ")
                for row in cur.execute('SELECT name, rating, stars FROM movies WHERE rating = ?', (userReadRating.upper(),)):
                    print(row)
    # READ Stars
            elif userRead == "3":
                userReadStars = input("How many Stars (1-5): ")
                for row in cur.execute('SELECT name, rating, stars FROM movies WHERE stars = ?', (userReadStars,)):
                    print(row)

    # AVERAGE Stars for Database
            elif userRead == "4":
                cur.execute("SELECT ROUND(AVG(stars), 1) FROM movies")
                userAverageStars = cur.fetchone()[0]
                print("Average is", userAverageStars, "Stars")
            # NUMBER of Ratings
                cur.execute("SELECT COUNT(*) FROM movies WHERE rating = ?", ("G",))
                ratingG = cur.fetchone()[0]
                cur.execute("SELECT COUNT(*) FROM movies WHERE rating = ?", ("PG",))
                ratingPG = cur.fetchone()[0]
                cur.execute("SELECT COUNT(*) FROM movies WHERE rating = ?", ("PG-13",))
                ratingPG13 = cur.fetchone()[0]
                print("The amount of G rated movies is:", ratingG)
                print("The amount of PG rated movies is:", ratingPG)
                print("The amount of PG-13 rated movies is:", ratingPG13)

    # QUIT to main menu
            elif userRead == "5":
                print("Going to the Main Menu")

    # INVALID input
            else:
                print("OOPS incorrect value please choose 1-5")


###############    WRITE to Database    #####################
    
    elif userInput == "2":
        print("ADD NEW MOVIE")
        userAddName = input("Name of Movie: ")
        userAddRating = input("Movie Rating (example: G, PG): ")
        userAddStars = input("Stars you give Movie 1-5: ")

        cur.execute("INSERT INTO movies (name, rating, stars) VALUES (?, ?, ?)", (userAddName.title(), userAddRating.upper(), userAddStars))
        con.commit()
        print("Movie Added")

###############    MODIFY Database    #######################
    
    elif userInput == "3":
        userMovieModify = ""
        print("1. Find by ID")
        print("2. Find by Title ")
        userModify = input("Your Choice: ")
        if userModify == "1":
            userMovieModify = input("What is the ID?: ")
            print("What do you want to edit?: ")
            print("1. Movie Name")
            print("2. Movie Rating")
            print("3. Movie Stars")
            userEdit = input("Your choice to Edit: ")
            if userEdit == "1":
                userNewName = input("Update Name: ")
                cur.execute("UPDATE movies SET name = ? WHERE id = ?", (userNewName, userMovieModify,))
            
            elif userEdit == "2":
                userNewRating = input("Update Rating: ")
                cur.execute("UPDATE movies SET rating = ? WHERE id = ?", (userNewRating, userMovieModify,))

            elif userEdit == "3":
                UserNewStars = input("Update Stars: ")
                cur.execute("UPDATE movies SET stars = ? WHERE id = ?", (UserNewStars, userMovieModify))

        else:
            userMovieModify = input("What is the Title of the movie? ")
            print("What do you want to edit?: ")
            print("1. Movie Name")
            print("2. Movie Rating")
            print("3. Movie Stars")
            userEdit = input("Your choice to Edit: ")
            if userEdit == "1":
                userNewName = input("Update Name: ")
                cur.execute("UPDATE movies SET name = ? WHERE name = ?", (userNewName, userMovieModify,))
            
            elif userEdit == "2":
                userNewRating = input("Update Rating: ")
                cur.execute("UPDATE movies SET rating = ? WHERE name = ?", (userNewRating, userMovieModify,))

            elif userEdit == "3":
                UserNewStars = input("Update Stars: ")
                cur.execute("UPDATE movies SET stars = ? WHERE name = ?", (UserNewStars, userMovieModify))

        con.commit()
        print("EXISTING MOVIE EDITED")

###########   DELETE Item from Database   ##################
    
    elif userInput == "4":
        print("1. Delete by ID")
        print("2. Delete by Title")
        print("3. Quit")
        userDelete = input("Your Choice: ")
        userDeleteMovie = ""

        if userDelete == "1":
            userDeleteMovie = input("ID: ")
            cur.execute("DELETE FROM movies WHERE id = ?", (userDeleteMovie,))
        elif userDelete == "2":
            userDeleteMovie = input("Title: ")
            cur.execute("DELETE FROM movies WHERE name = ?", (userDeleteMovie,))
        
        con.commit()

########################  QUIT  ###########################
    
    elif userInput == "5":
        print(userInput, "Goodbye :)")
    

# INCORRECT INPUT
    
    else:
        print("OOPS You didn't put in a number 1-5 please put in a number.")
    time.sleep(1)