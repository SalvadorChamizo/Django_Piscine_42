import random
import beverages


class CoffeeMachine:

    class EmptyCup(beverages.HotBeverage):
        def __init__(self):
            super().__init__()
            self.name = "empty cup"
            self.price = 0.90

        def description(self):
            return "An empty cup?! Gimme my money back!"

    class BrokenMachineException(Exception):
        def __init__(self):
            super().__init__("This coffee machine has to be repaired.")

    def __init__(self):
        self.counter = 10

    def repair(self):
        self.counter = 10

    def serve(self, drink_class):
        self.counter -= 1

        if self.counter < 0:
            raise self.BrokenMachineException()

        if random.choice([True, False]):
            return drink_class()
        else:
            return self.EmptyCup()


if __name__ == '__main__':

    drinks = [
        beverages.HotBeverage,
        beverages.Coffee,
        beverages.Tea,
        beverages.Chocolate,
        beverages.Cappuccino
    ]

    coffeeMachine = CoffeeMachine()

    for drink in drinks:
        cup = coffeeMachine.serve(drink)
        print(cup)
        print()

    for drink in drinks:
        cup = coffeeMachine.serve(drink)
        print(cup)
        print()

    try:
        cup = coffeeMachine.serve(beverages.Coffee)
        print(cup)
        print()
    except Exception as e:
        print(e)
        print()

    coffeeMachine.repair()
    cup = coffeeMachine.serve(beverages.Coffee)
    print(cup)
    print()
