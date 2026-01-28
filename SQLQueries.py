def create_database(name):
    COMMAND = fr"""CREATE DATABASE {name};"""
    return COMMAND

def create_table(name):
    COMMAND = fr"""CREATE TABLE {name}
                (id int PRIMARY KEY,
                Название nvarchar(50) UNIQUE,
                [Тип (Овощ или фрукт)] nvarchar(50),
                Цвет nvarchar(30),
                Калорийность int,
                [Краткое описание] nvarchar(100));"""
    return COMMAND

def insert_data(table, columns, data):
    columns_str = ', '.join(columns)
    placeholders = ', '.join(['?'] * len(data))
    return f"INSERT INTO {table} ({columns_str}) VALUES ({placeholders})"


def get_all_data(name):
    COMMAND = fr"""SELECT * FROM {name};"""
    return COMMAND