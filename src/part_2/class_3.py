class MoneyBox:
    def __init__(self, capacity):
        self.capacity = 0
        self.max_cap = capacity

    def can_add(self, v):
        if self.max_cap <= (self.capacity + v):
            return True
        else:
            return False

    def add(self, v):
        self.capacity += v

x = MoneyBox (150)
print(x.can_add(149))
print(x.can_add(151))