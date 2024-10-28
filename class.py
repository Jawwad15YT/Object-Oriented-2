class coffee():
    def __init__(self,milk,sugar,coffee_beans):
        self.milk = milk
        self.sugar = sugar
        self.coffee_beans = coffee_beans



Cappucino = coffee("50%","25%","25%")
latte = coffee("25%","10%","65%")

print(Cappucino.milk)
print(latte.coffee_beans)
        