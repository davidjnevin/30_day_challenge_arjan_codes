from dataclasses import dataclass, field
from decimal import Decimal


class ItemNotFoundException(Exception):
    pass

@dataclass
class Item:
    name: str
    price: Decimal
    quantity: int

    # Add convenience methods to the Item class
    # to make it easier to update the quantity and price
    # of an item.
    # These methods are now the direct collaborators of
    # the Item class, and the main function can use them
    # to update the quantity and price of an item.
    # This way, the main function doesn't need to know
    # the internals of the Item class.
    def update_price(self, new_price: Decimal) -> None:
        self.price = new_price

    def update_quantity(self, new_quantity: int) -> None:
        self.quantity = new_quantity

    @property
    def subtotal(self) -> Decimal:
        return self.price * self.quantity


@dataclass
class ShoppingCart:
    # defines an attribute named items in a class,
    # which is expected to be a list of Item objects.
    # If no explicit value is assigned to items,
    # it will be initialized with an empty list by default.
    items: list[Item] = field(default_factory=list)
    discount_code: str | None = None

    # Add convenience methods to the ShoppingCart class
    # to make it easier to add and remove items from the cart.
    # These methods are now the direct collaborators of
    # the ShoppingCart class, and the main function can use them
    # to add and remove items from the cart.
    # This way, the main function doesn't need to know
    # the internals of the ShoppingCart class.
    # Add an item to the cart
    def add_item(self, item: Item) -> None:
        self.items.append(item)

    # Remove an item from the cart
    def remove_item(self, item_name: str) -> None:
        found_item = self.find_item_by_name(item_name)
        if found_item:
            self.items.remove(found_item)
        else:
            raise ItemNotFoundException(f"Item '{item_name}' not found.")

    def find_item_by_name(self, item_name: str) -> Item | None:
        for item in self.items:
            if item.name == item_name:
                return item
        return None

    @property
    def total(self) -> Decimal:
        return Decimal(sum(item.subtotal for item in self.items))

    def display(self) -> None:
        print("Shopping Cart:")
        print(f"{'Item':<10}{'Price':>10}{'Qty':>7}{'Total':>13}")
        for item in self.items:
            print(
                f"{item.name:<12}${item.price:>7.2f}{item.quantity:>7}     ${item.subtotal:>7.2f}"
            )
        print("=" * 40)
        print(f"Total: ${self.total:>7.2f}")

    def update_item_quantity(self, item_name: str, updated_quantity: int) -> None:
        found_item = self.find_item_by_name(item_name)
        if found_item:
            found_item.update_quantity(updated_quantity)
        else:
            raise ItemNotFoundException(f"Item '{item_name}' not found.")

    def update_item_price(self, item_name: str, updated_price: Decimal) -> None:
        found_item = self.find_item_by_name(item_name)
        if found_item:
            found_item.update_price(updated_price)
        else:
            raise ItemNotFoundException(f"Item '{item_name}' not found.")


def main() -> None:
    # Create a shopping cart and add some items to it
    cart = ShoppingCart(
        items=[
            Item("Apple", Decimal("1.5"), 10),
            Item("Banana", Decimal("2"), 2),
            Item("Pizza", Decimal("11.90"), 5),
        ],
    )


    # Violation Number 1:

    # The main function directly accesses and modifies the quantity
    # and price attributes of the Item objects in the cart.items list.
    # This violates the Law of Demeter because it involves accessing
    # the internals of objects that are not direct collaborators of
    # the ShoppingCart class.

    # Update some items' quantity and price
    # cart.items[0].quantity = 10
    # cart.items[2].price = Decimal("3.50")
    # Solution 1:
    cart.update_item_quantity("Apple", 10)
    cart.update_item_price("Pizza", Decimal("3.50"))


    # Violation Number 2:

    # The main function directly removes an item from the cart.items list.
    # Again, this violates the Law of Demeter as it exposes the internal
    # structure of the ShoppingCart class by allowing direct manipulation of its items.
    # Remove an item
    # cart.items.remove(cart.items[1])
    # total = sum(item.price * item.quantity for item in cart.items)
    # Solution 2.
    cart.remove_item("Banana")

    # Print the cart
    # Violation Number 3:

    # The main function directly accesses the name, price, and quantity
    # attributes of the Item objects in the cart.items list.
    # This violates the Law of Demeter because it involves accessing
    # the internals of objects that are not direct collaborators of
    # the ShoppingCart class.
    # Solution 3
    cart.display()

    # Main now has no idea of teh inner workings of ShoppingCart and Item.


if __name__ == "__main__":
    main()
