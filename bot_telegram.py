from aiogram.utils import executor

from create_bot import dp
from handlers import client, admin, other

import datetime


dt = datetime.datetime.now()
dt_string_format = dt.strftime("Date %d.%m.%Y time: %H:%M")

async def on_startup(_):
    print(f'\nBot started\n\nstatus - Online\ntime statted - {dt_string_format}')


client.register_client_handlers(dp)
admin.register_admin_handlers(dp)
other.register_other_hanlers(dp)

executor.start_polling(
    dp, 
    skip_updates=True,
    on_startup=on_startup
)