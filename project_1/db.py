# SingleTone 
# getter, setter와 같은 것
# 내부에서만 설정 가능한 것.

class Person :
    name = ""
    age = 0
    gender = ""

    def data_setter(self, p1, p2, p3):
        self.name = p1
        self.age = p2
        self.gender = p3
    
    def __str__(self) :
        return f"{self.name} | {self.age} | {self.gender}"

    def add_age(self):
        self.age = self.age + 1

