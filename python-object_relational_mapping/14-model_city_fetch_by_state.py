#!/usr/bin/python3
"""Lists all cities of a given state from the database."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
from model_city import City


if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    state_name = sys.argv[4]

    engine = create_engine(
        f"mysql+mysqldb://{user}:{passwd}@localhost/{db}",
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == state_name).first()
    if state:
        for city in state.cities:
            print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
