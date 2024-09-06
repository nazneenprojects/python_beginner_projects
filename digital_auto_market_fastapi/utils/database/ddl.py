from database import engine
from models import Base

"""

models.Base.metadata.create_all(bind=engine)

The create_all() function reads all the model classes that inherit from Base and checks the database (through the engine) to see if the corresponding tables exist.
If a table doesn’t exist, it creates the table in the database with the appropriate columns, data types, and constraints as defined in the model.
If the table already exists, it does nothing (i.e., it doesn’t recreate or overwrite the table).

models.Base:

This refers to the base class for all your database models. Typically, Base is an instance of declarative_base() (from SQLAlchemy) that serves as a foundation for defining the ORM models (tables).
All your models (such as User, Item, etc.) inherit from this Base class.
metadata:

metadata is a collection of objects in SQLAlchemy that contain the definitions of all the tables and their associated attributes (columns, constraints, etc.) that are part of the models.
It stores information about the table structures, constraints, relationships, and more.
create_all():

This method generates the SQL CREATE TABLE statements to create the tables in the database based on the models you've defined. It will only create tables that don't already exist.
It does not drop or modify existing tables, so it’s safe to run even if some tables are already in place.
bind=engine:

engine refers to the connection engine that you’ve defined in your code, which connects to the specific database (PostgreSQL, MySQL, SQLite, etc.).
The bind=engine argument specifies which database (through the engine) to create the tables in.
"""

Base.metadata.create_all(bind=engine)
