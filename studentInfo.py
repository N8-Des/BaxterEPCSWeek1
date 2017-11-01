import sqlalchemy, random
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.sql import text

engine = create_engine('sqlite://db.db:', echo=True)

def main():
  champFile = open("database.txt")
  itemFile = open("itemDatabase.txt")
  conn = engine.connect()
  metadata = MetaData()
  createTables(metadata, conn)
  statement = text("INSERT INTO champ (id, champName, item)" " values ()")
  conn.execute(statement)
  result = conn.execute(query).fetchall()
  print(result)



def createTables(metadata, conn):
  champ = Table('users', metadata,
    Column('id', Integer, primary_key=True),
    Column('item', String),
    Column('champName', String))

  item = Table('users', metadata,
    Column('id', Integer, primary_key=True),
    Column('item', String),
    Column('champName', String))

  metadata.create_all(engine)

main()