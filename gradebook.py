#!/usr/bin/env python3

# Task 1: Create a list called subjects
subjects = ["physics", "calculus", "poetry", "history"]

# Task 2: Create a list called grades
grades = [98, 97, 85, 88]

# Task 3: Create a two-dimensional list to combine subjects and grades
gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]

# Task 4: Print gradebook
print(gradebook)

# Task 5: Add computer science grade to gradebook
gradebook.append(["computer science", 100])

# Task 6: Add visual arts grade to gradebook
gradebook.append(["visual arts", 93])

# Task 7: Modify visual arts grade to include extra points
gradebook[4][1] += 5

# Task 8: Remove poetry grade from gradebook
gradebook.remove(["poetry", 85])

# Task 9: Add a "Pass" value to the sublist where poetry was removed
gradebook.append(["poetry", "Pass"])

# Task 10: Combine last_semester_gradebook and gradebook to create full_gradebook
last_semester_gradebook = [["Biology", 89], ["History", 84]]
full_gradebook = last_semester_gradebook + gradebook

# Print full_gradebook
print(full_gradebook)

