# Custom Exp.

class LowBalanceExceptionCustom(Exception): # Exception is a parent class to be used for customer exceptions
    def __init__(self, message):
        self.message = message
        super().__init__(message) # calling Exception class's constructora


balance = 100
withdraw = int(input("Enter the amount you want to withdraw"))
if withdraw > balance:
    raise LowBalanceExceptionCustom("Balance is low")
else:
    print("Remain Bal ", (balance - withdraw))

# Output:
# Enter the amount you want to withdraw1000000
# Traceback (most recent call last):
#   File "C:\Users\91981\PycharmProjects\PyATB5xLearning\Dec\ex07122024_ExceptionHandling\Lab173_Exception_Custom_Exception.py", line 12, in <module>
#     raise LowBalanceExceptionCustom("Balance is low")
# LowBalanceExceptionCustom: Balance is low