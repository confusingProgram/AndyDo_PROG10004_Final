import product
from product import Product
import data_persistence
from data_persistence import DataPersistence


class Manager:
    def __init__(self):
        self._products = []
        self._file = DataPersistence()
        for row in self._file._read_data:
            self._products.append(Product(row['Code'], row['Name'], row['type'],
                                      row['Price per Item'], row['Quantity']))
        pass

    def total_revenue(self):
        sum = 0.0
        for prod in self._products:
            sum = sum + prod.net_price()
        return sum
    
    def add_product(self, product_code, name, category, unit_price, quantity):
        self._products.append(Product(product_code, name, category, unit_price, quantity))

    


    