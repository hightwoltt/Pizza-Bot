from create_bot import bot, dp

import sqlite3 as sq


# Create a database table
def sql_start():
    global base, cur
    base = sq.connect('3,14zza.db')
    cur = base.cursor()
    
    if base:
        print('\n****** Data base connected ******\n')

        base.execute('CREATE TABLE IF NOT EXISTS classes(id PRIMARY KEY,\
            class TEXT)')

        base.execute('CREATE TABLE IF NOT EXISTS client(id PRIMARY KEY, name,\
            status_id INTEGER, adress TEXT, phone_number TEXT,\
            FOREIGN KEY(status_id) REFERENCES statuses(id))'
        )

        base.execute('CREATE TABLE IF NOT EXISTS orders(id PRIMARY KEY,\
            client_id INTEGER, position_id INTEGER,\
                FOREING KEY(client_id REFERENCES client(id),\
                FOREING KEY(position_id) REFERENCES position(id)))'
        )

        base.execute('CREATE TABLE IF NOT EXISTS payment_history(id PRIMARY KEY,\
            order_id INTEGER, datetime INTEGER, sum INTEGER,\
            FOREING KEY(order_id) REFERENCES orders(id))'
        )

        base.execute('CREATE TABLE IF NOT EXISTS position(id PRIMARY KEY,\
            photo TEXT, name TEXT, desctiption TEXT, price INTEGER,\
            class_id INTEGER, FOREING KEY(class_id) REFERENCES classes(id))'
        )

        base.execute('CREATE TABLE IF NOT EXISTS statuses(id PRIMARY KEY,\
            client_status TEXT)'
        )

        base.commit()
        print('\n****** Data status << OK >> ******\n')


#                                                   #
#                                                   # 
#                                                   # 
# ПЕРЕПИСАТЬ НАХУЙ ФУНКЦИИ SQL_ADD, SQL_READ !!!!!! #
#                                                   # 
#                                                   # 
#                                                   #   


# # Insert to database command
# async def sql_add_command(state):
#     async with state.proxy() as data:
#         cur.execute('INSERT INTO menu VALUES (?, ?, ?, ?)', tuple(data.values()))
#         base.commit()


# Full menu output command 
async def sql_read(message):
    for position in cur.execute('SELECT name, description, cls.class, price \
        FROM position AS p JOIN classes AS cls ON p.class_id = cls.id')\
            .fetchall():
        await bot.send_message(message.from_user.id, position[0],
                f'{position[1]}\n \
                \Класс: {position[2]}\n \
                \nЦена - {position[3]}'
        )     


# Drinks menu output command
async def sql_read(message):
    for position in cur.execute('SELECT name, description, cls.class, price \
        FROM position AS p JOIN classes AS cls ON p.class_id = cls.id WHERE\
            cls.class = Напитки').fetchall():
        await bot.send_message(message.from_user.id, position[0],
                f'{position[1]}\n \
                \Класс: {position[2]}\n \
                \nЦена - {position[3]}'
        )     
        

# Eat menu output command
async def sql_read(message):
    for position in cur.execute('SELECT name, description, cls.class, price \
        FROM position AS p JOIN classes AS cls ON p.class_id = cls.id WHERE\
            cls.class = Еда').fetchall():
        await bot.send_message(message.from_user.id, position[0],
                f'{position[1]}\n \
                \Класс: {position[2]}\n \
                \nЦена - {position[3]}'
        )