# Student Grade Calculator
# Week 2 Project - Control Flow & Data Structures
# Author: Sam Joshua V S

def calculate_grade(average):
    """Use if/elif/else to determine grade and a personalized comment."""
    if average >= 90:
        return 'A', 'Excellent! Keep up the great work!'
    elif average >= 80:
        return 'B', "Very Good! You're doing well."
    elif average >= 70:
        return 'C', 'Good. Room for improvement.'
    elif average >= 60:
        return 'D', 'Needs Improvement. Please study more.'
    else:
        return 'F', 'Failed. Please seek help from your teacher.'


def get_valid_number(prompt, min_val=0, max_val=100):
    """While loop + try/except: keep asking until a valid number is entered."""
    while True:
        try:
            value = float(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Please enter a number between {min_val} and {max_val}.")
        except ValueError:
            print("Invalid input! Please enter a number.")


def main():
    print("=" * 50)
    print("      STUDENT GRADE CALCULATOR")
    print("=" * 50)

    # While loop + try/except: validate number of students
    while True:
        try:
            num_students = int(input("\nEnter number of students: "))
            if num_students > 0:
                break
            else:
                print("Please enter a positive number!")
        except ValueError:
            print("Invalid input! Please enter a whole number.")

    # List operations: store data for multiple students
    student_names = []
    student_marks = []      # list of lists -> [math, science, english] per student
    student_results = []    # list of (average, grade, comment) per student

    # For loop: process every student
    for i in range(num_students):
        print(f"\n=== STUDENT {i + 1} ===")

        # While loop: validate name isn't empty
        name = input("Student name: ")
        while name.strip() == "":
            print("Name cannot be empty!")
            name = input("Student name: ")
        student_names.append(name)

        print("Enter marks (0-100):")
        math = get_valid_number("Math: ")
        science = get_valid_number("Science: ")
        english = get_valid_number("English: ")

        student_marks.append([math, science, english])

        average = (math + science + english) / 3
        grade, comment = calculate_grade(average)
        student_results.append((average, grade, comment))

    # Formatted table of results
    print("\n" + "=" * 60)
    print("                    RESULTS SUMMARY")
    print("=" * 60)
    print(f"{'Name':<20} | {'Avg':>5} | {'Grade':^5} | Comment")
    print("-" * 60)

    for i in range(num_students):
        name = student_names[i]
        average, grade, comment = student_results[i]
        print(f"{name:<20} | {average:>5.1f} | {grade:^5} | {comment}")

    # Statistics: average, highest, lowest
    if num_students > 0:
        averages = [result[0] for result in student_results]
        class_avg = sum(averages) / len(averages)
        max_avg = max(averages)
        min_avg = min(averages)
        max_index = averages.index(max_avg)
        min_index = averages.index(min_avg)

        print("\n" + "=" * 60)
        print("                   CLASS STATISTICS")
        print("=" * 60)
        print(f"Total Students: {num_students}")
        print(f"Class Average: {class_avg:.1f}")
        print(f"Highest Average: {max_avg:.1f} ({student_names[max_index]})")
        print(f"Lowest Average: {min_avg:.1f} ({student_names[min_index]})")

    print("\n" + "=" * 60)
    print("Thank you for using the Grade Calculator!")
    print("=" * 60)


if __name__ == "__main__":
    main()
