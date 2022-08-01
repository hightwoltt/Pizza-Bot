import sqlite3 as sq

def sql_start():
    global base, cur
    base = sq.connect('3,14zza.db')
    cur = base.cursor()
    
    if base:
        print('\n****** Data base connected ******\n')
    base.execute('CREATE TABLE IF NOT EXISTS menu(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)')
    base.commit()


async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO menu VALUES (?, ?, ?, ?)', tuple(data.values()))
        base.commit()