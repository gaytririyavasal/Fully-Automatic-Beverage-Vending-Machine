
PROJECT DESCRIPTION AND GUIDELINES PROVIDED ON ASSIGNMENT INSTRUCTIONS

In this activity, you will implement an application that controls a “Fully Automatic Beverage Vending Machine”. 

Your task is to implement the controller software of this machine.

The software should be able to control the brewing process of fresh coffee and tea beverages.

The machine should be able to

- Brew Coffee sorts of Espresso, Americano, Latte Macchiato, and
- Make Tea sorts of Black Tea, Green Tea, and Yellow Tea.
- Add condiments like milk and sugar to the hot beverage. 

Requirements:

- When the machine starts up and is initiated, it shows a request question and asks users about their beverage wishes.
- After each brewing process, the state of the beverage machine should return to the same initial state and display the request question to ask users again.
- As an additional requirement, the coffee machine should be able to add condiments like milk and sugar to the hot beverage. Users of the machine should be able to select between zero to 3 units of milk or sugar to add. The vending machine should not allow over 3 units of condiments. 

Implementation Details:

- Define classes for Espresso, Americano, Latte Macchiato, and Black Tea, Green Tea, and Yellow Tea. Think about building inheritance. 
- Define classes for Condiments like Milk and Sugar 
- Define a class for the vending machine's main controller
- Define the main function that gets the input from the user and prints it out to the standard output.  
