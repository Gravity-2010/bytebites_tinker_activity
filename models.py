# ByteBites models summary
#
# Customer: stores the customer name and purchase history as a list of Transaction objects.
# FoodItem: represents an item sold by ByteBites with name, price, category, and popularity rating.
# Menu: holds a list of FoodItem objects and provides browsing/filtering by category.
# Transaction: groups selected FoodItem objects together and computes the total order cost.


class FoodItem:
    """Represents a food item available in the ByteBites menu."""
    
    def __init__(self, name: str, price: float, category: str, popularity_rating: int):
        self.name = name
        self.price = price
        self.category = category
        self.popularity_rating = popularity_rating
    
    def get_details(self) -> dict:
        """Returns a dictionary with all item details."""
        return {
            "name": self.name,
            "price": self.price,
            "category": self.category,
            "popularity_rating": self.popularity_rating
        }


class Customer:
    """Represents a customer with name and purchase history."""
    
    def __init__(self, name: str):
        self.name = name
        self.purchase_history = []
    
    def add_transaction(self, tx: 'Transaction') -> None:
        """Adds a transaction to the customer's purchase history."""
        self.purchase_history.append(tx)
    
    def get_purchase_history(self) -> list:
        """Returns the list of transactions in purchase history."""
        return self.purchase_history


class Transaction:
    """Represents a single transaction with multiple food items."""
    
    def __init__(self):
        self.items = []
    
    def add_item(self, item: FoodItem) -> None:
        """Adds a food item to this transaction."""
        self.items.append(item)
    
    def get_items(self) -> list:
        """Returns the list of items in this transaction."""
        return self.items
    
    def total_cost(self) -> float:
        """Calculates and returns the total cost of all items in the transaction."""
        return sum(item.price for item in self.items)


class Menu:
    """Manages the collection of available food items."""
    
    def __init__(self):
        self.items = []
    
    def add_item(self, item: FoodItem) -> None:
        """Adds a food item to the menu."""
        self.items.append(item)
    
    def get_all_items(self) -> list:
        """Returns the list of all items in the menu."""
        return self.items
    
    def filter_by_category(self, category: str) -> list:
        """Returns items matching the specified category."""
        return [item for item in self.items if item.category == category]


# ============================================================================
# Unit Tests
# ============================================================================

def test_fooditem():
    """Test FoodItem class."""
    item = FoodItem("Spicy Burger", 8.99, "Entrees", 4)
    assert item.name == "Spicy Burger"
    assert item.price == 8.99
    assert item.category == "Entrees"
    assert item.popularity_rating == 4
    
    details = item.get_details()
    assert details["name"] == "Spicy Burger"
    assert details["price"] == 8.99
    assert details["category"] == "Entrees"
    assert details["popularity_rating"] == 4
    print("✓ FoodItem tests passed")


def test_customer():
    """Test Customer class."""
    customer = Customer("Alice")
    assert customer.name == "Alice"
    assert customer.purchase_history == []
    
    # Create and add transactions
    tx1 = Transaction()
    tx1.add_item(FoodItem("Burger", 8.99, "Entrees", 4))
    customer.add_transaction(tx1)
    
    assert len(customer.purchase_history) == 1
    assert customer.get_purchase_history()[0] == tx1
    
    tx2 = Transaction()
    tx2.add_item(FoodItem("Soda", 2.50, "Drinks", 3))
    customer.add_transaction(tx2)
    
    assert len(customer.get_purchase_history()) == 2
    print("✓ Customer tests passed")


def test_transaction():
    """Test Transaction class."""
    tx = Transaction()
    assert tx.items == []
    assert tx.total_cost() == 0.0
    
    # Add single item
    burger = FoodItem("Burger", 8.99, "Entrees", 4)
    tx.add_item(burger)
    assert len(tx.get_items()) == 1
    assert tx.total_cost() == 8.99
    
    # Add multiple items
    soda = FoodItem("Soda", 2.50, "Drinks", 3)
    tx.add_item(soda)
    assert len(tx.get_items()) == 2
    assert tx.total_cost() == 11.49
    
    fries = FoodItem("Fries", 3.50, "Sides", 5)
    tx.add_item(fries)
    assert tx.total_cost() == 14.99
    print("✓ Transaction tests passed")


def test_menu():
    """Test Menu class."""
    menu = Menu()
    assert menu.get_all_items() == []
    
    # Add items
    burger = FoodItem("Spicy Burger", 8.99, "Entrees", 4)
    soda = FoodItem("Cola", 2.50, "Drinks", 3)
    fries = FoodItem("Fries", 3.50, "Sides", 5)
    dessert = FoodItem("Ice Cream", 4.99, "Desserts", 5)
    
    menu.add_item(burger)
    menu.add_item(soda)
    menu.add_item(fries)
    menu.add_item(dessert)
    
    assert len(menu.get_all_items()) == 4
    
    # Test filtering by category
    entrees = menu.filter_by_category("Entrees")
    assert len(entrees) == 1
    assert entrees[0].name == "Spicy Burger"
    
    drinks = menu.filter_by_category("Drinks")
    assert len(drinks) == 1
    assert drinks[0].name == "Cola"
    
    sides = menu.filter_by_category("Sides")
    assert len(sides) == 1
    assert sides[0].name == "Fries"
    
    desserts = menu.filter_by_category("Desserts")
    assert len(desserts) == 1
    assert desserts[0].name == "Ice Cream"
    
    # Test filtering with no matches
    no_match = menu.filter_by_category("NonExistent")
    assert len(no_match) == 0
    print("✓ Menu tests passed")


if __name__ == "__main__":
    test_fooditem()
    test_customer()
    test_transaction()
    test_menu()
    print("\n✅ All tests passed!")
