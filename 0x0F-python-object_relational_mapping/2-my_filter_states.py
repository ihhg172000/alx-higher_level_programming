#!/usr/bin/python3
"""
Takes in an argument and
displays all values in the states table of hbtn_0e_0_usa
where name matches the argument.
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
        "SELECT * FROM states WHERE name = BINARY '{}' ORDER BY states.id"
        .format(argv[4])
    )

    query_rows = cursor.fetchall()

    for row in query_rows:
        print(row)

    cursor.close()
    db.close()
