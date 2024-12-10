# Базовый образ: Python 3.10 (slim чтобы было меньше места)
FROM python:3.10-slim

# Устанавливаем зависимости для сборки
RUN apt-get update && apt-get install -y curl build-essential && rm -rf /var/lib/apt/lists/*

# Устанавливаем Poetry
ENV POETRY_VERSION=1.6.1
RUN curl -sSL https://install.python-poetry.org | python3 -

# Добавляем Poetry в PATH
ENV PATH="/root/.local/bin:$PATH"

# Создадим директорию для приложения
WORKDIR /app

# Скопируем файлы зависимостей проекта
COPY pyproject.toml poetry.lock /app/
# Установим зависимости проекта
RUN poetry install --no-root --no-interaction --no-ansi

# Скопируем весь код приложения
COPY . /app/server

# Открываем порт приложения
EXPOSE 8000

# Команда по умолчанию - запуск сервера разработки (для продакшена нужен uwsgi/gunicorn)
CMD ["poetry", "run", "python", "server/manage.py", "runserver", "0.0.0.0:8000"]
