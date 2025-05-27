from bot.dispatcher import dp
from bot.handler.main import *
from bot.handler.user import *


dp.include_routers(*[main_router, user_router])