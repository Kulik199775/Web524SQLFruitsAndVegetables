import os
from dotenv import load_dotenv
import pyodbc

import SQLQueries

load_dotenv()

DRIVER = os.getenv('MS_SQL_DRIVER')
SERVER = os.getenv('MS_SQL_SERVER')
PAD_DATABASE = os.getenv('MS_SQL_PAD_DATABASE')
DATABASE = os.getenv('MS_SQL_PAD_DATABASE')
USER = os.getenv('MS_SQL_USER')
PASSWORD = os.getenv('MS_SQL_KEY')

connection_string = f"""DRIVER={{SQL Server}};
                        SERVER={SERVER};
                        DATABASE={PAD_DATABASE};
                        UID={USER};
                        PWD={PASSWORD};"""

"""Создание базы данных"""
created_db = 'FruitsAndVegetables'
conn = pyodbc.connect(connection_string)
conn.autocommit = True

try:
    SQL_QUERY = SQLQueries.create_database(created_db)
    conn.execute(SQL_QUERY)
except pyodbc.ProgrammingError as ex:
    print(ex)
else:
    print(f'База данных {created_db} успешно создана!')
finally:
    conn.close()

"""Создание таблицы"""
conn = pyodbc.connect(connection_string)
conn.autocommit = True
cursor = conn.cursor()
activ_db_name = 'FruitsAndVegetables'
table_name = 'FruitsAndVegetables'

try:
    SQL_QUERY = SQLQueries.create_table(table_name)
    cursor.execute(fr'USE {activ_db_name};')
    cursor.execute(SQL_QUERY)
except pyodbc.ProgrammingError as ex:
    print(ex)
else:
    print(f'Таблица {table_name} успешно создана!')
finally:
    conn.close()

"""Заполнение таблицы данными"""

conn = pyodbc.connect(connection_string)
conn.autocommit = True
cursor = conn.cursor()
activ_db_name = 'FruitsAndVegetables'
table_name = 'FruitsAndVegetables'
columns = ['id', 'Название', '[Тип (Овощ или фрукт)]', 'Цвет', 'Калорийность', '[Краткое описание]']
all_data = [(1, 'Яблоко', 'Фрукт', 'Зеленый', 52, 'Сладкий фрукт с хрустящей мякотью'),
            (2, 'Банан', 'Фрукт', 'Желтый', 89, 'Мягкий сладкий фрукт'),
            (3, 'Морковь', 'Овощ', 'Оранжевый', 41, 'Хрустящий корнеплод'),
            (4, 'Огурец', 'Овощ', 'Зеленый', 15, 'Сочный овощ с высоким содержанием воды'),
            (5, 'Апельсин', 'Фрукт', 'Оранжевый', 47, 'Цитрусовый фрукт, много витамина С'),
            (6, 'Картофель', 'Овощ', 'Коричневый', 77, 'Крахмалистый клубень'),
            (7, 'Виноград', 'Фрукт', 'Зеленый', 69, 'Сладкие маленькие ягоды'),
            (8, 'Брокколи', 'Овощ', 'Зеленый', 34, 'Овощ из семейства капустных'),
            (9, 'Клубника', 'Фрукт', 'Красный', 32, 'Сладкая ароматная ягода'),
            (10, 'Помидор', 'Овощ', 'Красный', 18, 'Плод из семейства пасленовых')]
try:
    cursor.execute(fr'USE {activ_db_name};')
    for data in all_data:
        SQL_query = SQLQueries.insert_data(table_name, columns, data)
        cursor.execute(SQL_query, data)
except pyodbc.ProgrammingError as ex:
    print(ex)
except pyodbc.IntegrityError as er:
    print(er)
else:
    print(f'Таблица {table_name} успешно заполнена!')
finally:
    conn.close()

"""Вывод данных из БД"""
conn = pyodbc.connect(connection_string)
conn.autocommit = True
cursor = conn.cursor()
activ_db_name = 'FruitsAndVegetables'
table_name = 'FruitsAndVegetables'
data_list = []

try:
    SQL_QUERY = SQLQueries.get_all_data(table_name)
    cursor.execute(fr'USE {activ_db_name};')
    result = cursor.execute(SQL_QUERY)
except pyodbc.ProgrammingError as ex:
    print(ex)
else:
    records = result.fetchall()
    for record in records:
        data_dict = {'id': record[0], 'Название':record[1], 'Тип (Овощ или фрукт)': record[2], 'Цвет': record[3], 'Калорийность': record[4], 'Краткое описание': record[5]}
        data_list.append(data_dict)
finally:
    conn.close()

