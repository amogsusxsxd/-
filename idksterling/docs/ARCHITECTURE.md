# Архитектура

Проекта GameHub

# Обзор

Проект использует традиционную веб-архитектуру с серверным рендерингом.

Фронтенд: HTML шаблоны с Jinja2, CSS, JavaScript

Бэкенд: Flask (Python)

База данных: SQLite

Архитектура: MVC (Model-View-Controller)

# Структура папок

gamehub-project/
├── static/                 # Статические файлы
│   ├── css/               # Стили
│   ├── js/                # JavaScript файлы
│   ├── images/            # Изображения
│   └── uploads/           # Загружаемые файлы
├── templates/             # HTML шаблоны
│   ├── base.html          # Базовый шаблон
│   ├── index.html         # Главная страница
│   ├── shop.html          # Магазин игр
│   ├── proba.html         # Страница регистрации/входа
│   ├── about.html         # Страница "О нас"
│   ├── Data_Base.html     # Базовый шаблон с навигацией
│   ├── dashboard.html     # Панель управления
│   ├── product_detail.html # Детали товара
│   ├── register.html      # Регистрация
│   └── niggagaming.html   # Игровая страница
├── app.py                 # Основное приложение Flask
├── create_tables.py       # Скрипт создания таблиц БД
├── gamehub.db            # База данных SQLite
├── my_database.db        # Дополнительная БД
├── proba.py              # Дополнительные функции
└── requirements.txt      # Зависимости Python