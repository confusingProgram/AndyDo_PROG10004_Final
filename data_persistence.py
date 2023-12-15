import csv

class DataPersistence:
    def __init__(self):
        self._read_data = []
        with open('products_sales.csv', 'r') as f:
            for row in csv.DictReader(f):
                self._read_data.append(row)