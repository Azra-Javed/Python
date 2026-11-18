class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real,"+", self.img, "i")

    def __add__(self,num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)

    def __sub__ (self, num2):
        newReal = self.real- num2.real
        newImg = self.img - num2.img
        return Complex(newReal, newImg)

num1 = Complex(1,3)
num1.showNumber()

num2 = Complex(4,6)
num2.showNumber()

num3 = num1 + num2
num3.showNumber()

class Employee:

    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary

    def showDetails(self):
        print("role: ", self.role)
        print("salary: ", self.salary)
        print("department: ", self.department)


class Engineer(Employee):
    def __init__(self, role, department, salary, name, age):
        self.name = name
        self.age = age
        super().__init__(role, department, salary)

    def showDetails(self):
            super().showDetails()
            print("name: ", self.name)
            print("age: ", self.age)
    

e1 = Engineer("engineer", "IT", 45566, "AZRa", 21)

e1.showDetails()


class Order:
     def __init__(self, item, price):
          self.item = item
          self.price = price

     def __gt__(self, order2):
      return self.price > order2.price

order1 = Order("chips", 50)
order2 = Order("chips", 30)

print(order1 > order2)