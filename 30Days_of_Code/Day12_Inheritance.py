# Hackerrank 30 Days of code Challenge
# https://www.hackerrank.com/domains/tutorials/30-days-of-code
# Day 12

class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name.:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
	def __init__(self, firstName, lastName, idNumber, scores):
		Person.__init__(self, firstName, lastName, idNumber)
		self.scores = scores
		self.avg_score = sum(scores) / len(scores)
	def calculate(self):
		if self.avg_score < 40:
			return "T"
		elif self.avg_score < 55:
			return "D"
		elif self.avg_score < 70:
			return "P"
		elif self.avg_score < 80:
			return "A"
		elif self.avg_score < 90:
			return "E"
		else:
			return "O"


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list(map(int, input().split()))
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
