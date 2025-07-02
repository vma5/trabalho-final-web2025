from flask import Flask, render_template, request, redirect, url_for # type: ignore
import sqlite3

DB = 'meds.db'
app = Flask(__name__)

def get_db():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    meds = get_db().execute('SELECT * FROM meds').fetchall()
    return render_template('index.html', meds=meds)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        dosage = request.form['dosage']
        time = request.form['time']
        db = get_db()
        db.execute('INSERT INTO meds (name, dosage, time) VALUES (?, ?, ?)',
                   (name, dosage, time))
        db.commit()
        return redirect(url_for('index'))
    return render_template('add.html')

if __name__ == '__main__':
    app.run(debug=True)