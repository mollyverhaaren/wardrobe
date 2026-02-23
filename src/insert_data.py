import sqlite3

def insert_data(db_name="wardrobe.db"):
    """Inserts sample data into the wardrobe database for analyzing."""

    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")

    # 1. Insert Sample Wardrobe Items
    items_data = [
        ('Green Fleece Chore Jacket', 'J.Crew', 'Outerwear', 'Polyester', 'Tumble Dry Low', 112.00, 42.00, "2022-01-18"),
        ('Gray Sweat Pants', 'J.Crew', 'Bottom', 'Polyester', 'Tumble Dry Low', 0.00, 0.00, "2021-03-01"),
        ('Vans Logo T-Shirt', 'Vans', 'Top', 'Polyester', 'Tumble Dry Low', 0.00, 0.00, '2022-05-01')        
    ]

    cursor.executemany("""
        INSERT INTO items (item_name, brand, category, fabric, care, retail_price, purchase_price, purchase_date)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, items_data)

    # 2. Insert Sample Wear Logs
    wear_data = [
        ('2026-02-23', 1, 'Home', 'Snow', 'NYC', 2, "Feel schlubby but warm."),
        ('2026-02-23', 2, 'Home', 'Snow', 'NYC', 4, "Always love these. Afraid they're going to fall apart."),
        ('2026-02-23', 3, 'Home', 'Snow', 'NYC', 2, "Feel schlubby but warm.")
    ]

    cursor.executemany("""
        INSERT INTO wear_history (date, item_id, outing_type, weather, location, fit_satisfaction, notes)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, wear_data)

    conn.commit()
    conn.close()
    print("Initial data successfully inserted into the database!")

if __name__ == "__main__":
    insert_data()