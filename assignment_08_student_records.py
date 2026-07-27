# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 8
# Topic: Lists of Dictionaries, Loops, and Functions
# =============================================================================
#
# TASK: Student Record Management System
#
# Build a console-based program that stores and manages student information.
# Each student record must contain:
#
#   - Name   : the student's full name (text)
#   - ID     : a unique student ID number (e.g. 20240001)
#   - Scores : a list of scores from multiple assessments (e.g. [75, 88, 90])
#
# -----------------------------------------------------------------------------
# FEATURES YOUR PROGRAM MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Add a Student
#      - Ask the user to enter the student's name and ID.
#      - Ask how many scores to enter, then collect each score one by one.
#      - Save the student record and confirm it was added.
#
#   2. Display All Students
#      - Print a formatted table showing every student's:
#          Name, ID, individual scores, and their average score.
#      - If no students have been added yet, print a message saying so.
#
#   3. Calculate Average Score for a Specific Student
#      - Ask the user to enter a student ID.
#      - Find the student and calculate the average of their scores.
#      - Display the result. If the ID is not found, print an error message.
#
#   4. Quit
#      - End the program.
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ================================
#      STUDENT RECORD SYSTEM MENU
#   ================================
#   1. Add student
#   2. Display all students
#   3. Calculate average score
#   4. Quit
#   Enter your choice (1-4):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Enter your choice (1-4): 1
#   Student name: Alice Mensah
#   Student ID: 20240001
#   How many scores? 3
#   Enter score 1: 78
#   Enter score 2: 85
#   Enter score 3: 90
#   Student "Alice Mensah" added successfully.
#
#   Enter your choice (1-4): 2
#   --------------------------------------------------
#   Name           ID          Scores         Average
#   --------------------------------------------------
#   Alice Mensah   20240001    78, 85, 90     84.33
#   --------------------------------------------------
#
#   Enter your choice (1-4): 3
#   Enter student ID: 20240001
#   Alice Mensah's average score: 84.33
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Store all student records in a list of dictionaries.
#   Example structure:
#       student = {
#           "name": "Alice Mensah",
#           "id": 20240001,
#           "scores": [78, 85, 90]
#       }
# - Average scores should be rounded to 2 decimal places.
# - Each feature MUST be implemented in its own function (see scaffold below).
# - Handle invalid menu choices and missing student IDs gracefully.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def add_student(students):
    """Ask for name, ID, scores count, and collect scores one by one."""
    name = input("Student name: ")
    student_id = input("Student ID: ")
    
    scores = []
    try:
        num_scores = int(input("How many scores? "))
        for i in range(1, num_scores + 1):
            score = float(input(f"Enter score {i}: "))
            scores.append(score)
    except ValueError:
        print("Error: Please enter a valid number for scores.")
        return

    student = {
        "name": name,
        "id": student_id,
        "scores": scores
    }
    students.append(student)
    print(f'Student "{name}" added successfully.')

def display_students(students):
    """Print a formatted table showing every student's name, ID, scores, and average."""
    if len(students) == 0:
        print("No student records have been added yet.")
        return

    print("-" * 75)
    print(f"{'Name':<20} {'ID':<12} {'Scores':<25} {'Average':<10}")
    print("-" * 75)
    
    for student in students:
        name = student["name"]
        student_id = student["id"]
        scores_str = ", ".join(str(s) for s in student["scores"])
        
        # Calculate average
        avg = sum(student["scores"]) / len(student["scores"]) if student["scores"] else 0
        
        print(f"{name:<20} {student_id:<12} {scores_str:<25} {avg:<10.2f}")
    
    print("-" * 75)

def calculate_student_average(students):
    """Find a student by ID and display their rounded average score."""
    if len(students) == 0:
        print("No student records available.")
        return

    search_id = input("Enter student ID: ")
    
    found = False
    for student in students:
        if student["id"] == search_id:
            found = True
            if student["scores"]:
                avg = sum(student["scores"]) / len(student["scores"])
                print(f"{student['name']}'s average score: {avg:.2f}")
            else:
                print(f"{student['name']} has no scores recorded.")
            break
            
    if not found:
        print(f"Error: Student ID '{search_id}' not found.")

def student_record_system():
    """Main function to run the student management menu loop."""
    students = []
    
    while True:
        print("\n=====================================")
        print("         STUDENT RECORD SYSTEM MENU   ")
        print("=====================================")
        print("1. Add student")
        print("2. Display all students")
        print("3. Calculate average score")
        print("4. Quit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            add_student(students)
        elif choice == '2':
            display_students(students)
        elif choice == '3':
            calculate_student_average(students)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Error: Invalid choice. Please enter a number between 1 and 4.")

# Execute the application
if __name__ == "__main__":
    student_record_system()