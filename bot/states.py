from aiogram.fsm.state import StatesGroup, State


class UserState(StatesGroup):
    name = State()
    address = State()
    contact = State()

