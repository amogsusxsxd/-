### /* Основные цвета */
--primary-blue: #022f7e;      /* Основной синий */
--gradient-start: #667eea;    /* Начало градиента */
--gradient-end: #764ba2;      /* Конец градиента */
--text-dark: #333333;         /* Основной текст */
--text-gray: #666666;         /* Вторичный текст */
--text-light: #888888;        /* Третичный текст */

### /* Фоновые цвета */
--bg-white: #ffffff;          /* Белый фон */
--bg-light: #f8f9fa;          /* Светлый фон */
--bg-gray: #e9ecef;           /* Серый фон */

### /* Статусные цвета */
--success: #28a745;           /* Успех */
--warning: #ffc107;           /* Предупреждение */
--error: #dc3545;             /* Ошибка */
--info: #17a2b8;              /* Информация */

### /* Шрифты */
font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;

### /* Размеры шрифтов */
--text-xs: 0.75rem;    /* 12px */
--text-sm: 0.875rem;   /* 14px */
--text-base: 1rem;     /* 16px */
--text-lg: 1.125rem;   /* 18px */
--text-xl: 1.25rem;    /* 20px */
--text-2xl: 1.5rem;    /* 24px */
--text-3xl: 1.875rem;  /* 30px */
--text-4xl: 2.25rem;   /* 36px */

### /* Начертания */
font-weight: 400;  /* Regular */
font-weight: 600;  /* Semi-bold */
font-weight: 700;  /* Bold */

### /* Основная кнопка */
.btn-primary {
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: white;
    padding: 12px 30px;
    border: none;
    border-radius: 25px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    transition: all 0.3s ease;
}

.btn-primary:hover {
    transform: translateY(-2px);
    box-shadow: 0 10px 20px rgba(102, 126, 234, 0.3);
}

/* Вторичная кнопка */
.btn-secondary {
    background: #f8f9fa;
    color: #333;
    border: 2px solid #e1e5e9;
}

/* Кнопка-призрак */
.btn-ghost {
    background: transparent;
    color: #667eea;
    border: 2px solid #667eea;
}

--ease-in: cubic-bezier(0.4, 0, 1, 1);
--ease-out: cubic-bezier(0, 0, 0.2, 1);
--ease-in-out: cubic-bezier(0.4, 0, 0.2, 1);
--ease-smooth: cubic-bezier(0.25, 0.46, 0.45, 0.94);

### /* Быстрая анимация */
.transition-fast {
    transition: all 0.15s var(--ease-out);
}

### /* Стандартная анимация */
.transition-normal {
    transition: all 0.3s var(--ease-in-out);
}

### /* Медленная анимация */
.transition-slow {
    transition: all 0.5s var(--ease-smooth);
}