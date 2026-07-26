# Calculate the average of a student's marks
def calculate_average(marks):
    
    # If there are no marks return none
    if len(marks) == 0:
       return None

    # Calculate the average and return
    return sum(marks) / len(marks)

# Find the highest and lowest marks
def highest_and_lowest(marks):

    # Return a none value if there are no marks
    if len(marks) == 0:
       return None, None
    
    # Return the highest and Lowest marks as a tuple
    return max(marks), min(marks)

# Ask for a mark and make sure it is valid
def read_valid_mark():

    # Exception handling to verify the the mark is valid
    while True:
       try:
          mark = float(input("Enter mark: "))
       except ValueError:
          print("Please enter a number.")
       else:
           # See if the mark is in the valid range of 0 - 100
           if mark >= 0 and mark <= 100:
               return mark
           else:
               print("Enter valid mark between 0 and 100.")      

# Add a new student to the gradebook
def add_student(gradebook):
    # Ask the user to enter the student's name
    name = input("Enter student name: ")

    # See if the user enters a blank field
    if name == "":
        print("Student name cannot be blank.")
        return 
    # See if the student is already in the gradebook
    if name in gradebook:
        print("Student already exists.")
    else:
        gradebook[name] = []
        print(name, "was added successfully.")

# Add a mark to an existing student
def add_mark(gradebook):

    # Ask which student the mark belongs to 
    name = input("Enter student name: ")

    # See if the student exists before entering the mark
    if name not in gradebook:
        print("Student not found.")
    else:
        # Recieve a valid mark from the user
        mark = read_valid_mark()
        
        # Enter the mark to the student's list 
        gradebook[name].append(mark) 

        # Confirm the mark was added into the list 
        print("Mark added successfully.")

# Display all students and their marks
def view_all(gradebook):
    # See if their are or aren't students in the gradebook 
    if len(gradebook) == 0: 
        print("Gradebook empty, no students entered.")
    else:
        # Go through gradebook and display their name, marks and average
        for name in gradebook:
            marks = gradebook[name]
            average = calculate_average(marks)

            if average is None:
                print(name, marks, "Average: n/a")
            else:
                print(name, marks, "Average:", round(average, 2))

# Show a summary for one student
def student_summary(gradebook):

    # Ask the user what student they want to show the summary for
    name = input("Enter student name: ")

    # See if the student is in the gradebook 
    if name not in gradebook:
        print("Student not found.")
    elif len(gradebook[name]) == 0:
        print("Marks are not recorded for this student.")
    else:
        marks = gradebook[name]

        # To calculate the average of the student's marks
        average = calculate_average(marks)

        # To find the highest and lowest marks the student has recieved 
        highest, lowest = highest_and_lowest(marks)

        # To display the student summary 
        print("Student:", name)
        print("Marks:", marks)
        print("Number of marks:", len(marks))
        print("Average:", round(average, 2))
        print("Highest:", highest)
        print("Lowest:", lowest)

# Show the statistics for the whole class
def class_statistics(gradebook):

    # See if there is or isn't any students in the gradebook
    if len(gradebook) == 0:
        print("No student found in the gradebook.")
    else:
        # Display the total number of students
        print("Total students:", len(gradebook))

        # To create an empty list to store all the marks of the students in class 
        all_marks = []
        
        # Create lists for passing, failing and students with no marks
        passing = []
        failing = []
        no_marks = []
        
        # Go through all the students in the gradebook 
        for name in gradebook:

            # Look through each mark that belongs to that student 
            for mark in gradebook[name]:
                all_marks.append(mark)
 
            # See if the student has marks or not
            if len(gradebook[name]) == 0:
                no_marks.append(name)
            else: 
                # Calculate the students average 
                average = calculate_average(gradebook[name])

                # See if the student is passing or failing
                if average >= 50:
                    passing.append(name)
                else:
                    failing.append(name)

        # Find the student with the highest average
        top_student = None
        top_average = None

        for name in gradebook:
            if len(gradebook[name]) > 0:
                average = calculate_average(gradebook[name])

                if top_average is None or average > top_average:
                    top_student = name
                    top_average = average

        # To handle students with no marks, See if no marks were recorded
        if len(all_marks) == 0:
            print(" Marks have not been recorded yet.")
        else:
            # To calculate the average mark for the class 
            class_average = round(sum(all_marks) / len(all_marks), 2)
            
            # Find the highest and lowest marks in the class 
            highest = max(all_marks)
            lowest = min(all_marks) 

            # Display the class stats 
            print("Class Average:", class_average)
            print("Class Highest:", highest)
            print("Class Lowest:", lowest)
            print("Top student:", top_student, "Average:", round(top_average, 2))
     
        # Display the student grouping of whether they are passing, failing or have no marks entered
        print("Passing students:", passing)
        print("Failing students:", failing)
        print("Students with no marks:", no_marks)

# Remove a student from the gradebook
def remove_student(gradebook):
    
    # Ask the user which student you want to remove 
    name = input("Enter student name: ")
    
    # See if the student is in the gradebook
    if name not in gradebook: 
        print("No student found with that name.")
    else:
        # Ask the user to confirm before removing the student
        confirm = input("Are you sure you want to remove this student? (y/n): ")

        if confirm == "y":
            # Remove the student from the gradebook
            del gradebook[name]
            print(name, "was removed successfully.")
        else:
            print("Removal cancelled.")

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


