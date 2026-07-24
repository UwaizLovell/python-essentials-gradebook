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
    pass


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

    if choice == "7":
        print("Goodbye!")
        break


