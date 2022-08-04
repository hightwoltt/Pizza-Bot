from aiogram.utils import executor

from create_bot import dp
from handlers import client, admin, other
from data_base import sql_base

import datetime


dt = datetime.datetime.now()
dt_string_format = dt.strftime("Date %d.%m.%Y time: %H:%M")

# Print bot status 
async def on_startup(_):

    sql_base.sql_start()
    print(f'\nBot started\n\
        \nstatus - Online\
        \ntime statted - {dt_string_format}')


# Reegister all handlers
client.register_client_handlers(dp)
admin.register_admin_handlers(dp)
other.register_other_hanlers(dp)

# Start polling
executor.start_polling(
    dp, 
    skip_updates=True,
    on_startup=on_startup
)