class Customer(object):
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget

    def purchased(self, model, price):
        self.model = model
        self.price = price
        self.budget = (self.budget - self.price)
        print('I purchased %s for %s and my remaining budget is %s') % (self.model, self.price, self.budget)

    def __repr__(self):
        return'[%s, %s]' % (self.name, self.budget)