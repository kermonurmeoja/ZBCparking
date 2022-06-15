import os
import psycopg2
from flask import Flask, render_template, url_for, request

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='ZBCParking',
                            user=os.environ['kevinsutt35@gmail.com'],
                            password=os.environ['password'])
    return conn

@app.route("/", methods=['POST', 'GET'])
def index():

    return render_template('index.html')

app.run(debug=True)