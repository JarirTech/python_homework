import sqlite3
import pandas as pd

##Task 1: Create a New SQLite Database
#Write code to connect to a new SQLite database, ../db/magazines.db and to close the connection.
#Task 3: Populate Tables with Data

#Create functions, one for each of the tables, to add entries. Include code to handle exceptions as 
# needed, and to ensure that there is no duplication of information.

# add_publisher
def add_publisher(cursor, publisher_name):
    # Check if the publisher exist 
    cursor.execute(
        "SELECT publisher_id FROM Publishers WHERE publisher_name = ?",
        (publisher_name,)
    )

    result = cursor.fetchone()

    # if publisher exists, return its ID
    if result is not None:
        publisher_id = result[0]
        return publisher_id

    # If publisher does not exist, insert it
    cursor.execute("INSERT INTO Publishers (publisher_name) VALUES (?)",(publisher_name,))

    # return the new publisher ID
    new_publisher_id = cursor.lastrowid
    return new_publisher_id

#add_magazine

def add_magazine(cursor, magazine_name, publisher_id):
    # Check if the magazine already exists
    cursor.execute("SELECT magazine_id FROM Magazines WHERE magazine_name = ?",(magazine_name,) )

    result = cursor.fetchone()

    # If magazine exists, return its ID
    if result is not None:
        magazine_id = result[0]
        return magazine_id

    # Insert the magazine if it does not exist
    cursor.execute(
        "INSERT INTO Magazines (magazine_name, publisher_id) VALUES (?, ?)",(magazine_name, publisher_id) )

    # return the new magazine ID
    new_magazine_id = cursor.lastrowid
    return new_magazine_id

#add_subscriber
def add_subscriber(cursor, subscriber_name, subscriber_address):
    # check if the subscriber already exist
    cursor.execute( """ SELECT subscriber_id FROM Subscribers WHERE subscriber_name = ? AND subscriber_address = ?
        """, (subscriber_name, subscriber_address))

    result = cursor.fetchone()

    # If subscriber exist return the ID
    if result is not None:
        subscriber_id = result[0]
        return subscriber_id

    # Insert the subscriber if not found
    cursor.execute(
        "INSERT INTO Subscribers (subscriber_name, subscriber_address) VALUES (?, ?)", (subscriber_name, subscriber_address) )

    # Return the new subscriber ID
    new_subscriber_id = cursor.lastrowid
    return new_subscriber_id

#add_subscription

def add_subscription(cursor, subscriber_id, magazine_id, expiration_date):
    # Check if the subscription already exist
    cursor.execute(""" SELECT 1 FROM Subscribtion WHERE subscriber_id = ? AND magazine_id = ? """,
        (subscriber_id, magazine_id))

    result = cursor.fetchone()

    # If subscription exists, do nothing
    if result is not None:
        print("Subscription already exists.")
        return

    # Insert the new subscription
    cursor.execute( """ INSERT INTO Subscribtion (subscriber_id, magazine_id, expiration_date)
                         VALUES (?, ?, ?) """, (subscriber_id, magazine_id, expiration_date) )


try:
    with sqlite3.connect("../db/magazines.db") as conn:
        conn.execute("PRAGMA foreign_keys = 1")
        cursor = conn.cursor()

#Task 2: Define Database Structure
    #2.2Add SQL statements to sql_intro.py that create the following tables:
    #publishers table
        cursor.execute(""" CREATE TABLE IF NOT EXISTS Publishers
                        (publisher_id INTEGER PRIMARY KEY, publisher_name TEXT NOT NULL UNIQUE )  """)

    #magazines table
         
        cursor.execute(""" CREATE TABLE IF NOT EXISTS Magazines
                        (magazine_id  INTEGER PRIMARY KEY, publisher_id INTEGER NOT NULL,
                        magazine_name TEXT NOT NULL UNIQUE, 
                       FOREIGN KEY(publisher_id) REFERENCES Publishers(publisher_id) )  """)

    #subscribers table
        cursor.execute(""" CREATE TABLE IF NOT EXISTS Subscribers
                        (subscriber_id INTEGER PRIMARY KEY, subscriber_name TEXT NOT NULL, 
                       subscriber_address TEXT NOT NULL )   """)

    #subscriptions table(join table)

        cursor.execute(""" CREATE TABLE IF NOT EXISTS Subscribtion
                        (subscription_id INTEGER PRIMARY KEY, subscriber_id INTEGER NOT NULL,
                        magazine_id INTEGER NOT NULL, expiration_date TEXT NOT NULL, 
                       FOREIGN KEY(subscriber_id) REFERENCES Subscribers(subscriber_id),
                       FOREIGN KEY(magazine_id) REFERENCES Magazines(magazine_id))   """)
        conn.commit()


        print("Tables created successfully.")
    cursor = conn.cursor()

    # Publishers
    pub1 = add_publisher(cursor, "Tech Media")
    pub2 = add_publisher(cursor, "Science X")
    pub3 = add_publisher(cursor, "Global News")

    # Magazines
    mag1 = add_magazine(cursor, "Python Magazine", pub1)
    mag2 = add_magazine(cursor, "AI Magazine", pub1)
    mag3 = add_magazine(cursor, "Space Magazine", pub2)

    # Subscribers
    sub1 = add_subscriber(cursor, "Adam Jarir", "123 Main St")
    sub2 = add_subscriber(cursor, "Basma Ja", "45 casablanca")
    sub3 = add_subscriber(cursor, "Zara Jar", "99 casanegra")

    # Subscriptions
    add_subscription(cursor, sub1, mag1, "2026-01-01")
    add_subscription(cursor, sub1, mag2, "2025-06-30")
    add_subscription(cursor, sub2, mag3, "2025-12-31")
    add_subscription(cursor, sub3, mag1, "2026-03-15")

    conn.commit()
    print("Data inserted successfully.")

except sqlite3.Error as e:
    print("An error occurred while connecting to the database:", e)

#------------------------------------------------------------------------------------------   
#Task 4: Write SQL Queries
#1.Write a query to retrieve all information from the subscribers table.
cursor.execute("SELECT * FROM Subscribers")
for row in cursor.fetchall():
    print(row)

#2.Write a query to retrieve all magazines sorted by name.
cursor.execute("SELECT * FROM Magazines ORDER BY magazine_name")
for row in cursor.fetchall():
    print(row)

#3.Write a query to find magazines for a particular publisher, one of the publishers
#  you created. This requires a JOIN.
cursor.execute(""" SELECT m.magazine_name, p.publisher_name FROM Magazines m
    JOIN Publishers p ON m.publisher_id = p.publisher_id
    WHERE p.publisher_name = ? """, ("Tech Media",))

for row in cursor.fetchall():
    print(row)

#---------------------------------------------------------------------------------------
