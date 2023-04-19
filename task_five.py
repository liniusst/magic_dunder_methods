# pylint: disable= missing-docstring
from dataclasses import dataclass
from typing import Optional


@dataclass
class Product:
    id: int
    name: str
    description: str
    price: float
    quantity_in_stock: int

    def calculate_total_cost(self, given_number: Optional[int] = None):
        if given_number <= 0:
            return 0.0
        elif given_number > self.quantity_in_stock:
            return self.quantity_in_stock * self.price
        else:
            return given_number * self.price


product_one = Product(111, "iphone 11", "64gb black", 429, 2)
total_sum = product_one.calculate_total_cost()
print(total_sum)
