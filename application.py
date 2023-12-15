# Name: Andy Do
# Student Number: 991724830

import manager
from manager import Manager

class Application:
    def __init__(self):
        self._product_manager = Manager()
        pass

    def show_main_menu(self):
        while True:
            print("")
            print("1. Display All Products")
            print("2. Display Product By Type")
            print("3. Display Total Revenue")
            print("4. Add New Product")
            print("5. Exit Application")
            choice = input("Enter a number: ")
            if choice == "1":
                for prod in self._product_manager.get_products():
                    print(prod)
            elif choice == "2":
                type = input("Enter the product type: ").strip().upper()
                printed = 0
                for prod in self._product_manager.get_products():
                    if prod.get_category().upper() == type:
                        print(prod)
                        printed = printed + 1
                if printed == 0:
                    print(f"No items found.")
            elif choice == "3":
                print(f"Total Revenue: ${self._product_manager.total_revenue()}")
            elif choice == "4":
    #def add_product(self, product_code, name, category, unit_price, quantity):

                exit = False
                code = ""
                name = ""
                cat = ""
                u_p = ""
                quant = ""
                while True:
                    code = input("Enter code (numbers only, type EXIT to exit): ").strip()
                    if code.isdigit() == False or len(code) == 0:
                        if code.upper() == "EXIT":
                            exit = True
                        else:
                            print("Invalid code number.")
                            continue
                    ref = self._product_manager.list_of_codes()
                    if code in ref:
                        print("Code number already exists.")
                        continue
                    break
                if exit:
                    continue

                while True:
                    name = input("Enter name (type EXIT to exit): ").strip()
                    if name.upper() == "EXIT":
                        exit = True
                    elif len(name) == 0 or name == "":
                        print("Name cannot be void.")
                        continue
                    break
                if exit:
                    continue

                while True:
                    cat = input("Enter category (type EXIT to exit): ").strip()
                    if cat.upper() == "EXIT":
                        exit = True
                    elif len(cat) == 0 or cat.isalpha() == False:
                        print("Invalid category type.")
                        continue
                    break
                if exit:
                    continue

                while True:
                    u_p = input("Enter unit price (type EXIT to exit): ").strip()
                    if u_p.upper() == "EXIT":
                        exit = True
                    elif len(u_p) == 0:
                        print("Invalid category type.")
                        continue

                    if "." in u_p:
                        array = u_p.split('.')
                        if array[0].isdigit() == False:
                            print("Enter numbers only.")
                            continue
                        elif array[1].isdigit() == False:
                            print("Enter numbers only.")
                            continue
                        elif len(array[1]) > 2:
                            print("Limit to 2 decimal places.")
                            continue
                    else:
                        if u_p.isdigit() == False and u_p.upper() != "EXIT":
                            print("Enter numbers only.")
                            continue
                    break
                if exit:
                    continue

                while True:
                    quant = input("Enter quantity of items (integers only, type EXIT to exit): ").strip()
                    if quant.upper() == "EXIT":
                        exit = True
                        break
                    elif len(quant) == 0:
                        print("Number must not be empty.")
                        continue
                    elif quant.isdigit() == False:
                        print("Enter numbers only.")
                        continue
                    else:
                        try:
                            num_val = int(quant)
                            if num_val == 0:
                                raise Exception
                        except Exception as e:
                            print("Quantity cannot be 0.")
                            continue
                        break
                if exit:
                    continue
                self._product_manager.add_product(code, name, cat, float(u_p), int(quant))
            elif choice == "5":
                print("Thank you for using our service.")
                break 
                

            

    def run(self):
        self.show_main_menu()

app1 = Application()
app1.run()