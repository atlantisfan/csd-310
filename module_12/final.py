# Author: 	Justin Brehms
# Class: 	CSD 310 Module 12 - Final
# Project: 	WhatABook
# Date: 	03/05/2021

import mysql.connector
from mysql.connector import errorcode

#Credentials for accessing database
""" database configuration object """
loginInfo = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}
db = mysql.connector.connect(**loginInfo) # connect to database
cursor = db.cursor() 
#Define List Books Function
def listAllBooks(cursor):
    # Perform inner join
    cursor.execute("SELECT book_id, book_name, author, details from book")

    # get the results from the cursor object 
    books = cursor.fetchall()
    print("\t\tBooks In Stock")
    print("\t##############################################")
    
    # iterate out books 
    for book in books:
        print("  Book Name: {}\n  Author: {}\n  Details: {}\n".format(book[0], book[1], book[2]))
	

def listAllStores(cursor):
    '''Show all Stores in database'''
    cursor.execute("SELECT store_id, locale, hours FROM store")
    locations = cursor.fetchall()
    print("\t  Here are our Store Locations and Hours")
    print("\t##############################################")
    for location in locations:
        print("  Locale: {}\n".format(location[1]))

def mainMenu():
    #Load User Menu
    print("\t##############################################")
    print("\t  Hello! Welcome to the WhatABook Main Menu!\n\t")
    print("\t\t1. View Books\n\t\t2. View Store Locations"
        "\n\t\t3. My Account")
    print("\t\t or type '4' to quit\n")
    print("\t##############################################")
    try:
        menu_choice = int(input('\t\t Please enter a selection: '))
        return menu_choice
    except ValueError:
        print("\n  Invalid Selection. Exiting. \n")
        quit
def show_account_menu():
    """ display the users account menu """
    print("\t##############################################")
    print("\t\t Customer Area Menu")
    print("\t\t1. Wishlists\n\t\t2. Add Book"
        "\n\t\t3. Back to Main Menu")
    print("\t\t or type '4' to quit\n")
    print("\t##############################################")
    try:
        account_selection = int(input('\t\t Please enter a Selection: '))
        return account_selection
    except ValueError:
        print("\n  Invalid number, program terminated...\n")
def show_wishlist(cursor, user_id):
    """ query the database for a list of books added to the users wishlist """
    cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " + 
        "FROM wishlist " + 
        "INNER JOIN user ON wishlist.user_id = user.user_id " + 
        "INNER JOIN book ON wishlist.book_id = book.book_id " + 
        "WHERE user.user_id = {}".format(user_id))
    wishlist = cursor.fetchall()
    print("\t\tYour Wishlist")
    print("\t##############################################")

    for book in wishlist:
        print("        Book Name: {}\n        Author: {}\n".format(book[4], book[5]))
def listAllBooks_to_add(cursor, user_id):
    """ query the database for books not already in their wishlist """

    query = ("SELECT book_id, book_name, author, details "
        "FROM book "
        "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(user_id))

    print(query)
    cursor.execute(query)
    books_to_add = cursor.fetchall()
    print("\n        -- DISPLAYING AVAILABLE BOOKS --")
    for book in books_to_add:
        print("        Book Id: {}\n        Book Name: {}\n".format(book[0], book[1]))

def add_book_to_wishlist(cursor, user_id, _book_id):
    cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(user_id, _book_id))
    
def validate_user():
    """ validate the users ID """
    try:
        print("\t##############################################")
        user_id = int(input('Please type your user id'))
        if user_id < 0 or user_id > 3:
            print("\n  Invalid customer number, program terminated...\n")
            quit
        return user_id
    except ValueError:
        print("\n  Invalid Selection. Exiting. \n")
        quit
try:
    """ try/catch block for handling potential MySQL database errors """ 
    db = mysql.connector.connect(**loginInfo) # connect to database
    cursor = db.cursor() 
    user_selection = mainMenu()
    while user_selection != 4:
        if user_selection == 1:
            listAllBooks(cursor)
           
        # if the user selects option 2, call the listAllStores method and display the configured locations
        if user_selection == 2:
            listAllStores(cursor)

        # if item 3 is entered, call the validate_user method to validate the info 
        # if success, call the show_account_menu()
        if user_selection == 3:
            myuser_id = validate_user()
            account_option = show_account_menu()

		# while account option does not equal 3
            while account_option != 3:
                # if the use selects option 1, call the show_wishlist() method to show the current users 
                # configured wishlist items 
                if account_option == 1:
                    show_wishlist(cursor, myuser_id)
                # if the user selects option 2, call the listAllBooks_to_add function to show the user 
                # the books not currently configured in the users wishlist
                if account_option == 2:

                    # show the books not currently configured in the users wishlist
                    listAllBooks_to_add(cursor, myuser_id)

                    # get the entered book_id 
                    book_id = int(input("\n        Enter the id of the book you want to add: "))
                    
                    # add the selected book the users wishlist
                    add_book_to_wishlist(cursor, myuser_id, book_id)

                    db.commit() # commit the changes to the database 

                    print("\n        Book id: {} was added to your wishlist!".format(book_id))

                # if the selected option is less than 0 or greater than 3, display an invalid user selection 
                if account_option < 0 or account_option > 3:
                    print("\n      Invalid option, please retry...")

                # show the account menu 
                account_option = show_account_menu()
        
            # if the user selection is less than 0 or greater than 4, display an invalid user selection
            if user_selection < 0 or user_selection > 4:
                print("\n      Invalid option, please retry...")

        # show the main menu
        user_selection = mainMenu()

        print("\n\n  Program terminated...")

except mysql.connector.Error as err:
    """ handle errors """ 

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Username or password are invalid.")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist.")

    else:
        print(err)

finally:
    """ close the connection"""
    db.close()
