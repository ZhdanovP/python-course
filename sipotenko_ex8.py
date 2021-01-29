#Exercise 8
#
#    Implement DebitCard model. You must implementing following operation:
#        authorize(pin) -> bool
#        Withdrawal(money) -> int
#        GetBalance() -> int
#    These operations must be return correct result if user call authorize() before
#    Otherwise these function must be return -1

class DebitCard:
    def __init__(self, name, pin, balance):
        self.__name = name
        self.__isAuthorized = False
        self.__pin = pin
        self.__balance = balance
    def authorize(self, pin):
        self.__isAuthorized = self.__pin == pin
        return self.__isAuthorized
    def withdrawal(self, money_amount):
        if self.__isAuthorized and (self.__balance >= money_amount):
            self.__balance -= money_amount
            return self.__balance
        else:
            return -1
    def getBalance(self):
        return self.__balance if self.__isAuthorized else -1
    
x = DebitCard("Simple tester",1234,100)
print(x.getBalance())
print(x.withdrawal(10))
print(x.authorize(555))
print(x.getBalance())
print(x.withdrawal(10))
print(x.authorize(1234))
print(x.getBalance())
print(x.withdrawal(200))
print(x.withdrawal(50))
print(x.getBalance())
