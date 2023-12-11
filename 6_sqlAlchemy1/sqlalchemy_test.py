# Let us start with the imports!
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine, func
from sqlalchemy.orm import Session, declarative_base

# We start with setting up a declrative_base()
Base = declarative_base()
# Now we create a class that is a child of that Base

    #Set up a __tablename__ as the tablename!

if __name__ == '__main__':
    #We can go ahead and create the db engine (creates the file as well)
    # engine = create_engine('sqlite:///hiking.db')

    # create schema (which will create the mountain schema) 

    # Now we can use an with statement
    # with Session(engine) as session:
    # Within this with we now do anything with the session! 
    '''
    Session.add()
    Session.query()
        .all()
        .orderby() ex: Table.name.desc()
        .limit()
        .filter() ex Table.name = "name"
        .update() ex {Table.name: newname}
    Session.delete()
    Session.commit()
    '''
    # To drop a table use TableClass.__table__.drop(engine)
    pass