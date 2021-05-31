


from abc import ABC, abstractmethod
class car(ABC):
      def paySlip(self, amount):
            print("Your purchase amount: ",amount)
#this function is telling us to pass in an argument, but we won't tell you how or what kind
#of data it will be.
            @abstractmethod
            def payment(self, amount):
                  pass

class DebitCardPayment(car):
#here we've defined how to implement the payment function from its parent paySlip class.
      def payment(self, amount):
            print('Your purchase amount of {} exceeded your $100 limit '.format(amount))

obj = DebitCardPayment()
obj.paySlip("$400")
obj.payment("$400")


"""
Abstraction is useful for working on much larger projects when child classes may need to
utilize implementation of methods differently from its parent class and other child classes that inherit from the same parent.
Think of it like this:  You have one parent class of Payment, then child classes need to run different payment options separately from each other,
such as Debit, Credit, Gift card, etc.
They all take a payment from the customer, but each process needs to be different according to how the banks process them.
"""
