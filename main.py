from flask import Flask
from flask import render_template
from flask import request
import sqlalchemy, random
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.sql import text

app = Flask (__name__)

@app.route('/', methods=['POST','GET'])
def home():
  if request.method == 'POST':
    if int(request.form['amount']) > 10:
      return render_template('index.html', error = 'Must be less than 10')
    else: 
      engine = create_engine('sqlite:///db.db', echo=True)
      conn = engine.connect()
      champs = conn.execute("SELECT * FROM champ order by random() limit " + request.form["amount"]).fetchall()
      return render_template('result.html', champs = champs)
  else:
    return render_template('index.html')

if __name__ == '__main__':
  app.run(debug=True, host='127.0.0.1')