class Monitor:
    #initialize the class
    def __init__(self,kulay="",laki=0,hugis="",pangalan="",sulat=""):
        self.color=kulay #attributes
        self.size=laki
        self.shape=hugis
        self.brand=pangalan
        self.text=sulat

    #define methods or things the class can do
    def getInfo(self,message):
        self.text=message

    def displayInfo(self):
        print("The message is",self.text)

    def showAttributes(self):
        print("color=",self.color)
        print("size=",self.size)
        print("brand=",self.brand)
        print("shape=",self.shape)

#call the class Monitor and create an object called "mon"

mon=Monitor()
mon.shape="triangle"
mon.size=50
mon.brand="asus"
mon.color="green"
mon.text="thank you"

mon.showAttributes()
mon.displayInfo()
mon.text="get out"
mon.displayInfo()
mon.getInfo("LOL")
mon.displayInfo()

#kulay="",laki=0,hugis="",pangalan="",sulat=""
print("\n")
print("This is object 2 called mon2")
mon2=Monitor("black", 45, "round", "lenovo", "crash out")
mon2.showAttributes()
mon2.displayInfo()
