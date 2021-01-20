class CoffeeMachine():
    water = 400
    milk = 540
    coffe_beans = 120
    cups = 9
    money = 550
    mode = 'default'


    def UI(self, string):
        if self.mode == 'default':
            self.default_method(string)
        elif self.mode == "buy":
            self.buy(string)
        elif self.mode == "fill":
            self.fill(string)
        elif self.mode == 'fill_water':
            self.fill_water(string)
        elif self.mode == 'fill_milk':
            self.fill_milk(string)
        elif self.mode == 'fill_beans':
            self.fill_beans(string)
        elif self.mode == 'fill_cups':
            self.fill_cups(string)

    def default_method(self, string):
        if string == "buy":
            self.mode = string
            self.UI('')
        elif string == "fill":
            self.mode = string
            self.UI('')
        elif string == "take":
            print("\n I gave you $"+ str(self.money)+"\n")
            self.money = 0
            self.UI('')
        elif string == "remaining":
            self.status()
            self.UI('')
        elif string == "exit":
            print('Closing')
        else:
             print("Write action (buy, fill, take, remaining, exit): ")

    def fill(self, string):
        print("\nWrite how many ml of water do you want to add:")
        self.mode = "fill_water"

    def fill_water(self, water):
        self.water += int(water)
        print("Write how many ml of milk do you want to add:")
        self.mode = "fill_milk"

    def fill_milk(self, milk):
        self.milk += int(milk)
        print("Write how many grams of coffee beans do you want to add:")
        self.mode = "fill_beans"

    def fill_beans(self, beans):
        self.coffe_beans += int(beans)
        print("Write how many disposable cups of coffee do you want to add:")
        self.mode = "fill_cups"

    def fill_cups(self, cups):
        self.cups += int(cups)
        self.mode = "default"
        self.UI('')

    def status(self):
        print("\nThe coffee machine has:\n{0} of water\n{1} of milk\n{2} of coffee beans\n{3} of disposable cups\n"
            "${4} of money\n".format(self.water, self.milk, self.coffe_beans, self.cups, self.money))

    def buy(self, what):
        if what == '':
            print("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu : ")
        if what is not '':
            if what == '1':
                need_w = 250
                need_mi = 0
                need_b = 16
                cost = 4
            elif what == '2':
                need_w = 350
                need_mi = 75
                need_b = 20
                cost = 7
            elif what == '3':
                need_w = 200
                need_mi = 100
                need_b = 12
                cost = 6
            elif what == 'back':
                self.mode = 'default'
                print("\n")
                self.UI('')
                return
            if all([self.water >= need_w, self.milk >= need_mi, self.coffe_beans >= need_b, self.cups >= 1]):
                self.water -= need_w
                self.milk -= need_mi
                self.coffe_beans -= need_b
                self.money += cost
                self.cups -= 1
                print("I have enough resources, making you a coffee!\n")
            else:
                if self.water < need_w:
                    missing = 'water'
                elif self.milk < need_mi:
                    missing = "milk"
                elif self.coffe_beans < need_b:
                    missing = "coffe_beans"
                else:
                    missing = "cups"
                print("Sorry, not enough " + missing+"!\n")
            self.mode = 'default'
            self.UI('')



test = CoffeeMachine()
user_input = ''
while user_input != 'exit':
    test.UI(user_input)
    user_input = input()

