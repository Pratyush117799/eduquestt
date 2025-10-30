import sqlite3
from datetime import datetime, timedelta

DB = "scheduler.db"

# Create table if not exists
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

# Add new schedule
def add_schedule(title, date, event_type, reminder_before=1):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("INSERT INTO schedule (title, date, type, reminder_before) VALUES (?, ?, ?, ?)",
              (title, date, event_type, reminder_before))
    conn.commit()
    conn.close()
    print(f"✅ Added: {title} ({event_type}) on {date}")

# Show all upcoming events
def show_upcoming():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("SELECT * FROM schedule ORDER BY date ASC")
    rows = c.fetchall()
    print("\n📅 Upcoming Schedules:")
    for r in rows:
        print(f"• {r[1]} | {r[3].title()} | {r[2]}")
    conn.close()

# Check today’s reminders
def check_reminders():
    today = datetime.now().date()
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("SELECT title, date, type, reminder_before FROM schedule")
    for title, date_str, t, rb in c.fetchall():
        event_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        if event_date - timedelta(days=rb) == today:
            print(f"🔔 Reminder: {t.title()} '{title}' is due on {event_date}!")
    conn.close()

if __name__ == "__main__":
    init_db()

    print("📘 Assignment/Test Scheduler")
    print("1. Add schedule")
    print("2. View all")
    print("3. Check reminders")
    choice = input("Choose (1/2/3): ")

    if choice == "1":
        title = input("Enter title: ")
        date = input("Enter date (YYYY-MM-DD): ")
        event_type = input("Type (assignment/test): ").lower()
        reminder = int(input("Remind how many days before? "))
        add_schedule(title, date, event_type, reminder)

    elif choice == "2":
        show_upcoming()

    elif choice == "3":
        check_reminders()
