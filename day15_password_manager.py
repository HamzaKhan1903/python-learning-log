import sqlite3
connection = sqlite3.connect("credential_manager.db")
cursor = connection.cursor()
cursor.execute ("CREATE TABLE IF NOT EXISTS user_details (unique_id INTEGER PRIMARY KEY, site_name TEXT, username TEXT, password TEXT, last_updated TEXT)")
connection.commit()