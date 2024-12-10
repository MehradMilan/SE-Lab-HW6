from flask import Flask, request, jsonify
import sqlite3
import os

app = Flask(__name__)
DB_PATH = '/app/data/data.db'

def init_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            value REAL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/items', methods=['GET'])
def get_items():
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM items")
        rows = cursor.fetchall()
        conn.close()
        return jsonify(rows), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/items', methods=['POST'])
def add_item():
    try:
        data = request.json
        if not data or 'name' not in data or 'value' not in data:
            return jsonify({"error": "Invalid input data"}), 400

        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO items (name, value) VALUES (?, ?)", (data['name'], data['value']))
        conn.commit()
        conn.close()
        return jsonify({"message": "Item added successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM items WHERE id = ?", (item_id,))
        if cursor.rowcount == 0:
            conn.close()
            return jsonify({"error": "Item not found"}), 404

        conn.commit()
        conn.close()
        return jsonify({"message": "Item deleted successfully!"}),
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)