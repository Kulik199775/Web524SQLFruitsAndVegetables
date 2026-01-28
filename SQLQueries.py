def create_database(name):
    COMMAND = fr'CREATE DATABASE {name};'
    return COMMAND

def create_table(name):
    COMMAND = fr"""CREATE TABLE {name}
                (id int PRIMARY KEY,
                Название nvarchar(50) UNIQUE,
                Тип (Овощ или фрукт) nvarchar(50),
                Цвет nvarchar(30),
                Калорийность int,
                Краткое описание nvarchar(100)"""
    return COMMAND

def insert_data(table, columns, data):
    COMMAND = fr"""INSERT INTO {table} {columns}
                    VALUES
                    {data}"""
    return COMMAND