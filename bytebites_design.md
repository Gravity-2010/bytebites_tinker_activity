# ByteBites Design

## UML Diagram

```text
+---------------------+
|      Customer       |
+---------------------+
| - name: str         |
| - purchase_history: list[Transaction] |
+---------------------+
| + add_transaction(tx: Transaction) -> None |
| + get_purchase_history() -> list[Transaction] |
+---------------------+

           1
Customer o----* Transaction

+---------------------+
|      Transaction    |
+---------------------+
| - items: list[FoodItem] |
+---------------------+
| + add_item(item: FoodItem) -> None |
| + total_cost() -> float |
| + get_items() -> list[FoodItem] |
+---------------------+

           1
Transaction o----* FoodItem

+---------------------+
|      Menu           |
+---------------------+
| - items: list[FoodItem] |
+---------------------+
| + add_item(item: FoodItem) -> None |
| + filter_by_category(category: str) -> list[FoodItem] |
| + get_all_items() -> list[FoodItem] |
+---------------------+

+---------------------+
|     FoodItem        |
+---------------------+
| - name: str         |
| - price: float      |
| - category: str     |
| - popularity_rating: int |
+---------------------+
| + get_details() -> dict |
+---------------------+
```

## Relationships

- `Customer` maintains a purchase history of `Transaction` objects.
- `Transaction` aggregates multiple `FoodItem` objects.
- `Menu` contains multiple `FoodItem` objects for browsing and filtering.
- `FoodItem` is the shared item entity used by both `Menu` and `Transaction`.
