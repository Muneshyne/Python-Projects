

class ProtectVar:
      def __init__(self):
                  self.protectedVar = 1

obj = ProtectVar()
obj._protectedVar = 32
print(obj._protectedVar)
# with a protected var its set to not be used outside of this class






class Protected:
      def __init__(self):
            self.__privateVar = 16 #double underscores make it private

      def getPrivate(self):
            print(self.__privateVar) #prints the original variable

      def setPrivate(self, private):
            self.__privateVar = private

obj = Protected()
obj.getPrivate()
obj.setPrivate(45) #sets new var
obj.getPrivate()
