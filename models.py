class Product:
    def __init__(self, name, unit, unit_price, quantity):
        self.name = name
        self.unit = unit
        self.unit_price = unit_price
        self.quantity = quantity
        self.products = [self]

def product_create(data):
    data.pop("csrf_token")
    item = Product(name=data["name"], unit = data["unit"], unit_price = data["unit_price"], quantity = data["quantity"])
    return item
