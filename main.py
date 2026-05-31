import tkinter as tk
import matplotlib.pyplot as plt
from tkinter import messagebox
from database import (
    add_session,
    get_sessions,
    get_total_hours,
    get_average_focus,
    get_top_subject,
    get_subject_hours,
    delete_session,
    get_streak
)

# Function when button clicked
def save_data():
    subject = subject_entry.get()
    hours = hours_entry.get()
    focus = focus_entry.get()
    study_date = date_entry.get()

    # Save to database
    add_session(
    subject,
    float(hours),
    int(focus),
    study_date
)

    messagebox.showinfo("Success", "Study Session Saved!")

# Function to display all sessions
def view_sessions():

    sessions = get_sessions()

    session_text.delete("1.0", tk.END)

    for session in sessions:
        session_text.insert(
            tk.END,
            f"ID: {session[0]} | Subject: {session[1]} | Hours: {session[2]} | Focus: {session[3]} | Date: {session[4]}\n"
        )

 # Function to show analytics
def show_analytics():

    total_hours = get_total_hours()

    average_focus = get_average_focus()

    top_subject = get_top_subject()

    streak = get_streak()

    analytics_text.delete("1.0", tk.END)

    analytics_text.insert(
        tk.END,
        f"Total Study Hours: {total_hours}\n"
    )

    analytics_text.insert(
        tk.END,
        f"Average Focus Score: {average_focus}\n"
    )

    analytics_text.insert(
    tk.END,
    f"Most Studied Subject: {top_subject[0]}\n"
    )

    analytics_text.insert(
    tk.END,
    f"Current Study Streak: {streak} days"
    )

    # Function to show graph
def show_graph():

    data = get_subject_hours()

    subjects = []
    hours = []

    for item in data:
        subjects.append(item[0])
        hours.append(item[1])

    plt.bar(subjects, hours)

    plt.title("Study Hours Per Subject")

    plt.xlabel("Subjects")

    plt.ylabel("Hours Studied")

    plt.show()  

# Function to delete session
def remove_session():

    session_id = delete_entry.get()

    delete_session(session_id)

    messagebox.showinfo(
        "Deleted",
        "Study Session Deleted!"
    )    

# Create window
window = tk.Tk()

window.title("StudyBloom")
window.geometry("700x850")
window.resizable(True, True)
window.configure(bg="#E481CB")

title_label = tk.Label(
    window,
    text="🌸 StudyBloom 🌸",
    font=("Georgia", 22, "bold"),
    bg="#E481CB",
    fg="#4A235A"
)

title_label.pack(pady=15)


# Subject
tk.Label(
    window,
    text="📚 Subject",
    font=("Arial", 11, "bold"),
    bg="#E481CB",
    fg="white"
).pack(pady=5)
subject_entry = tk.Entry(window)
subject_entry.pack()

# Hours
tk.Label(
    window,
    text="⏰ Hours Studied",
    font=("Arial", 11, "bold"),
    bg="#E481CB",
    fg="white"
).pack(pady=5)
hours_entry = tk.Entry(window)
hours_entry.pack()

# Focus
tk.Label(
    window,
    text="🎯 Focus Score (1-10)",
    font=("Arial", 11, "bold"),
    bg="#E481CB",
    fg="white"
).pack(pady=5)
focus_entry = tk.Entry(window)
focus_entry.pack()

# Date
tk.Label(
    window,
    text="📅 Study Date (YYYY-MM-DD)",
    font=("Arial", 11, "bold"),
    bg="#E481CB",
    fg="white"
).pack(pady=5)

date_entry = tk.Entry(window)

date_entry.pack()

# Save Button
save_button = tk.Button(
    window,
    text="💖 Save Session",
    command=save_data,
    width=20,
    bg="#FFC0CB",
    font=("Arial", 10, "bold")
)
save_button.pack(pady=20)

# View Sessions Button
view_button = tk.Button(
    window,
    text="📚 View Sessions",
    command=view_sessions,
    width=20,
    bg="#FFC0CB",
    font=("Arial", 10, "bold")
)
view_button.pack(pady=10)

# Text area to display sessions
session_text = tk.Text(
    window,
    height=4,
    width=60,
    bg="#FFF8FC"
)
session_text.pack()

# Analytics Button
analytics_button = tk.Button(
    window,
    text="📊 Show Analytics",
    command=show_analytics
)

analytics_button.pack(pady=10)

# Analytics display area
analytics_text = tk.Text(
    window,
    height=5,
    width=50,
    bg="#FFF8FC"
)

analytics_text.pack()

# Graph Button
graph_button = tk.Button(
    window,
    text="🌷 Study Graph",
    command=show_graph
)

graph_button.pack(pady=10)

# Delete Session Label
tk.Label(
    window,
    text="🗑 Enter Session ID to Delete",
    font=("Arial", 11, "bold"),
    bg="#E481CB",
    fg="white"
).pack(pady=5)

# Delete Entry Box
delete_entry = tk.Entry(window)

delete_entry.pack()

# Delete Button
delete_button = tk.Button(
    window,
    text="🗑 Delete Session",
    command=remove_session
)

delete_button.pack(pady=10)


footer = tk.Label(
    window,
    text="Made by Aditi 🌸",
    font=("Century Gothic", 9),
    bg="#E481CB",
    fg="black"
)

footer.place(relx=0.98, rely=0.98, anchor="se")

window.mainloop()