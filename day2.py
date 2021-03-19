class Person: #person
    pass
# name,lname,address,dob

class Student(Person): #student
   def __init__(self,fname,lname,address,dob,courses):
       Person.__init__(self,fname,lname,address,dob)
       self.courses = courses 

    def printInfo(self):
        print(self.fname)
        print(self.lname)
        #print all

a = Student("ram","thapa","subidanagar","1997-10-12","BBA")
a.printInfo()






       

