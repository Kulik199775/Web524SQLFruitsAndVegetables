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
                        PWD={PASSWORD}"""

# """Создание базы данных"""
# created_db = 'FruitsAndVegetables'
# conn = pyodbc.connect(connection_string)
# conn.autocommit = True
#
# try:
#     SQL_QUERY = SQLQueries.create_database(created_db)
#     conn.execute(SQL_QUERY)
# except pyodbc.ProgrammingError as ex:
#     print(ex)
# else:
#     print(f'База данных {created_db} успешно создана!')
# finally:
#     conn.close()

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