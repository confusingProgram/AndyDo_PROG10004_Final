class Product:
    def __init__(self, product_code, name, category, unit_price, quantity):
        self._product_code = product_code
        self._name = name
        self._category = category
        self._unit_price = float(unit_price)
        self._quantity = int(quantity)
    
    def get_product_code(self):
        return self._product_code
    
    def set_category(self, new_cat):
        try:
            if new_cat == "":
                print("New category shall not be blank.")
                raise ValueError
            if new_cat.isalpha() == False:
                print("New category shall only contain alphabet characters.")
                raise ValueError
        except ValueError as e:
            print("")
            pass

    def net_price(self):
        sub_total = self._unit_price*self._quantity
        total = sub_total * 1.135
        return total
    
    def __str__(self):
        return f"{self._product_code}, {self._name}, {self._category}, {self.net_price()}"
        #230, Dell, Computer, 7661.25
        pass

