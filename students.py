
import tkinter as tk
from tkinter import messagebox

# List to store all student records
students = []


# Function to add a new student
def add_student():

    # Get student name from user
    name = input("Enter Student Name: ")

    # Get student marks and convert to integer
    marks = int(input("Enter Marks: "))

    # Get course name
    course = input("Enter Course: ")

    # Create a dictionary for one student
    student = {
        "name": name,
        "marks": marks,
        "course": course
    }

    # Add student dictionary to the students list
    students.append(student)

    # Display success message
    print("Student Added Successfully")


# Function to display all students
def view_students():

    # Check if list is empty
    if len(students) == 0:
        print("No Students Found")
        return

    # Heading
    print("\n----- Student List -----")

    # Loop through each student
    for student in students:

        # Display student details
        print(
            f"Name: {student['name']}, "
            f"Marks: {student['marks']}, "
            f"Course: {student['course']}"
        )


# Function to search for a student
def search_student():

    # Get name to search
    name = input("Enter Student Name to Search: ")

    # Loop through all students
    for student in students:

        # Compare names ignoring uppercase/lowercase
        if student["name"].lower() == name.lower():

            # Display found message
            print("Student Found")

            # Display student record
            print(student)

            # Exit function
            return

    # Executes if student not found
    print("Student Not Found")


# Function to update student marks
def update_marks():

    # Get student name
    name = input("Enter Student Name: ")

    # Loop through students
    for student in students:

        # Check matching name
        if student["name"].lower() == name.lower():

            # Get new marks
            new_marks = int(input("Enter New Marks: "))

            # Update marks value
            student["marks"] = new_marks

            # Success message
            print("Marks Updated Successfully")

            # Exit function
            return

    # If no matching student found
    print("Student Not Found")


# Function to delete a student
def delete_student():

    # Get student name
    name = input("Enter Student Name: ")

    # Loop through students
    for student in students:

        # Check matching name
        if student["name"].lower() == name.lower():

            # Remove student from list
            students.remove(student)

            # Success message
            print("Student Deleted Successfully")

            # Exit function
            return

    # If student not found
    print("Student Not Found")


# Main function containing menu
def main():

    # Infinite loop until user exits
    while True:

        # Display menu
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Marks")
        print("5. Delete Student")
        print("6. Exit")

        # Get user choice
        choice = input("Enter Choice: ")

        # Call add_student function
        if choice == "1":
            add_student()

        # Call view_students function
        elif choice == "2":
            view_students()

        # Call search_student function
        elif choice == "3":
            search_student()

        # Call update_marks function
        elif choice == "4":
            update_marks()

        # Call delete_student function
        elif choice == "5":
            delete_student()

        # Exit program
        elif choice == "6":
            print("Thank You")
            break

        # Invalid choice
        else:
            print("Invalid Choice")


# Starting point of the program
if __name__ == "__main__":
    main()