from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import Restaurant, Pizza, RestaurantPizza, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/database_name'  # Replace with your database connection URL
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
    pizzas =
