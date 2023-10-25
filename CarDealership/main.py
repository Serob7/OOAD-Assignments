from customer import Customer
from salesman import CarInventory, Salesman
from car import ElectricCar, HybridCar

def main():
    #Creating Car instances
    electric1 = ElectricCar('Tesla', 'Model S', 90000)
    hybrid = HybridCar('Kia', 'Optima', 45000)

    #creating CarInventory instance
    inventory = CarInventory('My inventory')

    #creating Salesman instance
    salesman = Salesman('Serob', 3.5)

    #Adding cars to inventory
    salesman.add_car(electric1, inventory)
    salesman.add_car(hybrid, inventory)

    #Viewing inventory
    print('Car Inventory')
    salesman.view_car_inventory(inventory)
    print('\n')

    #creating customer instance and purchasing car
    customer1 = Customer('John', 'john@gmail.com')
    customer1.purchase_car(inventory, electric1, salesman)
    print('\n')

    #View salesman's history and salary
    print("Salesman's history")
    salesman.view_sale_history()
    print(f"Salesman's salary: ${salesman.salary}")

if __name__ == '__main__':
    main()




