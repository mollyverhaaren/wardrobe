import sqlite3

def initialize_database(db_name="wardrobe.db"):
    """Creates the necessary tables for the wardrobe tracking database."""
    
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS items (
            item_id INTEGER PRIMARY KEY AUTOINCREMENT,
            item_name TEXT NOT NULL,
            brand TEXT,
            category TEXT,
            fabric TEXT,
            care TEXT,
            retail_price REAL,
            purchase_price REAL,
            purchase_date DATE,
            status TEXT DEFAULT 'Active'
        );
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS wear_history (
            log_id INTEGER PRIMARY KEY AUTOINCREMENT,
            date DATE NOT NULL,
            item_id INTEGER,
            outing_type TEXT,
            weather TEXT,
            location TEXT,
            fit_satisfaction INTEGER CHECK(fit_satisfaction >= 1 AND fit_satisfaction <= 5),
            notes TEXT,
            FOREIGN KEY (item_id) REFERENCES items(item_id)
        );
    """)
    
    conn.commit()
    conn.close()
    print(f"Database '{db_name}' initialized successfully with 'items' and 'wear_history' tables.")

if __name__ == "__main__":
    initialize_database()