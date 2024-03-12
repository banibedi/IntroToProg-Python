# Title: Assignment04
# Desc: This assignment demonstrates how to do data processing using lists and files ()
# Bani Bedi, 2/9/24, Created Script

# Set My Variables
student_first_name: str = ""
student_last_name: str = ""
course_name: str = ""
menu_choice: str = ""
student_data: dict = {}
students: list = []

# Display Menu
MENU: str = """
---Course Registration Program---
Select from the following menu:
    1. Register a Student for a Course
    2. Show current data
    3. Save data to a file
    4. Exit the program
__________________________________
"""

# Creating the Table Guidelines
def print_students():
    if not students:
        print("No students registered yet.")
    else:
        print("Current Data:")
        print("First Name\tLast Name\tCourse Name")
        for student_data in students:
            print(f"{student_data[0]}\t\t{student_data[1]}\t\t{student_data[2]}")

while True:
    print(MENU)
    menu_choice = input("Which of the following would you like to select: ")

    # If User Choice is 1
    if menu_choice == "1":
        while True:  # Loop to allow registering multiple students
            student_first_name = input("Enter your first name: ")
            student_last_name = input("Enter your last name: ")
            course_name = input("Please enter the name of your course: ")
            students.append([student_first_name, student_last_name, course_name])
            menu_choice = input("Would you like to register another student? (y/n): ")
            if menu_choice == "y":
                continue
            else:
                break

    # If User Choice is 2
    elif menu_choice == "2":
        print_students()

    # If User Choice is 3
    elif menu_choice == "3":
        if not students:
            print("No students registered yet. Data not saved.")
        else:
            file_name = "Enrollments.csv"
            with open(file_name, "w") as file:
                for student_data in students:
                    file.write(f"{student_data[0]}, {student_data[1]}, {student_data[2]}\n")
            print("Data saved to", file_name)

    # If User Choice is 4
    elif menu_choice == "4":
        print("Program Ended")
        break
    else:
        print('Invalid input. Please try again.')
