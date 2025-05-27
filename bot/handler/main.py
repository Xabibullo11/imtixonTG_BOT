from aiogram import html, Router, F
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types import Message, KeyboardButton
from aiogram.utils.i18n import gettext as _, lazy_gettext as __
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from bot.buttons.reply import main_menu_button, registration_button, contact_button
from bot.states import UserState
from db.model_func import add_user_to_db, select_user_from_db

main_router = Router()

@main_router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(_("Registratsia/Kirish"), reply_markup=registration_button())

@main_router.message(F.text.in_(["Registratsiya/Kirish", "Registration/login"]))
async def command_registration_handler(message: Message, state: FSMContext) -> None:
    if select_user_from_db(message.from_user.id):
        await message.answer(_("Asosiy menyu"), reply_markup=main_menu_button())
        return
    await state.set_state(UserState.name)
    await message.answer(_("Ismingizni kiriting"))

@main_router.message(UserState.name, F.text)
async def name_handler(message: Message, state: FSMContext) -> None:
    name = message.text
    await state.update_data({"name": name})
    await state.set_state(UserState.address)
    await message.answer(_("Addresingizni kiriting"))

@main_router.message(UserState.address, F.text)
async def name_handler(message: Message, state: FSMContext) -> None:
    address = message.text
    await state.update_data({"address": address})
    await state.set_state(UserState.contact)
    await message.answer(_("Telefon raqam kiriting"), reply_markup=contact_button())

@main_router.message(UserState.contact, F.contact)
async def name_handler(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    id_ = message.from_user.id
    name = data.get("name")
    address = data.get("address")
    contact = message.contact.phone_number

    add_user_to_db(id_, name, address, contact)

    await message.answer(_(""))
