import psycopg2
import csv

# Подключение к базе данных
conn = psycopg2.connect(
    dbname='phonebook',
    user='postgres',
    password='asyl',
    host='localhost',
    port='5432'
)
cur = conn.cursor()

# Создание таблицы, если не существует
def create_table():
    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            phone VARCHAR(20)
        );
    """)
    conn.commit()

# Загрузка из CSV
def insert_from_csv(file_path):
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # пропустить заголовок
        for row in reader:
            cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (row[0], row[1]))
    conn.commit()
    print("Данные из CSV загружены.")

# Ввод вручную
def insert_from_input():
    name = input("Введите имя: ")
    phone = input("Введите номер: ")
    cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    print("Данные добавлены.")

# Обновление по выбору
def update_data():
    choice = input("Что хотите обновить? (name/phone): ")
    old_value = input("Введите старое значение: ")
    new_value = input("Введите новое значение: ")
    if choice == "name":
        cur.execute("UPDATE phonebook SET name = %s WHERE name = %s", (new_value, old_value))
    elif choice == "phone":
        cur.execute("UPDATE phonebook SET phone = %s WHERE phone = %s", (new_value, old_value))
    conn.commit()
    print("Данные обновлены.")

# Поиск по полю
def query_data():
    field = input("Фильтровать по (name/phone): ")
    value = input("Введите значение для поиска: ")
    cur.execute(f"SELECT * FROM phonebook WHERE {field} ILIKE %s", (f"%{value}%",))
    rows = cur.fetchall()
    for row in rows:
        print(row)

# Удаление по полю
def delete_data():
    field = input("Удалить по (name/phone): ")
    value = input("Введите значение: ")
    cur.execute(f"DELETE FROM phonebook WHERE {field} = %s", (value,))
    conn.commit()
    print("Запись удалена.")

# Функция поиска по шаблону (SQL-функция)
def search_pattern():
    pattern = input("Введите часть имени или номера: ")
    cur.execute("SELECT * FROM search_phonebook(%s)", (pattern,))
    rows = cur.fetchall()
    for row in rows:
        print(row)

# Вставка/обновление через процедуру
def insert_or_update():
    name = input("Имя: ")
    phone = input("Номер: ")
    cur.execute("CALL insert_or_update_user(%s, %s)", (name, phone))
    conn.commit()
    print("Пользователь добавлен или обновлён.")

# Массовая вставка с проверкой
def insert_many():
    count = int(input("Сколько пользователей добавить? "))
    names = []
    phones = []
    for _ in range(count):
        name = input("Имя: ")
        phone = input("Номер: ")
        names.append(name)
        phones.append(phone)
    cur.execute("CALL insert_many_users(%s, %s)", (names, phones))
    conn.commit()
    print("Массовая вставка завершена.")

# Получение страницы с LIMIT и OFFSET
def get_page():
    limit = int(input("Сколько записей показать? "))
    offset = int(input("С какого смещения начать? "))
    cur.execute("SELECT * FROM get_phonebook_page(%s, %s)", (limit, offset))
    rows = cur.fetchall()
    for row in rows:
        print(row)

# Удаление через процедуру
def delete_user():
    name = input("Имя (можно оставить пустым): ")
    phone = input("Телефон (можно оставить пустым): ")
    cur.execute("CALL delete_user(%s, %s)", (name if name else None, phone if phone else None))
    conn.commit()
    print("Удаление выполнено.")

# Главное меню
def main():
    create_table()
    while True:
        print("\nМеню:")
        print("1. Добавить из CSV")
        print("2. Добавить вручную")
        print("3. Обновить данные")
        print("4. Поиск (по полю)")
        print("5. Удалить (по полю)")
        print("6. Выход")
        print("7. Поиск по шаблону (SQL)")
        print("8. Вставка/обновление (SQL процедура)")
        print("9. Массовая вставка пользователей (SQL)")
        print("10. Получить страницу с LIMIT/OFFSET")
        print("11. Удаление через SQL-процедуру")

        choice = input("Выберите действие: ")

        if choice == '1':
            path = input("Путь к CSV-файлу: ")
            insert_from_csv(path)
        elif choice == '2':
            insert_from_input()
        elif choice == '3':
            update_data()
        elif choice == '4':
            query_data()
        elif choice == '5':
            delete_data()
        elif choice == '6':
            break
        elif choice == '7':
            search_pattern()
        elif choice == '8':
            insert_or_update()
        elif choice == '9':
            insert_many()
        elif choice == '10':
            get_page()
        elif choice == '11':
            delete_user()
        else:
            print("Неверный ввод.")

    cur.close()
    conn.close()

if __name__ == "__main__":
    main()
