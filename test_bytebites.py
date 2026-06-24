from models import FoodItem, Menu, Transaction


def test_calculate_total_with_multiple_items():
    """Verify a transaction total equals the sum of added items."""
    transaction = Transaction()
    transaction.add_item(FoodItem("Burger", 10.00, "Entrees", 4))
    transaction.add_item(FoodItem("Soda", 5.00, "Drinks", 3))

    assert transaction.total_cost() == 15.00


def test_order_total_is_zero_when_empty():
    """Verify an empty transaction total is zero."""
    transaction = Transaction()

    assert transaction.total_cost() == 0.00


def test_filter_by_category_returns_only_requested_items():
    """Verify menu filtering returns only items of the requested category."""
    menu = Menu()
    menu.add_item(FoodItem("Spicy Burger", 8.99, "Entrees", 4))
    menu.add_item(FoodItem("Cola", 2.50, "Drinks", 3))
    menu.add_item(FoodItem("Iced Tea", 2.99, "Drinks", 4))
    menu.add_item(FoodItem("Fries", 3.50, "Sides", 5))

    drinks = menu.filter_by_category("Drinks")

    assert len(drinks) == 2
    assert all(item.category == "Drinks" for item in drinks)
    assert {item.name for item in drinks} == {"Cola", "Iced Tea"}


if __name__ == "__main__":
    test_calculate_total_with_multiple_items()
    test_order_total_is_zero_when_empty()
    test_filter_by_category_returns_only_requested_items()
    print("\n✅ test_bytebites.py passed all tests")
