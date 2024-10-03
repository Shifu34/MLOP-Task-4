from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Function to initialize the database using init.sql
def init_db():
    with sqlite3.connect('names.db') as conn:
        cursor = conn.cursor()
        with open('init.sql', 'r') as f:
            cursor.executescript(f.read())
        conn.commit()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        dob = request.form['dob']
        conn = sqlite3.connect('names.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (name, age, dob) VALUES (?, ?, ?)', (name, age, dob))
        conn.commit()
        conn.close()
        return redirect('/')
    return render_template('index.html')

if __name__ == '__main__':
    init_db()  # Initialize the database when the app starts
    app.run(debug=True)
