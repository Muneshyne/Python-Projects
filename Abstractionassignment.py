


from abc import ABC, abstractmethod
class Mortgage(ABC):
      def pay(self, amount):
            print("Your savings account balance is: ",amount)
#this function is telling us to pass in an argument.

            @abstractmethod
            def payment(self, amount):
                  pass

class HomePayment(Mortgage):
#here we've defined how to implement the payment function from its parent paySlip class.
      def payment(self, amount):
            print('Your overdue mortgage payment due is {} '.format(amount)) #needs wildcard to show format(amount)

obj = HomePayment()
obj.pay("$1400")
obj.payment("$1200")


"""
Abstraction is useful for working on much larger projects when child classes may need to
utilize implementation of methods differently from its parent class and other child classes that inherit from the same parent.
Think of it like this:  You have one parent class of Payment, then child classes need to run different payment options separately from each other,
such as Debit, Credit, Gift card, etc.
They all take a payment from the customer, but each process needs to be different according to how the banks process them.
"""
