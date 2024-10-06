import json
import csv
import os.path


# Создание переменных, содержащих путь до файлов books.csv и users.json
file_dir = os.path.dirname(__file__)

def get_path(filename: str):
    return os.path.join(file_dir, filename)

JSON_FILE_PATH = get_path(filename="users.json")
CSV_FILE_PATH = get_path(filename="books.csv")

#print(JSON_FILE_PATH)
#print(CSV_FILE_PATH)


result_csv = {}
result_books = []

with open(CSV_FILE_PATH, newline="") as f:
    reader = csv.reader(f)
    # Извлекаем заголовок
    header = next(reader)

    # Итерируемся по строкам делая из них словари
    for row in reader:
        result_csv = dict(zip(header, row))
        result_books.append(result_csv)

print(result_books)
print(len(result_books))

# Прочитать файл users.json
with open(JSON_FILE_PATH, "r") as f:
    users = json.load(f)

#print(users)
a = len(users)  # записываем в переменную "а"  количество элементов в списке

result_users = []

for i in users:
    result_user = {}
    result_user["name"] = i["name"]
    result_user["gender"] = i["gender"]
    result_user["address"] = i["address"]
    result_user["age"] = i["age"]
    result_user["books"] = []
    result_users.append(result_user)

print(result_users)
print(len(result_users))

# Распределение книг между пользователями
if len(result_books) > len(result_users):
    books_per_user = len(result_books) // len(result_users)
    extra_books = len(result_books) % len(result_users)
else:
    books_per_user = len(result_books) // len(result_users)
    extra_books = 0

# Обновляем количество книг для каждого пользователя
for i in range(len(result_users)):
    user = result_users[i]
    user_books = []

    for j in range(books_per_user):
        user_books.append(result_books[extra_books + i * books_per_user + j])

    # Дополнительно добавляем одну книгу тем пользователям, у которых индекс меньше, чем extra_books
    if i < extra_books:
        user_books.append(result_books[i])

    result_users[i]['books'] = user_books

# Сохранение результата в JSON файл
with open('result.json', 'w') as f:
    json.dump(result_users, f, indent=4)
