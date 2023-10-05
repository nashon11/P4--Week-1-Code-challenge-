from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import Restaurant, Pizza, RestaurantPizza, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:\\\'  # 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

# Define routes and views here

# Route to get a list of restaurants
@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    restaurant_list = []

    for restaurant in restaurants:
        restaurant_data = {
            'id': restaurant.id,
            'name': restaurant.name,
            'address': restaurant.address
        }
        restaurant_list.append(restaurant_data)

    return jsonify(restaurant_list)

# Route to get details of a specific restaurant
@app.route('/restaurants/<int:id>', methods=['GET'])
def get_restaurant(id):
    restaurant = Restaurant.query.get(id)

    if not restaurant:
        return jsonify({'error': 'Restaurant not found'}), 404

    pizzas = []
    for pizza in restaurant.pizzas:
        pizza_data = {
            'id': pizza.id,
            'name': pizza.name,
            'ingredients': pizza.ingredients
        }
        pizzas.append(pizza_data)

    restaurant_data = {
        'id': restaurant.id,
        'name': restaurant.name,
        'address': restaurant.address,
        'pizzas': pizzas
    }

    return jsonify(restaurant_data)

# Route to delete a restaurant
@app.route('/restaurants/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)

    if not restaurant:
        return jsonify({'error': 'Restaurant not found'}), 404

    # Implement logic to delete the restaurant and associated restaurant_pizzas
    db.session.delete(restaurant)

    # Commit the changes to the database
    db.session.commit()

    return jsonify({}), 204  # Return an empty response with HTTP status 204

# Route to get a list of pizzas
@app.route('/pizzas', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    pizza_list = []

    for pizza in pizzas:
        pizza_data = {
            'id': pizza.id,
            'name': pizza.name,
            'ingredients': pizza.ingredients
        }
        pizza_list.append(pizza_data)

    return jsonify(pizza_list)

# Route to create a new restaurant_pizza
@app.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()

    # Validate the data
    if 'price' not in data or 'pizza_id' not in data or 'restaurant_id' not in data:
        return jsonify({'errors': ['Missing required fields']}), 400

    price = data['price']
    pizza_id = data['pizza_id']
    restaurant_id = data['restaurant_id']

    # Implement logic to create a new restaurant_pizza based on the data provided
    restaurant_pizza = RestaurantPizza(price=price, pizza_id=pizza_id, restaurant_id=restaurant_id)
    db.session.add(restaurant_pizza)
    db.session.commit()

    # Return the created restaurant_pizza data in JSON format
    return jsonify({
        'id': restaurant_pizza.id,
        'price': restaurant_pizza.price,
        'pizza_id': restaurant_pizza.pizza_id,
        'restaurant_id': restaurant_pizza.restaurant_id
    }), 201  # Return HTTP status 201 for "Created"

if __name__ == '__main__':
    app.run()

