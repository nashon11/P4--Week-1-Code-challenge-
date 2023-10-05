from app import app, db, Restaurant, Pizza, RestaurantPizza

# Create some sample restaurants
restaurant1 = Restaurant(name="Pizza Palace", address="123 Main St")
restaurant2 = Restaurant(name="Italian Delight", address="456 Elm St")

# Create some sample pizzas
pizza1 = Pizza(name="Margherita", ingredients="Tomato, Mozzarella, Basil")
pizza2 = Pizza(name="Pepperoni", ingredients="Pepperoni, Cheese, Tomato Sauce")

# Add objects to the session and commit to the database
with app.app_context():
    db.session.add(restaurant1)
    db.session.add(restaurant2)
    db.session.add(pizza1)
    db.session.add(pizza2)
    db.session.commit()

# Create relationships between restaurants and pizzas with prices
restaurant_pizza1 = RestaurantPizza(price=12.99, restaurant_id=restaurant1.id, pizza_id=pizza1.id)
restaurant_pizza2 = RestaurantPizza(price=15.99, restaurant_id=restaurant1.id, pizza_id=pizza2.id)
restaurant_pizza3 = RestaurantPizza(price=14.99, restaurant_id=restaurant2.id, pizza_id=pizza1.id)
restaurant_pizza4 = RestaurantPizza(price=16.99, restaurant_id=restaurant2.id, pizza_id=pizza2.id)

# Add restaurant_pizza objects to the session and commit to the database
with app.app_context():
    db.session.add(restaurant_pizza1)
    db.session.add(restaurant_pizza2)
    db.session.add(restaurant_pizza3)
    db.session.add(restaurant_pizza4)
    db.session.commit()

print("Sample data has been seeded into the database.")
