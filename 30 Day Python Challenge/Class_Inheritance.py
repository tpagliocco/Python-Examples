# You are given two classes, Person and Student
# Person is the base calass, Student is the derived class
# Complete the student class with a constructor and calculate code
# Return grade based on average of all the test scores of the student

class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here

    def __init__(self, firstName, lastName, id, scores):
        Person.__init__(self, firstName, lastName, idNum)
        self.scores = scores


    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here

    def calculate(self):
        self.total = sum(self.scores)
        self.average = self.total // len(self.scores)
        if self.average >= 90:
            self.grade = "O"
        elif self.average >= 80 and self.average <= 89:
            self.grade = "E"
        elif self.average >= 70 and self.average <= 79:
            self.grade = "A"
        elif self.average >= 55 and self.average <= 69:
            self.grade = "P"
        elif self.average >= 40 and self.average <= 54:
            self.grade = "D"
        else:
            self.grade = "T"

        return self.grade
        
line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())

    
    
    
