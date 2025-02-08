class StringManipulator:
    def __init__(self):
        self.text = "" 
    
    def getString(self):
        self.text = input("Введите строку: ") 
    
    def printString(self):
        print(self.text.upper())  


obj = StringManipulator()  
obj.getString()  
obj.printString() 
