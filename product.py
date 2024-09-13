class Product:
    def __init__(self, name, price):
        self._productName = name
        self._productPrice = price

    # Property for productName
    @property
    def productName(self):
        return self._productName

    @productName.setter
    def productName(self, name):
        self._productName = name

    # Property for productPrice
    @property
    def productPrice(self):
        return self._productPrice

    @productPrice.setter
    def productPrice(self, price):
        self._productPrice = price

    def __str__(self):
        return f"Product(name={self._productName}, price={self._productPrice})"
