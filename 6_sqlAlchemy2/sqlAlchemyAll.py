# Imports
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import Column, Integer, String, create_engine, func
# from sqlalchemy.orm import Session, declarative_base

#initialize with decrative base
# Base = declarative_base()

#Creating a class that works with a table (child component of the base)

#Create tables
def create_tables():
    #Create the engine
    # engine = create_engine('sqlite:///food.db')
    #Create the tables based on out parent base
    # Base.metadata.create_all(engine)
    pass
# Add a object
def add(meal):
    # Create the engine
    # engine = create_engine('sqlite:///food.db')
    # Create a session from that engine (Allowing us to create tables)
    # with Session(engine) as session:
        # Using .add we can now add an object
        # Make sure to commit
        pass

#Get all data
def select():
    pass

# Filter
def filter_by():
    pass

#Update
def update():
    #Updating formatting {attribute: new_attribute}
    
    pass

#With a delete we need to first query!
def delete():
    pass

if __name__ == '__main__':
    
    pass