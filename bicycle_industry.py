import bicycle
import customer
import bikeshop

def WithinBudget(bikeshop, budget):
    models = []
    for bikes in bikeshop.inventory:
        if int(budget) >= int(bikeshop.add_margins(bikes.cost)):
            models.append([bikes.name, bikes.cost])
    return(models)

def Build_A_Bikeshop(shop):
    inventory = []
    model001 = bicycle.Bicycle('Model001', '6lbs', 300.00)
    model002 = bicycle.Bicycle('Model002', '5lbs', 400.00)
    model003 = bicycle.Bicycle('Model003', '4lbs', 500.00)
    model004 = bicycle.Bicycle('Model004', '3lbs', 600.00)
    model005 = bicycle.Bicycle('Model005', '2lbs', 700.00)
    model006 = bicycle.Bicycle('Model006', '1lbs', 800.00)

    inventory =   [
        model001, model002, model003, model004, model005, model006
    ]

    return(bikeshop.Bikeshop(shop, inventory))

if __name__=='__main__':
    
    PerformanceBicycle = Build_A_Bikeshop('Performance Bicycle')    
    print('Welcome to %s, today we have the following in stock: %s') % (PerformanceBicycle.name, PerformanceBicycle.inventory)
    
    """Build three customers"""
    customers = []
    Customer1 = customer.Customer('Customer1', 500.00)
    Customer2 = customer.Customer('Customer2', 700.00)
    Customer3 = customer.Customer('Customer3', 1000.00)
    
    customers = [ 
        Customer1, Customer2, Customer3
    ]
         
    for customer in customers:
        BikesinBudget = WithinBudget(PerformanceBicycle, customer.budget)
        print('%s , You can afford the following bikes: %s') % (customer.name, BikesinBudget)
        ans = raw_input('Which would you like to purchase?')
        for bikes in PerformanceBicycle.inventory:
            if ans == bikes.name:
                customer.purchased(bikes.name, PerformanceBicycle.add_margins(bikes.cost))
                PerformanceBicycle.sell(bikes.name)
    print('Our remaining inventory is: %s') % (PerformanceBicycle.inventory)
    print('Our profit for the day is: %s') % (PerformanceBicycle.profit)
