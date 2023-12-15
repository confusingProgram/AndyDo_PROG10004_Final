import product
from product import Product
import data_persistence
from data_persistence import DataPersistence


class Manager:
    def __init__(self):
        self._products = []
        self.get_data()
        

    def get_products(self):
        return self._products
    def total_revenue(self):
        sum = 0.0
        for prod in self._products:
            sum = sum + prod.net_price()
        return sum
    
    def add_product(self, product_code, name, category, unit_price, quantity):
        self._products.append(Product(product_code, name, category, unit_price, quantity))

    def list_of_codes(self):
        list = []
        for prod in self._products:
            list.append(prod.get_product_code())
        return list

    def get_data(self):
        file = DataPersistence()
        for row in file._read_data:
            self._products.append(Product(row['Code'], row['Name'], row['type'],
                                      row['Price per Item'], row['Quantity']))

    


    