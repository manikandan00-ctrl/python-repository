class stud:
    def __init__(self,a,b,c):
        self.sno=a
        self.sname=b
        self.sage=c
    def display(self):
        print("no",self.sno)
        print("name",self.sname)
        print("age",self.sage)

class marks(stud):
    def __init__(self,a,b,c,m1,m2,m3):
        super().__init__(a,b,c)
        self.marks1=m1
        self.marks2=m2
        self.marks3=m3
    def display(self):
        super().display()
        print("marks1",self.marks1)
        print("marks2",self.marks2)
        print("marks3",self.marks3)


ob=marks(1,"abc",24,50,67,78)
ob.display()
