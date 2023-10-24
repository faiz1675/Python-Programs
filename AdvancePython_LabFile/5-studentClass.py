#5- Create a class named as Student to store the name and marks in
#  three subjects. Use List to store the marks.
# a. Write an instance method called compute to compute total marks and 
# average marks of a student. 
# b. Write a method called display to display student information. 

class Student:
    subj=['Python','Java','DBMS']
    marks=[]
    total=0
    avg=0
    def __init__(self,name):
        self.name=name
        print("Enter your marks of three subjects")
        for i in range(1,4):
            m=int(input())
            Student.marks.append(m)
    def compute(self):
        for i in Student.marks:
            Student.total+=i
        Student.avg=Student.total/len(Student.marks)
        print("Total Marks = ",Student.total)
        print("Average Marks = ",Student.avg)
    def displayDetails(self):
        print("Name : ",self.name)
        c=0
        for i in Student.marks:
            print("Marks in {} = {}".format(Student.subj[c],i))
            c+=1
s=Student("Faiz")
s.displayDetails()
s.compute()