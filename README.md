# flask-formatter

REST-сервис на Flask для форматирования текста. Самостоятельная работа по дисциплине «Основы DevOps».

## Структура проекта

```
flask-formatter/
├── src/
│   ├── __init__.py
│   ├── app.py          # Flask-приложение
│   └── functional.py   # Логика форматирования
├── tests/
│   ├── __init__.py
│   └── app_test.py     # pytest-тесты
├── .gitignore
├── .gitlab-ci.yml      # CI/CD пайплайн
├── requirements.txt
├── setup.cfg           # Конфигурация flake8 и mypy
└── README.md
```

## Запуск тестов локально

```bash
pip install -r requirements.txt
pytest tests/
flake8 .
mypy .
```
