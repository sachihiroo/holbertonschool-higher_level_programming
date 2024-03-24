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

    # Executing the SQL query to select all states
    # from the database and sorting by 'id' in ascending order
    name = sys.argv[4]
    cursor.execute(
        "SELECT cities.name\
                 FROM cities INNER JOIN states ON\
                 cities.state_id = states.id WHERE\
                states.name LIKE BINARY %s\
                  ORDER BY cities.id ASC",
        (name,),
    )

    all = cursor.fetchall()
    city_name = []
    for city in all:
        city_name.append(city[0])

    print(", ".join(city_name))
    # Closing the cursor and database connection
    cursor.close()
    db.close()
