import sqlite3
from datetime import datetime, timedelta

# Connect to database
conn = sqlite3.connect("study.db")

# Create cursor
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS sessions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject TEXT,
    hours REAL,
    focus INTEGER,
    study_date TEXT
)
""")

conn.commit()

# Function to save study session
def add_session(subject, hours, focus, study_date):
    cursor.execute(
        "INSERT INTO sessions (subject, hours, focus, study_date) VALUES (?, ?, ?, ?)",
        (subject, hours, focus, study_date)
    )

    conn.commit()

    print("Session Saved!")



    # Function to get all sessions
def get_sessions():
    cursor.execute("SELECT * FROM sessions")
    return cursor.fetchall()

# Function to calculate total study hours
def get_total_hours():

    cursor.execute("SELECT SUM(hours) FROM sessions")

    result = cursor.fetchone()

    return result[0]


# Function to calculate average focus score
def get_average_focus():

    cursor.execute("SELECT AVG(focus) FROM sessions")

    result = cursor.fetchone()

    return round(result[0], 2)


# Function to get most studied subject
def get_top_subject():

    cursor.execute("""
        SELECT subject, SUM(hours) as total
        FROM sessions
        GROUP BY subject
        ORDER BY total DESC
        LIMIT 1
    """)

    return cursor.fetchone()

# Function to get subject-wise study hours
def get_subject_hours():

    cursor.execute("""
        SELECT subject, SUM(hours)
        FROM sessions
        GROUP BY subject
    """)

    return cursor.fetchall()

# Function to delete a session
def delete_session(session_id):

    cursor.execute(
        "DELETE FROM sessions WHERE id = ?",
        (session_id,)
    )

    conn.commit()

    print("Session Deleted!")


    from datetime import datetime, timedelta

# Function to calculate study streak
def get_streak():

    cursor.execute("""
        SELECT DISTINCT study_date
        FROM sessions
        ORDER BY study_date DESC
    """)

    dates = cursor.fetchall()

    if not dates:
        return 0

    date_list = [
        datetime.strptime(row[0], "%Y-%m-%d").date()
        for row in dates
    ]

    streak = 1

    for i in range(len(date_list) - 1):

        if date_list[i] - timedelta(days=1) == date_list[i + 1]:
            streak += 1
        else:
            break

    return streak
