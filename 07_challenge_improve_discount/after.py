from dataclasses import dataclass, field
from decimal import Decimal


class ItemNotFoundException(Exception):
    pass


class DiscountNotFoundException(Exception):
    pass


@dataclass
class Item:
    name: str
    price: Decimal
    quantity: int

    @property
    def subtotal(self) -> Decimal:
        return self.price * self.quantity


@dataclass
class Discount:
    amount: Decimal
    percentage: Decimal


DISCOUNTS = {
    "SAVE10": Discount(amount=Decimal("0"), percentage=Decimal("0.1")),
    "5BUCKSOFF": Discount(amount=Decimal("5.00"), percentage=Decimal("0")),
    "FREESHIPPING": Discount(amount=Decimal("2.00"), percentage=Decimal("0")),
    "BLKFRIDAY": Discount(amount=Decimal("0"), percentage=Decimal("0.2")),
}


@dataclass
class ShoppingCart:
    items: list[Item] = field(default_factory=list)
    discounts: list[str] = field(default_factory=list)

    def add_item(self, item: Item) -> None:
        self.items.append(item)

    def remove_item(self, item_name: str) -> None:
        found_item = self.find_item(item_name)
        self.items.remove(found_item)

    def find_item(self, item_name: str) -> Item:
        for item in self.items:
            if item.name == item_name:
                return item
        raise ItemNotFoundException(f"Item '{item_name}' not found.")

    def apply_discount(self, code: str):
        if not code in DISCOUNTS:
            raise DiscountNotFoundException(f"Discount code {code} is not valid.")
        self.discounts.append(code)

    def remove_discount(self, code: str) -> None:
        try:
            self.discounts.remove(code)
        except ValueError:
            print("That discount cannot be found.")

    @property
    def discount(self) -> Decimal:
        total_discount = Decimal("0")
        for code in self.discounts:
            if code in DISCOUNTS:
                total_discount += DISCOUNTS[code].amount + (DISCOUNTS[code].percentage * self.subtotal)
        return total_discount

    @property
    def subtotal(self) -> Decimal:
        return Decimal(sum(item.subtotal for item in self.items))

    @property
    def total(self) -> Decimal:
        return self.subtotal - self.discount

    def print_cart(self) -> None:
        # Print the cart
        print("Shopping Cart:")
        print(f"{'Item':<10}{'Price':>10}{'Qty':>7}{'Total':>13}")
        for item in self.items:
            print(f"{item.name:<12}${item.price:>7.2f}{item.quantity:>7}     ${item.subtotal:>7.2f}")
        print("=" * 40)
        if self.discount:
            print(f"Subtotal: ${self.subtotal:>7.2f}")
            print(f"Discount: ${self.discount:>7.2f}")
        print(f"Total:    ${self.subtotal:>7.2f}")


def main() -> None:
    # Create a shopping cart and add some items to it
    cart = ShoppingCart(
        items=[
            Item("Apple", Decimal("1.50"), 10),
            Item("Banana", Decimal("2.00"), 2),
            Item("Pizza", Decimal("11.90"), 5),
        ],
    )

    cart.apply_discount("SAVE10")

    cart.print_cart()


if __name__ == "__main__":
    main()
