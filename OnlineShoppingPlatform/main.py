from product import Clothing, Electronics
from customer import Customer

def main():
    #create Customer and Product instances
    customer = Customer('Serob', 'serob@gmail.com')
    product1 = Electronics('Laptop', 2100, '500 GB SSD, 16 GB RAM')
    product2 = Clothing('Jeans', 49.99, 'High quality material')

    #purchase products, view order history
    customer.purchase_product([product1, product2])
    customer.view_history()
    customer.leave_review(product1, 'Perfect performance')
    customer.leave_review(product2, 'Material was not that a good quality')

if __name__ == '__main__':
    main()
