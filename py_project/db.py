class Snack :
    name = ""
    price = 0
    company = ""

    def data_setter(self, p1, p2 ,p3):
        self.name = p1
        self.price = p2
        self.company = p3


    def __str__(self):
        return f"{self.name} | {self.price} | {self.company}"
    
class Juice :
    name = ""
    price = 0
    company = ""

    def data_setter(self, p1, p2, p3):
        self.name = p1
        self.price = p2
        self.company = p3
    
    def __str__(self):
        return f"{self.name} | {self.price} | {self.company}"


class Etc : 
    name = ""
    price = 0
    company = ""

    def data_setter(self, p1 ,p2, p3):
        self.name = p1
        self.price = p2
        self.company = p3
    
    def __str__(self):
        return f"{self.name} | {self.price} | {self.company}"