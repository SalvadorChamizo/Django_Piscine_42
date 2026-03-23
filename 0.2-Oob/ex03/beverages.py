class HotBeverage:
    def __init__(self):
        self.name = "hot beverage"
        self.price = 0.30

    def description(self):
        return "Just some hot water in a cup."

    def __str__(self):
        return f"name : {self.name}\n" \
                f"price : {self.price}\n" \
                f"description : {self.description()}"


class Coffee(HotBeverage):
    def __init__(self):
        self.name = "coffee"
        self.price = 0.40

    def description(self):
        return "A coffee, to stay awake."


class Tea(HotBeverage):
    def __init__(self):
        self.name = "tea"
        self.price = 0.30


class Chocolate(HotBeverage):
    def __init__(self):
        self.name = "chocolate"
        self.price = 0.50

    def description(self):
        return "Chocolate, sweet chocolate..."


class Cappuccino(HotBeverage):
    def __init__(self):
        self.name = "cappuccino"
        self.price = 0.45

    def description(self):
        return "Un po´ di Italia nella sua tazza!"


if __name__ == "__main__":
    drinks = [HotBeverage(), Coffee(), Tea(), Chocolate(), Cappuccino()]

    for drink in drinks:
        print(drink)
        print()
