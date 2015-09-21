import bicycle

class Bikeshop(object):
    def __init__(self, name, inventory):
        self.name = name
        self.inventory = inventory
        self.profit = 0

    def add_margins(self, mcost):
        self.mcost = mcost
        mcost *= 1.20
        return mcost

    def __str__(self):
        return '[%s]' % (self.inventory)              

    def sell(self, model):
        self.model = model
        for bikes in self.inventory:
            if self.model == bikes.name:
               self.profit = self.profit + ((self.add_margins(bikes.cost)) - bikes.cost) 
               self.inventory.remove(bikes)
        return(self.inventory, self.profit)

if __name__ == '__main__':
    inventory = []
    model001 = bicycle.Bicycle('Model001', '6lbs', 400.00)
    model002 = bicycle.Bicycle('Model002', '5lbs', 500.00)
    inventory = [
        model001, model002
    ]
    PerformanceBicycle = Bikeshop('Performance Bicycle', inventory)
    PerformanceBicycle.sell(PerformanceBicycle.inventory[1].name)        
    print(PerformanceBicycle.inventory, PerformanceBicycle.profit)