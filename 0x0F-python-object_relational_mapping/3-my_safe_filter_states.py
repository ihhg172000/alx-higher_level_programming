#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.
"""
from sys import argv
import MySQLdb


if __name__ == '__main__':

    if ';' in argv[4]:
        quit()

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    cursor = db.cursor()

    cursor.execute(
        "SELECT * FROM states WHERE name = BINARY '{}' ORDER BY states.id"
        .format(argv[4])
    )

    query_rows = cursor.fetchall()

    for row in query_rows:
        print(row)

    cursor.close()
    db.close()
