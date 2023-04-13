# pylint: disable= missing-docstring


class Product:
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    def __str__(self) -> str:
        return f"Product name: {self.name} price is {self.price}"

    def __repr__(self) -> str:
        return f"Product({self.name}, {self.price})."


this_product = Product(name="Alus", price=1.99)
print(this_product)
print(repr(this_product))
