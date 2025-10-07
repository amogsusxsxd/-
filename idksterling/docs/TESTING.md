- [ ] Регистрация нового пользователя
- [ ] Вход существующего пользователя
- [ ] Выход из системы
- [ ] Валидация полей формы
- [ ] Обработка неверных credentials
- [ ] Сохранение сессии
- [ ] Отображение списка товаров
- [ ] Фильтрация по жанрам
- [ ] Фильтрация по платформам
- [ ] Поиск товаров
- [ ] Сортировка товаров
- [ ] Добавление в заказ
- [ ] Указание количества
- [ ] Расчет общей стоимости
- [ ] Подтверждение заказа
- [ ] Создание записи в БД
- [ ] Chrome
- [ ] Firefox
- [ ] Safari 
- [ ] Edge

### Сценария

def test_complete_purchase_flow():
### Регистрация
    register_user()
    
### Поиск товара
    search_game("The Witcher 3")
    
### Добавление в заказ
    add_to_order()
    
### Оформление заказа
    checkout()
    
### Проверка БД
    assert order_created_in_db()

### Проверка связей
SELECT * FROM products WHERE genre_id NOT IN (SELECT id FROM genres);

### Проверка дубликатов
SELECT username, COUNT(*) FROM users GROUP BY username HAVING COUNT(*) > 1;

### Проверка обязательных полей
SELECT * FROM products WHERE name IS NULL OR price IS NULL;

### conftest.py
import pytest
from app import app, db

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

@pytest.fixture
def auth_client(client):
    # Авторизованный клиент
    client.post('/login', data={
        'username': 'testuser',
        'password': 'testpass'
    })
    return client