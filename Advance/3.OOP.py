class Person:
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        print('name is %s' % self.name)

    def get_birthday(self):
        self.age += 1
        print('birthday is %s' % self.age)


ali = Person('Ali', 22)

ali.get_name()
ali.get_birthday()


class Computer:
    def __init__(self, ram, hard, cpu):
        self.ram = ram
        self.hard = hard
        self.cpu = cpu

    def value(self):
        print('ram is %s' % self.ram)


class Labtop(Computer):
    def __init__(self, ram, hard, cpu, screen):
        Computer.__init__(self, ram, hard, cpu)
        self.screen = screen


pc1 = Computer(8, 'ssd', 'i7')
pc1.value()
