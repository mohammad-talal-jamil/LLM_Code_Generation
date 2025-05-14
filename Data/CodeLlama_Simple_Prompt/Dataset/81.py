def numerical_letter_grade(grades):
    """
    This function takes a list of GPAs as input and returns a list of letter grades based on the following table:
    GPA       |    Letter grade
    4.0                A+
    > 3.7                A 
    > 3.3                A- 
    > 3.0                B+
    > 2.7                B 
    > 2.3                B-
    > 2.0                C+
    > 1.7                C
    > 1.3                C-
    > 1.0                D+ 
    > 0.7                D 
    > 0.0                D-
    0.0                E
    """
    letter_grades = []
    for gpa in grades:
        if gpa >= 4.0:
            letter_grade = 'A+'
        elif gpa >= 3.7:
            letter_grade = 'A'
        elif gpa >= 3.3:
            letter_grade = 'A-'
        elif gpa >= 3.0:
            letter_grade = 'B+'
        elif gpa >= 2.7:
            letter_grade = 'B'
        elif gpa >= 2.3:
            letter_grade = 'B-'
        elif gpa >= 2.0:
            letter_grade = 'C+'
        elif gpa >= 1.7:
            letter_grade = 'C'
        elif gpa >= 1.3:
            letter_grade = 'C-'
        elif gpa >= 1.0:
            letter_grade = 'D+'
        elif gpa >= 0.7:
            letter_grade = 'D'
        elif gpa >= 0.0:
            letter_grade = 'D-'
        else:
            letter_grade = 'E'
        letter_grades.append(letter_grade)
    return letter_grades
