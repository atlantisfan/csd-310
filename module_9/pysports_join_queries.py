# Justin Brehms
# CSD 310 Databse design
# Module 9.2

import mysql.connector
# Login to mysql database using pysports_user
pysports = mysql.connector.connect (
    host="127.0.0.1",
    user="pysports_user",
    password="MySQL8IsGreat!",
    database="pysports"
    )

mycursor = pysports.cursor()

# perform inner join 
cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

# get results from cursor 
players = cursor.fetchall()

print("\n  -- DISPLAYING PLAYER RECORDS --")

# use for loop to iterate results 
for player in players:
    print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team Name: {}\n".format(player[0], player[1], player[2], player[3]))

input("\n\n  Press any key to continue... ")

#close connection to database
db.close()