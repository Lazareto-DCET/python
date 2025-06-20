class MDAS:
    def __init__(self,n1=0,n2=0):
        self.num1=n1
        self.num2=n2

    def setNum1(self,n1):
        self.num1=n1
        
    def setNum2(self,n2):
        self.num2=n2

    def getSum(self):
        self.sum1=self.num1+self.num2
        return self.sum1

    def getDiff(self):
        self.diff1=self.num1-self.num2
        return self.diff1

    def getProduct(self):
        self.product1=self.num1*self.num2
        return self.product1

    def getQuotient(self):
        self.quo1=self.num1/self.num2
        return self.quo1

while True:
    print("===================")
    print("  MDAS Calculator  ")
    print("===================")
    print("[A]ddition")
    print("[S]ubtraction")
    print("[M]ultiplication")
    print("[D]ivision")
    print("[E]xit")
    print("-------------------")
    choice=input("Enter your choice: ")

    if (choice=="A" or choice=="a"):
        while True:
            try:
                a=MDAS()
                n1=float(input("Enter 1st No.: "))
                n2=float(input("Enter 2nd No.: "))
                n3=float(input("Enter 3rd No.: "))
                a.setNum1(n1)
                a.setNum2(n2)
                a.setNum1(a.getSum())
                a.setNum2(n3)
                s=a.getSum()
                print("The sum is", s)
                break
            except ValueError:
                print("\nYou just entered a letter, try again")

    elif (choice=="S" or choice=="s"):
        while True:
            try:
                s=MDAS()
                n1=float(input("Enter 1st No.: "))
                n2=float(input("Enter 2nd No.: "))
                n3=float(input("Enter 3rd No.: "))
                s.setNum1(n1)
                s.setNum2(n2)
                s.setNum1(s.getDiff())
                s.setNum2(n3)
                d=s.getDiff()
                print("The difference is", d)
                break
            except ValueError:
                print("\nYou just entered a letter, try again")

    elif (choice=="M" or choice=="m"):
        while True:
            try:
                m=MDAS()
                n1=float(input("Enter 1st No.: "))
                n2=float(input("Enter 2nd No.: "))
                n3=float(input("Enter 3rd No.: "))
                m.setNum1(n1)
                m.setNum2(n2)
                m.setNum1(m.getProduct())
                p=m.getProduct()
                print("The product is", p)
                break
            except ValueError:
                print("\nYou just entered a letter, try again")

    elif (choice=="D" or choice=="d"):
        while True:
            try:
                d=MDAS()
                n1=float(input("Enter 1st No.: "))
                n2=float(input("Enter 2nd No.: "))
                n3=float(input("Enter 3rd No.: "))
                d.setNum1(n1)
                d.setNum2(n2)
                d.setNum1(d.getQuotient())
                q=d.getQuotient()
                print("The quotient is", q)
                break
            except ValueError:
                print("\nYou just entered a letter, try again")

    elif (choice=="E" or choice=="e"):
        print("\nProgram Terminated Successfully")
        break
    else:
        print("\nInvalid Operation, try again!")



