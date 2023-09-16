#!/usr/bin/python3
"""
takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa.
"""
from sys import argv
import MySQLdb


if __name__ == '__main__':

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    cursor = db.cursor()

    cursor.execute(
        """
        SELECT cities.name
        FROM cities JOIN states ON cities.state_id = states.id
        WHERE states.name = BINARY %s
        ORDER BY cities.id
        """,
        (argv[4], )
    )

    query_rows = cursor.fetchall()
    cities = tuple(map(lambda value: value[0], query_rows))

    print(', '.join(cities))

    cursor.close()
    db.close()
