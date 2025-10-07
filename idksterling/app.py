from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
import hashlib
import secrets

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

def get_db_connection():
    """Создает подключение к базе данных"""
    conn = sqlite3.connect('my_database.db', check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

def hash_password(password):
    """Хеширует пароль"""
    return hashlib.sha256(password.encode()).hexdigest()

def productDB():
    """Получает список продуктов из БД"""
    try:
        conn = get_db_connection()
        products = conn.execute('SELECT * FROM product').fetchall()
        conn.close()
        return products
    except sqlite3.Error as e:
        print(f"Ошибка базы данных: {e}")
        return []

def get_user_purchases(user_id):
    """Получает покупки пользователя"""
    try:
        conn = get_db_connection()
        purchases = conn.execute('''
            SELECT p.name, p.price, pur.purchase_date 
            FROM purchases pur 
            JOIN product p ON pur.product_id = p.id 
            WHERE pur.user_id = ? 
            ORDER BY pur.purchase_date DESC
        ''', (user_id,)).fetchall()
        conn.close()
        return purchases
    except sqlite3.Error as e:
        print(f"Ошибка базы данных: {e}")
        return []

@app.route('/')
def hello_world():
    tovar = productDB()
    return render_template("index.html", shop=tovar)

@app.route('/shop')
def shop():
    """Страница магазина с фильтрами"""
    try:
        conn = get_db_connection()
        
        genre_filter = request.args.get('genre', '')
        platform_filter = request.args.get('platform', '')
        publisher_filter = request.args.get('publisher', '')

        query = '''
            SELECT p.*, g.name as genre_name, pub.name as publisher_name 
            FROM product p
            LEFT JOIN genre g ON p.genre_id = g.id
            LEFT JOIN publisher pub ON p.publisher_id = pub.id
            WHERE 1=1
        '''
        params = []
        
        if genre_filter:
            query += ' AND g.name = ?'
            params.append(genre_filter)
        if platform_filter:
            query += ' AND EXISTS (SELECT 1 FROM product_platform pp JOIN platform pl ON pp.platform_id = pl.id WHERE pp.product_id = p.id AND pl.name = ?)'
            params.append(platform_filter)
        if publisher_filter:
            query += ' AND pub.name = ?'
            params.append(publisher_filter)
        
        products = conn.execute(query, params).fetchall()
        
        genres = conn.execute('SELECT DISTINCT name FROM genre').fetchall()
        platforms = conn.execute('SELECT DISTINCT name FROM platform').fetchall()
        publishers = conn.execute('SELECT DISTINCT name FROM publisher').fetchall()
        
        conn.close()
        
        return render_template("shop.html", shop=products, genres=genres, platforms=platforms, publishers=publishers,
                              selected_genre=genre_filter, selected_platform=platform_filter, selected_publisher=publisher_filter)
    except sqlite3.Error as e:
        print(f"Ошибка базы данных: {e}")
        return render_template("shop.html", shop=[], genres=[], platforms=[], publishers=[])

@app.route('/game_shop')
def game_shop():
    """Страница распродажи игр"""
    try:
        conn = get_db_connection()
        sale_products = conn.execute(
            'SELECT * FROM product WHERE price < 1500'
        ).fetchall()
        conn.close()
        return render_template("niggagaming.html", shop=sale_products)
    except sqlite3.Error as e:
        print(f"Ошибка базы данных: {e}")
        return render_template("niggagaming.html", shop=[])

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Регистрация пользователя"""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        
        try:
            conn = get_db_connection()
            existing_user = conn.execute(
                'SELECT * FROM users WHERE username = ?', (username,)
            ).fetchone()
            
            if existing_user:
                flash('Пользователь с таким именем уже существует', 'error')
                return render_template('register.html')
            
            hashed_password = hash_password(password)
            conn.execute(
                'INSERT INTO users (username, password, email) VALUES (?, ?, ?)',
                (username, hashed_password, email)
            )
            conn.commit()
            conn.close()
            
            flash('Регистрация прошла успешно! Теперь вы можете войти.', 'success')
            return redirect(url_for('login'))
            
        except sqlite3.Error as e:
            print(f"Ошибка базы данных: {e}")
            flash('Ошибка при регистрации', 'error')
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Авторизация пользователя"""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        try:
            conn = get_db_connection()
            user = conn.execute(
                'SELECT * FROM users WHERE username = ?', (username,)
            ).fetchone()
            conn.close()
            
            if user and user['password'] == hash_password(password):
                session['user_id'] = user['id']
                session['username'] = user['username']
                flash('Вход выполнен успешно!', 'success')
                return redirect(url_for('personal_account'))
            else:
                flash('Неверное имя пользователя или пароль', 'error')
                
        except sqlite3.Error as e:
            print(f"Ошибка базы данных: {e}")
            flash('Ошибка при входе', 'error')
    
    return render_template('proba.html')

@app.route('/logout')
def logout():
    """Выход из системы"""
    session.clear()
    flash('Вы вышли из системы', 'info')
    return redirect(url_for('hello_world'))

@app.route('/personal_account')
def personal_account():
    """Личный кабинет"""
    if 'user_id' not in session:
        flash('Для доступа к личному кабинету необходимо войти в систему', 'error')
        return redirect(url_for('login'))
    
    user_id = session['user_id']
    purchases = get_user_purchases(user_id)
    
    return render_template("dashboard.html", 
                         user={'username': session['username']}, 
                         purchases=purchases)

@app.route('/buy/<int:product_id>')
def buy_product(product_id):
    """Покупка товара"""
    if 'user_id' not in session:
        flash('Для покупки необходимо войти в систему', 'error')
        return redirect(url_for('login'))
    
    try:
        conn = get_db_connection()
        
        product = conn.execute(
            'SELECT * FROM product WHERE id = ?', (product_id,)
        ).fetchone()
        
        if not product:
            flash('Товар не найден', 'error')
            return redirect(url_for('shop'))
        
        conn.execute(
            'INSERT INTO purchases (user_id, product_id, purchase_date) VALUES (?, ?, datetime("now"))',
            (session['user_id'], product_id)
        )
        conn.commit()
        conn.close()
        
        flash(f'Поздравляем! Вы приобрели "{product["name"]}"', 'success')
        return redirect(url_for('personal_account'))
        
    except sqlite3.Error as e:
        print(f"Ошибка базы данных: {e}")
        flash('Ошибка при покупке товара', 'error')
        return redirect(url_for('shop'))

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    """Страница деталей продукта"""
    try:
        conn = get_db_connection()
        product = conn.execute(
            'SELECT * FROM product WHERE id = ?', (product_id,)
        ).fetchone()
        
        conn.close()
        
        if product:
            return render_template("product_detail.html", product=product)
        else:
            return "Продукт не найден", 404
    except sqlite3.Error as e:
        print(f"Ошибка базы данных: {e}")
        return "Ошибка сервера", 500

@app.route('/stockings')
def stockings():
    return 'Покупки'

@app.route('/contact')
def contact():
    return 'Контакты'

@app.route('/descriptions')
def descriptions():
    return 'расписание'

@app.route('/about-us')
def about_us():
    return 'о нас'

@app.route('/user/<username>')
def user_profile(username):
    return f'Профиль пользователя: {username}'

@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == '__main__':
    print('[server starting...]')
    app.run(debug=True)