

class User:
      name = "No Name Provided"
      email = " "
      password = "password123"
      reciept_number = 10


class Customer(User):
      area = "Retail", "Diner"
      phone_reward = " "

class Employee(User):
      address = " "
      pay_rate = 15.00
      

"""
class Math:
      def __init__(self, x, y):
            self.x = x
            self.y = y
      def add(self):
            return self.x + self.y
      def subtract(self):
            return self.x - self.y

class Math2:
      def __init__(self, x, y):
            self.x = x
            self.y = y
      def multiply(self):
            return self.x * self.y
      def divide(self):
            return self.x / self.y
