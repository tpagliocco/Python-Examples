# Given the names and grades for each student in a Physics class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
# Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.
#
# Input Format
# The first line contains an integer, N, the number of students.
# The 2N subsequent lines describe each student over 2 lines; the first line contains a student's name, and the second line contains their grade.

#Output Format
#Print the name(s) of any student(s) having the second lowest grade in Physics; if there are multiple students, order their names alphabetically and print each one on a new line.

if __name__ == '__main__':

    # Initialise the marksheet
    pythonStudents = [ ]

    # For each input append the marksheet with name and score
    for _ in range(int(input())):
        name = input()
        score = float(input())
        pythonStudents.append(list([name, score]))

    # Sort the nested list using the scores as the key
    pythonStudentsSrt = sorted(pythonStudents, key=lambda x: x[1])

    # Extract the lowest score
    lowestScore = pythonStudentsSrt[0][1]

    # Find the second lowest score
    secLowestScore = lowestScore
    for element in pythonStudentsSrt:
        if element[1] > lowestScore:
            secLowestScore = element[1]
            break

    # Find all second lowest scorers
    secLowScorers = []
    for element in pythonStudentsSrt:
        if element[1] == secLowestScore:
            secLowScorers.append(element[0])

    # Print the list of second lowest scorers sorted alphabetically in the correct format
    print(*["".join(i) for i in sorted(secLowScorers)], sep='\n')