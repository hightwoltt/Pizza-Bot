from create_bot import bot, dp

import sqlite3 as sq


# Create a database table
def sql_start():
    global base, cur
    base = sq.connect('3,14zza.db')
    cur = base.cursor()
    
    if base:
        print('\n****** Data base connected ******\n')

        base.execute('CREATE TABLE IF NOT EXISTS client(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)')
        base.execute('CREATE TABLE IF NOT EXISTS statuses(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)')
        base.execute('CREATE TABLE IF NOT EXISTS order(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)')
        base.execute('CREATE TABLE IF NOT EXISTS positions(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)')
        base.execute('CREATE TABLE IF NOT EXISTS payment_history(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)')
        base.execute('CREATE TABLE IF NOT EXISTS classes(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)')

        base.commit()
        print('\n****** Data status << OK >> ******\n')


# Insert to database command
async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO menu VALUES (?, ?, ?, ?)', tuple(data.values()))
        base.commit()


# Full menu output command
async def sql_read(message):
    for position in cur.execute('SELECT * FROM menu').fetchall():
        await bot.send_photo(message.from_user.id, position[0],
                f'{position[1]}\n \
                \nОписание: {position[2]}\n \
                \nЦена - {position[3]}'
        )
        


def sql_start_drinks():
    global base, cur
    base = sq.connect('3,14zza.db')
    cur = base.cursor()
    
    if base:
        print('\n****** Data base connected ******\n')
    base.execute('CREATE TABLE IF NOT EXISTS drinks(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)')
    base.commit()


# Drinks menu output command
async def sql_read(message):
    for position in cur.execute('SELECT * FROM menu').fetchall():
        await bot.send_photo(message.from_user.id, position[0],
                f'{position[1]}\n \
                \nОписание: {position[2]}\n \
                \nЦена - {position[3]}'
        )     
        

def sql_start_eat():
    global base, cur
    base = sq.connect('3,14zza.db')
    cur = base.cursor()
    
    if base:
        print('\n****** Data base connected ******\n')
    base.execute('CREATE TABLE IF NOT EXISTS eat(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)')
    base.commit()


# Eat menu output command
async def sql_read(message):
    for position in cur.execute('SELECT * FROM menu').fetchall():
        await bot.send_photo(message.from_user.id, position[0],
                f'{position[1]}\n \
                \nОписание: {position[2]}\n \
                \nЦена - {position[3]}'
        )