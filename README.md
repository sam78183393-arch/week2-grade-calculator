week2-grade-calculator

A grade calculator that processes multiple students' marks, calculates
grades with personalized comments, and prints class statistics — built to
practice conditionals, lists, loops, functions, and error handling.

What I Learned:
Conditional Logic — using `if`/`elif`/`else` to turn a numeric average
into a letter grade.
Lists — storing names, marks, and results for multiple students using
parallel lists (`student_names`, `student_marks`, `student_results`).
Loops — a `for` loop processes every student; `while` loops keep
re-prompting until input is valid (positive student count, non-empty
name, marks in range).
Error Handling — `try`/`except` around `int()`/`float()` conversions
so invalid input doesn't crash the program.
Functions — `calculate_grade()` and `get_valid_number()` keep the
logic organized and reusable.

FeaturesProject Description:

✅ Processes multiple students
✅ Calculates grades based on a custom grading system (`if/elif/else`)
✅ Personalized comment for every grade
✅ Class statistics: average, highest, and lowest scorer
✅ Formatted table output of all results
✅ Input validation for student count, names, and marks
✅ Error handling for invalid (non-numeric) input
Project Structure
```
week2-grade-calculator/
│── grade_calculator.py     # Main program
│── test_students.txt       # Sample stdin input for non-interactive testing
│── results_sample.txt      # Example program output
│── README.md               # This file
└── .gitignore
```
Grading System
Grade	Range	Comment
A	90–100	Excellent! Keep up the great work!
B	80–89	Very Good! You're doing well.
C	70–79	Good. Room for improvement.
D	60–69	Needs Improvement. Please study more.
F	0–59	Failed. Please seek help from your teacher.
How to Run
Requirements
Python 3.9+ (no third-party dependencies)
Interactive mode
```bash
cd week2-grade-calculator
python3 grade_calculator.py
```
Enter the number of students, then each student's name and marks (0–100)
for Math, Science, and English. The program prints the results table and
class statistics automatically at the end.
Non-interactive / test mode
```bash
python3 grade_calculator.py < test_students.txt
```
Sample Output
```
==================================================
      STUDENT GRADE CALCULATOR
==================================================

Enter number of students: 2

=== STUDENT 1 ===
Student name: John Smith
Enter marks (0-100):
Math: 85
Science: 92
English: 88

=== STUDENT 2 ===
Student name: Sarah Johnson
Enter marks (0-100):
Math: 78
Science: 81
English: 85

============================================================
                    RESULTS SUMMARY
============================================================
Name                 |   Avg | Grade | Comment
------------------------------------------------------------
John Smith           |  88.3 |   B   | Very Good! You're doing well.
Sarah Johnson        |  81.3 |   B   | Very Good! You're doing well.

============================================================
                   CLASS STATISTICS
============================================================
Total Students: 2
Class Average: 84.8
Highest Average: 88.3 (John Smith)
Lowest Average: 81.3 (Sarah Johnson)

============================================================
Thank you for using the Grade Calculator!
============================================================
```
Challenges & Solutions
Handling invalid marks input — Solved with a `while True` loop
wrapped in `try`/`except ValueError` inside `get_valid_number()`,
re-prompting until a number between 0 and 100 is entered.
Validating the student count and name fields — Solved with their own
small `while` loops that reject non-numbers, zero/negative counts, and
blank names before moving on.
Formatting the results table — Solved using fixed-width f-string
formatting (`f"{name:<20}"`, `f"{average:>5.1f}"`) so columns line up no
matter how long a name is.
Calculating multiple statistics — Solved with a list comprehension to
pull out all averages, then `sum()`, `max()`, `min()`, and `.index()` to
get the class average, top scorer, and lowest scorer.
Testing Evidence
Running `python3 grade_calculator.py < test_students.txt` feeds in 2
students (John Smith and Sarah Johnson) with their Math/Science/English
marks, and produces the results table and class statistics shown above.
`results_sample.txt` captures that expected output for reference.
