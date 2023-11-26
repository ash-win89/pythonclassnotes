class student:

    def setname(self,name):
        self.name = name

    def getname(self):
        return 'the entered name is',self.name

    def setmarks(self,marks):
        self.marks = marks

    def getmarks(self):
        return  'the student earned marks',self.marks


for i in range(2):
    s = student()
    name = input('enter the name of student')
    s.setname(name)
    marks = int(input('enter the student mark'))
    s.setmarks(marks)
    print(s.getname())
    print(s.getmarks())
