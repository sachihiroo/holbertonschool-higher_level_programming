#!/usr/bin/python3

"""
Function to list all states from
the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys

if __name__ == "__main__":

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
    )

    # Creating a cursor object using the cursor() method
    cursor = db.cursor()

    # Executing the SQL query to select all states from
    #  the database and sorting by 'id' in ascending order
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetching all the rows from the query result
    states = cursor.fetchall()

    # Displaying the results in the specified format
    for state in states:
        print(state)

    # Closing the cursor and database connection
    cursor.close()
    db.close()
