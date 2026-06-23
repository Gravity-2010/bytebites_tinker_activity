
**Class Diagram (Mermaid)**
```mermaid
classDiagram
    class Customer {
        +String name
        +List~Transaction~ purchaseHistory
        +bool isVerified()
        +void addPurchase(Transaction)
    }
    class FoodItem {
        +String name
        +float price
        +String category
        +int popularityRating
    }
    class Menu {
        +List~FoodItem~ items
        +List~FoodItem~ filterByCategory(String category)
        +void addItem(FoodItem)
        +void removeItem(FoodItem)
    }
    class Transaction {
        +List~FoodItem~ items
        +float totalCost()
        +void addItem(FoodItem)
        +void removeItem(FoodItem)
    }

    Customer "1" o-- "0..*" Transaction : purchaseHistory
    Transaction "1" o-- "0..*" FoodItem : contains
    Menu "1" o-- "0..*" FoodItem : catalog
```

**Class Details**
- **`Customer`**: name; `purchaseHistory` (list of `Transaction`); methods: `isVerified()`, `addPurchase(Transaction)`.
- **`FoodItem`**: name, price, category, popularityRating.
- **`Menu`**: `items` (collection of `FoodItem`); `filterByCategory(String)` returns matching items; add/remove item helpers.
- **`Transaction`**: `items` (selected `FoodItem`s); `totalCost()` computes sum; add/remove item helpers.

