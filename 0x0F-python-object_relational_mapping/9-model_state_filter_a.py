#!/usr/bin/python3
"""
Lists all State objects that contain the letter a
from the database hbtn_0e_6_usa.
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


if __name__ == '__main__':
    engine = create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}',
        pool_pre_ping=True
    )

    Base.metadata.create_all(engine)

    session = Session(engine)

    states = session.query(State).filter(
        State.name.contains('a')
    ).order_by(State.id).all()

    for state in states:
        print(f'{state.id}: {state.name}')

    session.close()
