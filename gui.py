
# Import tkinter library for creating GUI applications
import tkinter as tk

# Import messagebox for popup messages
from tkinter import messagebox

# Import the students list from the existing program
# We are reusing the same data structure
from students import students


# ==================================================
# FUNCTION TO ADD A NEW STUDENT
# ==================================================
def add_student_gui():

    # Get text entered in Name field
    name = name_entry.get()

    # Get text entered in Marks field
    marks = marks_entry.get()

    # Get text entered in Course field
    course = course_entry.get()

    # Check whether any field is empty
    if not name or not marks or not course:

        # Show error popup
        messagebox.showerror(
            "Error",
            "All fields are required"
        )

        # Stop function execution
        return

    # Create dictionary and add it to students list
    students.append({
        "name": name,
        "marks": int(marks),
        "course": course
    })

    # Show success popup
    messagebox.showinfo(
        "Success",
        "Student Added Successfully"
    )

    # Clear Name textbox
    name_entry.delete(0, tk.END)

    # Clear Marks textbox
    marks_entry.delete(0, tk.END)

    # Clear Course textbox
    course_entry.delete(0, tk.END)

    # Refresh student list display
    view_students_gui()


# ==================================================
# FUNCTION TO DISPLAY ALL STUDENTS
# ==================================================
def view_students_gui():

    # Remove all old items from listbox
    listbox.delete(0, tk.END)

    # Loop through each student record
    for student in students:

        # Create formatted text
        student_info = (
            f"{student['name']} | "
            f"{student['marks']} | "
            f"{student['course']}"
        )

        # Add student information into listbox
        listbox.insert(
            tk.END,
            student_info
        )


# ==================================================
# CREATE MAIN APPLICATION WINDOW
# ==================================================

# Create root window object
root = tk.Tk()

# Set window title
root.title("Student Management System")

# Set window size
root.geometry("600x400")


# ==================================================
# NAME SECTION
# ==================================================

# Label for student name
tk.Label(
    root,
    text="Student Name"
).pack()

# Textbox for entering student name
name_entry = tk.Entry(
    root,
    width=40
)

# Display textbox on screen
name_entry.pack()


# ==================================================
# MARKS SECTION
# ==================================================

# Label for marks
tk.Label(
    root,
    text="Marks"
).pack()

# Textbox for entering marks
marks_entry = tk.Entry(
    root,
    width=40
)

# Display textbox
marks_entry.pack()


# ==================================================
# COURSE SECTION
# ==================================================

# Label for course
tk.Label(
    root,
    text="Course"
).pack()

# Textbox for entering course name
course_entry = tk.Entry(
    root,
    width=40
)

# Display textbox
course_entry.pack()


# ==================================================
# BUTTON TO ADD STUDENT
# ==================================================

# Create button
tk.Button(
    root,

    # Text shown on button
    text="Add Student",

    # Function executed when button is clicked
    command=add_student_gui

).pack(
    pady=10
)


# ==================================================
# BUTTON TO VIEW STUDENTS
# ==================================================

# Create button
tk.Button(
    root,

    # Text shown on button
    text="View Students",

    # Function called on click
    command=view_students_gui

).pack()


# ==================================================
# LISTBOX TO DISPLAY STUDENTS
# ==================================================

# Create listbox widget
listbox = tk.Listbox(
    root,

    # Width of listbox
    width=70,

    # Number of visible rows
    height=10
)

# Display listbox
listbox.pack(
    pady=20
)


# ==================================================
# START GUI EVENT LOOP
# ==================================================

# Keeps window running and waiting for user actions
root.mainloop()