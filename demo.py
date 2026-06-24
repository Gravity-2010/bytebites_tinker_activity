"""
ByteBites Demo Script
Demonstrates the core functionality of the four classes:
- Creating a menu with food items
- Creating customers and transactions
- Tracking purchase history
"""

from models import FoodItem, Customer, Menu, Transaction


def main():
    print("=" * 70)
    print("ByteBites App Demo")
    print("=" * 70)
    
    # Step 1: Create a Menu and add food items
    print("\n[1] Creating Menu with Sample Food Items")
    print("-" * 70)
    
    menu = Menu()
    
    items_data = [
        ("Spicy Burger", 8.99, "Entrees", 4),
        ("Classic Burger", 7.99, "Entrees", 5),
        ("Grilled Chicken", 9.49, "Entrees", 3),
        ("French Fries", 3.50, "Sides", 5),
        ("Onion Rings", 4.50, "Sides", 4),
        ("Cola", 2.50, "Drinks", 3),
        ("Iced Tea", 2.99, "Drinks", 4),
        ("Chocolate Shake", 4.99, "Drinks", 5),
        ("Brownie", 4.99, "Desserts", 5),
        ("Ice Cream Cup", 3.99, "Desserts", 4),
    ]
    
    for name, price, category, rating in items_data:
        item = FoodItem(name, price, category, rating)
        menu.add_item(item)
        print(f"  ✓ Added: {name} (${price}, {category}, rating: {rating})")
    
    print(f"\nTotal items in menu: {len(menu.get_all_items())}")
    
    # Step 2: Browse menu by category
    print("\n[2] Browsing Menu by Category")
    print("-" * 70)
    
    categories = ["Entrees", "Sides", "Drinks", "Desserts"]
    for category in categories:
        items = menu.filter_by_category(category)
        print(f"\n  {category}:")
        for item in items:
            details = item.get_details()
            print(f"    - {details['name']}: ${details['price']}")
    
    # Step 3: Create customers and transactions
    print("\n[3] Creating Customers and Transactions")
    print("-" * 70)
    
    # Customer 1: Alice
    alice = Customer("Alice")
    print(f"\n  Created customer: {alice.name}")
    
    # Alice's Transaction 1
    tx1 = Transaction()
    burger = menu.filter_by_category("Entrees")[0]  # Spicy Burger
    fries = menu.filter_by_category("Sides")[0]     # French Fries
    cola = menu.filter_by_category("Drinks")[0]     # Cola
    
    tx1.add_item(burger)
    tx1.add_item(fries)
    tx1.add_item(cola)
    alice.add_transaction(tx1)
    print(f"\n  Transaction 1 for {alice.name}:")
    for item in tx1.get_items():
        print(f"    - {item.name}: ${item.price}")
    print(f"    Total: ${tx1.total_cost():.2f}")
    
    # Alice's Transaction 2
    tx2 = Transaction()
    chicken = menu.filter_by_category("Entrees")[2]  # Grilled Chicken
    shake = menu.filter_by_category("Drinks")[2]     # Chocolate Shake
    
    tx2.add_item(chicken)
    tx2.add_item(shake)
    alice.add_transaction(tx2)
    print(f"\n  Transaction 2 for {alice.name}:")
    for item in tx2.get_items():
        print(f"    - {item.name}: ${item.price}")
    print(f"    Total: ${tx2.total_cost():.2f}")
    
    # Customer 2: Bob
    bob = Customer("Bob")
    print(f"\n  Created customer: {bob.name}")
    
    tx3 = Transaction()
    burger2 = menu.filter_by_category("Entrees")[1]  # Classic Burger
    rings = menu.filter_by_category("Sides")[1]      # Onion Rings
    brownie = menu.filter_by_category("Desserts")[0] # Brownie
    
    tx3.add_item(burger2)
    tx3.add_item(rings)
    tx3.add_item(brownie)
    bob.add_transaction(tx3)
    print(f"\n  Transaction 1 for {bob.name}:")
    for item in tx3.get_items():
        print(f"    - {item.name}: ${item.price}")
    print(f"    Total: ${tx3.total_cost():.2f}")
    
    # Step 4: Display purchase history
    print("\n[4] Customer Purchase History")
    print("-" * 70)
    
    for customer in [alice, bob]:
        print(f"\n  {customer.name}'s Purchase History:")
        history = customer.get_purchase_history()
        total_spent = 0.0
        
        for i, tx in enumerate(history, 1):
            cost = tx.total_cost()
            total_spent += cost
            print(f"    Transaction {i}: ${cost:.2f}")
        
        print(f"    Total spent: ${total_spent:.2f}")
    
    print("\n" + "=" * 70)
    print("✅ Demo Complete!")
    print("=" * 70)


if __name__ == "__main__":
    main()
