class humans:
    def eat(self):
        print('humans are eating')

class boys(humans):
    def eat(self):
        super().eat()
        print("boys are eating rice")


h = boys()
h.eat()
