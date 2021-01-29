"""
* Implement DebitCard model. You must implementing following operation:
    - authorize(pin) -> bool
    - Withdrawal(money) ->  int
    - GetBalance() -> int
* These operations must be return correct result if user call authorize() before
* Otherwise these function must be return -1
* For example, following main code

```
x = DebitCard('Simple tester',1234,100)
print(x.GetBalance())
print(x.Withdrawal(10))
print(x.Authorize(555))
print(x.GetBalance())
print(x.Withdrawal(10))
print(x.Authorize(1234))
print(x.GetBalance())
print(x.Withdrawal(200))
print(x.Withdrawal(50))
print(x.GetBalance())
"""

class DebitCard:
    def __init__(self, name, pin, money):
        self.name = name
        self.pin = pin
        self.money = money
        self.__is_authorized = False

    def authorize (self,entered_pin):
        if entered_pin == self.pin:
            self.__is_authorized = True
        return self.__is_authorized

    def getBalance(self):
        if self.__is_authorized == True:
            return self.money
        else:
            return -1

    def withdrawal(self, sum):
        if self.__is_authorized == True:
            if self.money >= sum:
                self.money -= sum
                return self.money
            else:
                return -1
        else:
            return -1


x = DebitCard('Simple tester',1234,100)


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