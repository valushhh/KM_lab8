import requests
import random
import json

def get_post_by_random_id():
    # Генеруємо випадкове число від 1 до 100
    random_id = random.randint(1, 100)

    # Створюємо динамічне посилання до API
    url = f"https://jsonplaceholder.typicode.com/posts/{random_id}"

    try:
        # Надсилаємо GET-запит до API
        response = requests.get(url)
        response.raise_for_status()  # Перевірка HTTP-помилок

        # Парсимо JSON у словник (об'єкт)
        post_data = response.json()

        # Отримуємо потрібні елементи
        post_id = post_data.get("id")
        title = post_data.get("title")
        body = post_data.get("body")

        # Виводимо дані в консоль
        print("Отриманий пост:")
        print(f"ID: {post_id}")
        print(f"Заголовок: {title}")
        print(f"Тіло: {body}")

    except requests.exceptions.RequestException as e:
        print("Помилка при отриманні даних:", e)
    except json.JSONDecodeError as e:
        print("Помилка при парсингу JSON:", e)

get_post_by_random_id()
