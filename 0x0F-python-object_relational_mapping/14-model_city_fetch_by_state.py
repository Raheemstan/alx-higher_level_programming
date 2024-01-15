#!/usr/bin/python3
"""prints all City objects
from the database hbtn_0e_14_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    # Database connection
    username, password, dbname = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{dbname}')
    Base.metadata.create_all(engine)

    # Session creation
    session = Session(engine)

    # Query and print City objects
    cities = session.query(City).join(State).order_by(City.id).all()
    for city in cities:
        print(f"{city.state.name}: ({city.id}) {city.name}")

    # Close the session
    session.close()
