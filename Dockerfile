# Указываем базовый образ
FROM python:3.12-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Устанавливаем зависимости системы (для psycopg2 и других пакетов)
RUN apt-get update && apt-get install -y gcc libpq-dev && apt-get clean

# Копируем файл зависимостей
COPY requirements.txt .

# Устанавливаем зависимости Python
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все остальные файлы проекта
COPY . .

# Экспортируем порт, на котором будет работать наше приложение
EXPOSE 8000

# Команда для запуска приложения
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]