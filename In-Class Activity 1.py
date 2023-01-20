#  File: In-Class Activity 1.py

#  Description: This program implements an application that controls a "Fully Automatic Beverage Vending Machine”. 

#  student Name: Gaytri Riya Vasal

#  Student UT EID: grv377

#  Course Name: CS 313E

#  Unique Number: 86439

#  Date Created: 6/8/2022

#  Date Last Modified: 6/10/2022

class Beverage:

    def __repr__(self):
        return ""

class Coffee(Beverage):

    def __init__(self, coffee):
        self.coffee = coffee

    def __repr__(self):
        return ""

class Expresso(Coffee):
        
    def __repr__(self):
        return "Expresso"
    
class Americano(Coffee):

    def __repr__(self):
        return "Americano"
    
class LatteMacchiato(Coffee):

    def __repr__(self):
        return "Latte Macchiato"

class Tea(Beverage):

    def __init__(self, tea):
        self.tea = tea

    def __repr__(self):
        return ""

class Black(Tea):

    def __repr__(self):
        return "Black Tea"

class Green(Tea):

    def __repr__(self):
        return "Green Tea"

class Yellow(Tea):

    def __repr__(self):
        return "Yellow Tea"

class Condiments():

    def __init__ (self, units):
        self.units = units
        
    def __repr__ (self):
        return str(self.units)

class Milk(Condiments):

    def __init__ (self, units):
        self.units = units

    def __repr__(self):
        return str(self.units) + " unit(s) of milk"

class Sugar(Condiments):

    def __init__ (self, units):
        self.units = units

    def __repr__(self):
        return str(self.units) + " unit(s) of sugar"

class VendingMachineController():

    def __init__(self):

        while (True):
            self.sort = ""
            self.milk = "0 unit(s) of milk"
            self.sugar = "0 unit(s) of sugar"
            
            beverage = input("Select a beverage: \n1. Coffee \n2. Tea \n")

            if beverage == "1":
                sort = input("Select an option: \n1. Expresso \n2. Americano \n3. Latte Macchiato\n")
                if sort == "1":
                    self.sort = Expresso(Coffee(Beverage))
                elif sort == "2":
                    self.sort = Americano(Coffee(Beverage))
                elif sort == "3":
                    self.sort = LatteMacchiato(Coffee(Beverage))
                    
            elif beverage == "2":
                sort = input("Select an option: \n1. Black \n2. Green \n3. Yellow\n")
                if sort == "1":
                    self.sort = Black(Tea(Beverage))
                elif sort == "2":
                    self.sort = Green(Tea(Beverage))
                elif sort == "3":
                    self.sort = Yellow(Tea(Beverage))

            condiments = input("Which condiment would you like? \n1. None \n2. Milk \n3. Sugar\n")

            if condiments == "2":
                units = int(input("How many units would you want?\n"))
                while units > 3:
                    units = int(input("More than 3 cumulative units are not allowed. Please try again: How many units would you want?\n"))
                self.milk = Milk(Condiments(units))
                if units != 3:
                    condiments = input("Would you like sugar as well? 1. Yes 2. No\n")
                    if condiments == "1":
                        moreunits = int(input("How many units would you want?\n"))
                        while units + moreunits > 3:
                            moreunits = int(input("More than 3 cumulative units are not allowed. Please try again: How many units would you want?\n"))
                        self.sugar = Sugar(Condiments(moreunits))
                        print(self.sort, "+", self.milk, "+", self.sugar)
                    else:
                        print(self.sort, "+", self.milk, "+", self.sugar)
                else:
                    print(self.sort, "+", self.milk, "+", self.sugar)
                            
            elif condiments == "3":
                units = int(input("How many units would you want?\n"))
                while units > 3:
                    units = int(input("More than 3 cumulative units are not allowed. Please try again: How many units would you want?\n"))
                self.sugar = Sugar(Condiments(units))
                if units != 3:
                    condiments = input("Would you like milk as well? 1. Yes 2. No\n")
                    if condiments == "1":
                        moreunits = int(input("How many units would you want?\n"))
                        while units + moreunits > 3:
                            moreunits = int(input("More than 3 cumulative units are not allowed. Please try again: How many units would you want?\n"))
                        self.milk = Milk(Condiments(moreunits))
                        print(self.sort, "+", self.milk, "+", self.sugar)
                    else:
                        print(self.sort, "+", self.milk, "+", self.sugar)
                else:
                    print(self.sort, "+", self.milk, "+", self.sugar) 

            else:
                print(self.sort, "+", self.milk, "+", self.sugar)
            
def main():

    print(VendingMachineController())

main()
