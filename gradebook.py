# Calculate the average of a student's marks
def calculate_average(marks):
    pass


# Find the highest and lowest marks
def highest_and_lowest(marks):
    pass


# Ask for a mark and make sure it is valid
def read_valid_mark():
    pass

# Add a new student to the gradebook
def add_student(gradebook):
    # Ask the user to enter the student's name
    name = input("Enter student name: ")

    # See if the student is already in the gradebook
    if name in gradebook:
        print("Student already exists.")
    else:
        gradebook[name] = []
        print(name, "was added successfully.")

# Add a mark to an existing student
def add_mark(gradebook):
    pass


# Display all students and their marks
def view_all(gradebook):
    pass

# Show a summary for one student
def student_summary(gradebook):
    pass


# Show statistics for the whole class
def class_statistics(gradebook):
    pass


# Remove a student from the gradebook
def remove_student(gradebook):
    pass

# Create the gradebook that will store students and their marks
gradebook = {}

# Keep showing the menu until the user chooses to exit
while True:
    print("\nStudent Gradebook Manager")
    print("1. Add student")
    print("2. Add mark")
    print("3. View all students")
    print("4. Student summary")
    print("5. Class statistics")
    print("6. Remove student")
    print("7. Exit")

    choice = input("Choose an option: ")

    # Run the correct function depending on the user's choice
    if choice == "1":
        add_student(gradebook)
    elif choice == "2":
        add_mark(gradebook)
    elif choice == "3":
        view_all(gradebook)
    elif choice == "4":
        student_summary(gradebook)
    elif choice == "5":
        class_statistics(gradebook)
    elif choice == "6":
        remove_student(gradebook)
    elif choice == "7":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Please choose from 1 to 7.")


