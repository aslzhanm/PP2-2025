import psycopg2
import csv

# Подключение к базе данных
conn = psycopg2.connect(
    dbname='postgres',
    user='postgres',
    password='asyl',
    host='localhost',
    port='5432'
)
cur = conn.cursor()

# Создание таблицы
def create_table():
    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            phone VARCHAR(20)
        );
    """)
    conn.commit()

# Вставка данных из CSV
def insert_from_csv(file_path):
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # пропустить заголовок
        for row in reader:
            cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (row[0], row[1]))
    conn.commit()
    print("Данные из CSV загружены.")

# Ввод с консоли
def insert_from_input():
    name = input("Введите имя: ")
    phone = input("Введите номер: ")
    cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    print("Данные добавлены.")

# Обновление данных
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

# Поиск с фильтром
def query_data():
    field = input("Фильтровать по (name/phone): ")
    value = input("Введите значение для поиска: ")
    cur.execute(f"SELECT * FROM phonebook WHERE {field} ILIKE %s", (f"%{value}%",))
    rows = cur.fetchall()
    for row in rows:
        print(row)

# Удаление
def delete_data():
    field = input("Удалить по (name/phone): ")
    value = input("Введите значение: ")
    cur.execute(f"DELETE FROM phonebook WHERE {field} = %s", (value,))
    conn.commit()
    print("Запись удалена.")

# Главное меню
def main():
    create_table()
    while True:
        print("\n1. Добавить из CSV\n2. Добавить вручную\n3. Обновить\n4. Поиск\n5. Удалить\n6. Выйти")
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
        else:
            print("Неверный ввод.")

    cur.close()
    conn.close()

if __name__ == "__main__":
    main()
