Вот обновленный файл `README.md` с пошаговыми инструкциями для запуска проекта тремя способами: без Docker, с использованием только Dockerfile, и через Docker Compose.

---

# JSON-RPC Django Client

Этот проект представляет собой Django-клиент для взаимодействия с JSON-RPC API.

---

## Как запустить проект

### 1. Запуск без Docker

#### Шаги:
1. Убедитесь, что у вас установлен **Python 3.8** или выше.
2. Установите виртуальное окружение:
   ```bash
   python -m venv venv
   ```
3. Активируйте виртуальное окружение:
   - **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - **Mac/Linux**:
     ```bash
     source venv/bin/activate
     ```
4. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
5. Запустите сервер разработки:
   ```bash
   python manage.py runserver
   ```
6. Откройте в браузере: [http://localhost:8000](http://localhost:8000).

---

### 2. Запуск через Dockerfile

#### Шаги:
1. Убедитесь, что у вас установлен **Docker**.
2. Соберите Docker-образ:
   ```bash
   docker build -t jsonrpc-client .
   ```
3. Запустите контейнер:
   ```bash
   docker run -p 8000:8000 jsonrpc-client
   ```
4. Откройте в браузере: [http://localhost:8000](http://localhost:8000).

---

### 3. Запуск через Docker Compose

#### Шаги:
1. Убедитесь, что у вас установлен **Docker Compose**.
2. Соберите контейнеры и запустите проект:
   ```bash
   docker-compose up --build
   ```
3. Откройте в браузере: [http://localhost:8000](http://localhost:8000).

4. Чтобы остановить проект:
   ```bash
   docker-compose down
   ```

---

## Описание файлов

### Dockerfile
Файл для сборки Docker-образа:

```dockerfile
# Используем базовый образ Python
FROM python:3.10

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы проекта
COPY . /app

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Открываем порт для сервера Django
EXPOSE 8000

# Команда по умолчанию для запуска контейнера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

### docker-compose.yml
Файл для запуска проекта через Docker Compose:

```yaml
version: '3.9'

services:
  web:
    build:
      context: .
      dockerfile: Dockerfile
    command: python manage.py runserver 0.0.0.0:8000
    ports:
      - "8000:8000"
    volumes:
      - .:/app
      - static_volume:/app/static

volumes:
  static_volume:
```

---
