import sqlalchemy, random
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.sql import text

engine = create_engine('sqlite:///db.db', echo=True)

def main():
  champFile = open("Database.txt", "r")
  #itemFile = open("itemDatabase.txt")
  conn = engine.connect()
  metadata = MetaData()
  createTables(metadata, conn)
  names = champFile.readlines()

  for name in names:
    statement = text(
        "INSERT INTO champ (champName) " 
        "values ('" + name +  "')")
    conn.execute(statement)

  champs = conn.execute("SELECT * FROM champ").fetchall()
  print(result)


def createTables(metadata, conn):
  champ = Table('champ', metadata,
    Column('id', Integer, primary_key=True),
    Column('champName', String))

  #item = Table('itens', metadata,
    #Column('id', Integer, primary_key=True),
    #Column('item', String))

  metadata.create_all(engine)

main()