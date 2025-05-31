from aiogram import html, Router, F
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types import Message, KeyboardButton
from aiogram.utils.i18n import gettext as _, lazy_gettext as __
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram import Router

from bot.buttons.reply import main_menu_button, book_catalog_button, badiiy_button, Ilmiy_ommabop_button, biznes_button, \
    choose_language_button

user_router = Router()

@user_router.message(F.text.in_(["⬅️ Orqaga (Asosiy menyuga qaytish)", "⬅️ Back (Back to Main Menu)"]))
async def command_start_handler(message: Message) -> None:
    await message.answer(_("Asosiy menyu"), reply_markup=main_menu_button())

@user_router.message(F.text.in_(["📕 Kitoblar katalogi", "⬅️ Orqaga (Kitoblar katalogiga qaytish)", "📕 Book catalog", "⬅️ Back (Back to Book catalog)"]))
async def restaurant_menu_handler(message: Message) -> None:
    await message.answer("Kitoblar katalogi", reply_markup=book_catalog_button())

@user_router.message(F.text.in_(["📕 Badiiy adabiyot", " 📕 artistic literary"]))
async def salats_handler(message: Message) -> None:
    await message.answer("📕 Badiiy adabiyot", reply_markup=badiiy_button())

@user_router.message(F.text.in_(["📖 Ilmiy-ommabop)", "📖 Popular science"]))
async def fastfood_handler(message: Message):
    await message.answer("📖 Ilmiy-ommabop)", reply_markup=Ilmiy_ommabop_button())

@user_router.message(F.text.in_(["📘 Biznes va rivojlanish", "📘 Business and development"]))
async def fastfood_handler(message: Message):
    await message.answer("📘 Biznes va rivojlanish", reply_markup=biznes_button())

@user_router.message(F.text.in_(["📞 Biz bilan bog'lanish", "📞 Connect with us"]))
async def connect_with_us(message: Message):
    await message.answer("📞 Contact: +998900613324\n📩 Email: xabibullo11@gmail.com")


@user_router.message(F.text.in_(["💬 Til o'zgartirish", "💬 Change language"]))
async def change_language_handler(message: Message):
    await message.answer(_("Til o'zgartirish"), reply_markup=choose_language_button())

@user_router.message(F.text.in_(["English", "Uzbek"]))
async def change_language_handler(message: Message, state: FSMContext, i18n):
    map_ = {
        "English": "en",
        "Uzbek": "uz"
    }

    lang = map_.get(message.text)
    await state.set_data({"locale": lang})
    i18n.current_locale = lang

    await message.answer(_("Asosiyy menyuu"), reply_markup=main_menu_button())



# ozgardi
