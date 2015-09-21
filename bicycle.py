
class Bicycle(object):
    def __init__(self, name, weight, cost):
        self.name = name
        self.weight = weight
        self.cost = cost
        return None
    def __repr__(self):
        return '[ %s, %s, %s]' % (self.name, self.weight, self.cost)

if __name__=='__main__':
    model001 = Bicycle('Model001', '5lbs', 400)
    print(model001)