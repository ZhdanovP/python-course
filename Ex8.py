class DebitCard:
    def __init__(self, name, pin, balance):
        self.__name = name
        self.__pin = pin
        self.__balance = balance
        self.__authorized = False
    def authorize(pin):
        if self.__pin == pin:
            return True
            self.__authorized = True
        else:
            return False
            self.__authorized = False
    def Withdrawal(money):
        if self.__authorized == True and self.__balance-money>=0:
            self.__balance -= money
            return True
        else:
            return -1
    def GetBalance():
        if self.__authorized == True:
            return self.__balance
        else:
            return -1
