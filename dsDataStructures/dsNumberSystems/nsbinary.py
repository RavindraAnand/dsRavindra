class nsbinary:

    def __init__(self,decimalvalue):
        self.decimalvalue = decimalvalue
        self.lsBinary=[]

    def recursivebinaryTodecimal(self):
        if self.decimalvalue > 1:
            self.recursivebinaryTodecimal(self.decimalvalue//2)
        print(self.decimalvalue % 2)
