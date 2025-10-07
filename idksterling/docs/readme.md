# 🎮 GameHub - Игровая платформа

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)](https://flask.palletsprojects.com)
[![SQLite](https://img.shields.io/badge/SQLite-Database-lightgrey.svg)](https://sqlite.org)
[![Лицензия](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Версия](https://img.shields.io/badge/version-1.0.0-green.svg)]()

**GameHub** - это современная веб-платформа для продажи видеоигр, построенная на Flask. Платформа предоставляет пользователям удобный интерфейс для покупки игр, управления библиотекой и взаимодействия с игровым сообществом.

---

##  Быстрый старт

Это самый важный раздел! Покажу, как установить и запустить проект за 4 простых шага.

### Предварительные требования

* Python 3.8 или выше
* pip (менеджер пакетов Python)
* Git для клонирования репозитория

### Установка и запуск

1.  **Клонируйте репозиторий**
    ```bash
    git clone https://github.com/SuperFish22/GameHub.git
    cd GameHub
    ```

2.  **Создайте виртуальное окружение**
    ```bash
    # Для Windows
    python -m venv venv
    venv\Scripts\activate
    
    # Для Linux/MacOS
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Установите зависимости**
    ```bash
    pip install flask
    ```

4.  **Запустите приложение**
    ```bash
    python app.py
    ```
    Приложение будет доступно по адресу: `http://localhost:5000`.

---

##  Документация

*   **[Архитектура проекта](./docs/ARCHITECTURE.md)** - Детальное руководство по структуре проекта и БД
*   [API документация](./docs/API.md) - Описание всех endpoints
*   [Руководство по установке](./docs/INSTALLATION.md) - Подробная инструкция по настройке

---

##  Функциональность

*   **Магазин игр** - Каталог с фильтрацией по жанрам, платформам и издателям
*   **Система аутентификации** - Регистрация и вход пользователей
*   **Адаптивный дизайн** - Оптимизирован для всех устройств
*   **Умные фильтры** - Поиск игр по различным параметрам
*   **Современный UI** - Градиентный дизайн с анимациями

![Главная страница GameHub](https://via.placeholder.com/800x400/667eea/ffffff?text=GameHub+Dashboard)

---

##  Технологии

*   **Бэкенд:** Python, Flask
*   **Фронтенд:** HTML5, CSS3, JavaScript
*   **База данных:** SQLite
*   **Шаблонизатор:** Jinja2
*   **Стили:** Custom CSS с градиентами и анимациями

---

##  Структура проекта
