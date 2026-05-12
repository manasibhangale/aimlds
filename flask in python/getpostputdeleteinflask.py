from flask import Flask, jsonify, request

# Create Flask application instance
app = Flask(__name__)

# -------------------------------------------------------
# In-memory database (temporary storage)
# This is a Python list containing dictionaries.
# Each dictionary represents an item with:
# - id: unique identifier
# - name: name of the item
# - description: details about the item
# NOTE: Data will reset when server restarts
# -------------------------------------------------------
items = [
    {"id": 1, "name": "Laptop", "description": "Dell Inspiron"},
    {"id": 2, "name": "Phone", "description": "iPhone 14"}
]


# -------------------------------------------------------
# ROUTE: GET ALL ITEMS
# METHOD: GET
# URL: /items
# PURPOSE: Return all items in the database
# -------------------------------------------------------
@app.route("/items", methods=["GET"])
def get_items():
    # jsonify converts Python list/dict into JSON response
    return jsonify(items), 200


# -------------------------------------------------------
# ROUTE: GET SINGLE ITEM BY ID
# METHOD: GET
# URL: /items/<item_id>
# PURPOSE: Fetch a single item using its ID
# -------------------------------------------------------
@app.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    # Search item using generator expression
    item = next((i for i in items if i["id"] == item_id), None)

    # If item exists, return it
    if item:
        return jsonify(item), 200

    # If not found, return error message with 404 status
    return jsonify({"error": "Item not found"}), 404


# -------------------------------------------------------
# ROUTE: CREATE NEW ITEM
# METHOD: POST
# URL: /items
# PURPOSE: Add a new item to the list
# -------------------------------------------------------
@app.route("/items", methods=["POST"])
def create_item():
    # Get JSON data sent in request body
    data = request.get_json()

    # Validate input data
    if not data or "name" not in data or "description" not in data:
        return jsonify({"error": "Invalid input"}), 400

    # Generate new unique ID
    # If list is empty, start from 1 using default=0
    new_id = max([i["id"] for i in items], default=0) + 1

    # Create new item dictionary
    new_item = {
        "id": new_id,
        "name": data["name"],
        "description": data["description"]
    }

    # Add new item to list (database)
    items.append(new_item)

    # Return created item with 201 status code
    return jsonify(new_item), 201


# -------------------------------------------------------
# ROUTE: UPDATE EXISTING ITEM
# METHOD: PUT
# URL: /items/<item_id>
# PURPOSE: Modify existing item data
# -------------------------------------------------------
@app.route("/items/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    # Get updated data from request body
    data = request.get_json()

    # Find item by ID
    item = next((i for i in items if i["id"] == item_id), None)

    # If item not found, return error
    if not item:
        return jsonify({"error": "Item not found"}), 404

    # Update fields if provided, otherwise keep old values
    item["name"] = data.get("name", item["name"])
    item["description"] = data.get("description", item["description"])

    # Return updated item
    return jsonify(item), 200


# -------------------------------------------------------
# ROUTE: DELETE ITEM
# METHOD: DELETE
# URL: /items/<item_id>
# PURPOSE: Remove an item from the list
# -------------------------------------------------------
@app.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    global items  # allows modification of global list

    # Check if item exists
    item = next((i for i in items if i["id"] == item_id), None)

    # If not found, return error
    if not item:
        return jsonify({"error": "Item not found"}), 404

    # Remove item by filtering list
    items = [i for i in items if i["id"] != item_id]

    # Return success message
    return jsonify({"message": "Item deleted successfully"}), 200


# -------------------------------------------------------
# RUN FLASK APPLICATION
# debug=True enables:
# - Auto-reload on code changes
# - Detailed error messages
# -------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)