import os
import requests

# Создание новой папки
os.makedirs("json_files", exist_ok=True)

# Загрузка массива JSON-объектов
response = requests.get("https://jsonplaceholder.typicode.com/posts")
data = response.json()

# Сохранение каждого объекта в отдельный файл
for obj in data:
    file_name = f"json_files/{obj['id']}.json"
    with open(file_name, "w") as file:
        file.write(str(obj))
