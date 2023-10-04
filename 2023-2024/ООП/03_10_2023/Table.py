class Table:
    def __init__(self, l, wi, h, we):
        self.long = l
        self.width = wi
        self.height = h
        self.weight = we

    def outing(self):
        print(self.long, self.width, self.height)


class Worker(Table):
    def is_raise(self):
        if self.weight > 50 or self.long > 3:
            return "I need help"
        else:
            return 'Where should i take it?'

    def is_passed(self):
        if self.width > 2 and self.height > 3:
            return "will not fit"
        else:
            return 'Where should i take it?'


worker1 = Worker(1, 1, 1, 100)
worker2 = Worker(3, 2, 3, 50)
print(worker1.is_raise())
print(worker2.is_passed())
