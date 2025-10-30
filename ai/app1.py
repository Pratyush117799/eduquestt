from flask import Flask, render_template, request, redirect
import sqlite3
from datetime import datetime, timedelta

app = Flask(__name__)
DB = "scheduler.db"

def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS schedule (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    date TEXT NOT NULL,
                    type TEXT CHECK(type IN ('assignment','test')),
                    reminder_before INTEGER DEFAULT 1
                )''')
    conn.commit()
    conn.close()

@app.route("/")
def home():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("SELECT * FROM schedule ORDER BY date ASC")
    rows = c.fetchall()
    conn.close()

    today = datetime.now().date()
    reminders = []
    for r in rows:
        event_date = datetime.strptime(r[2], "%Y-%m-%d").date()
        if event_date - timedelta(days=r[4]) == today:
            reminders.append(r)
    return render_template("index.html", schedules=rows, reminders=reminders)

@app.route("/add", methods=["POST"])
def add():
    title = request.form["title"]
    date = request.form["date"]
    event_type = request.form["type"]
    reminder = int(request.form["reminder"])
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("INSERT INTO schedule (title, date, type, reminder_before) VALUES (?, ?, ?, ?)",
              (title, date, event_type, reminder))
    conn.commit()
    conn.close()
    return redirect("/")

@app.route("/delete/<int:id>")
def delete(id):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("DELETE FROM schedule WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect("/")

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
