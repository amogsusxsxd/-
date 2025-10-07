import sqlite3

def create_tables():
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()
    
    
    genres = ['Action', 'RPG', 'Adventure', 'Strategy', 'Sports']
    for genre in genres:
        cursor.execute('INSERT OR IGNORE INTO genre (name) VALUES (?)', (genre,))
    
    publishers = ['Electronic Arts', 'Ubisoft', 'Activision', 'Nintendo', 'Sony']
    for publisher in publishers:
        cursor.execute('INSERT OR IGNORE INTO publisher (name) VALUES (?)', (publisher,))
    
    platforms = ['PC', 'PlayStation', 'Xbox', 'Nintendo Switch']
    for platform in platforms:
        cursor.execute('INSERT OR IGNORE INTO platform (name) VALUES (?)', (platform,))
    
    test_products = [
        ('Cyberpunk 2077', 'Футуристическая RPG', 1999.99, 'https://via.placeholder.com/200x100?text=Cyberpunk', 2, 2),
        ('FIFA 23', 'Футбольный симулятор', 1499.99, 'https://via.placeholder.com/200x100?text=FIFA+23', 5, 1),
        ('The Witcher 3', 'RPG с открытым миром', 899.99, 'https://via.placeholder.com/200x100?text=Witcher+3', 2, 3),
        ('Call of Duty', 'Шутер от первого лица', 1299.99, 'https://via.placeholder.com/200x100?text=CoD', 1, 3)
    ]
    
    for product in test_products:
        cursor.execute('''
            INSERT OR IGNORE INTO product (name, description, price, image_url, genre_id, publisher_id) 
            VALUES (?, ?, ?, ?, ?, ?)
        ''', product)
    
    cursor.execute('''
        INSERT OR IGNORE INTO users (username, password, email) 
        VALUES (?, ?, ?)
    ''', ('testuser', 'testpass', 'test@example.com'))
    
    conn.commit()
    conn.close()
    print("Таблицы и тестовые данные успешно созданы!")

if __name__ == '__main__':
    create_tables()