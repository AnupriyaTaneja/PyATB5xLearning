from abc import ABC, abstractmethod

class Father(ABC):
    def __init__(self,name):
        self.name = name
        print("Loan completed by: ", name)

    @abstractmethod
    def loan(self):
        pass


class Son(Father):
    def loan(self):
        print("1L given")


son_obj = Son("xyz")
son_obj.loan()