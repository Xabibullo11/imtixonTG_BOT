from aiogram import html, Router, F
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types import Message, KeyboardButton
from aiogram.utils.i18n import gettext as _, lazy_gettext as __
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram import Router

from bot.buttons.reply import main_menu_button, restaurant_menu_button, salats_button, fastfood_button, dish_button, \
    choose_language_button

user_router = Router()

@user_router.message(F.text.in_(["⬅️ Orqaga (Asosiy menyuga qaytish)", "⬅️ Back (Back to Main Menu)"]))
async def command_start_handler(message: Message) -> None:
    await message.answer(_("Asosiy menyu"), reply_markup=main_menu_button())

@user_router.message(F.text.in_(["🍽 Restoran menyusi", "⬅️ Orqaga (Restoran menyusiga qaytish)", "🍽 Restaurant menu", "⬅️ Back (Back to Restaurant Menu)"]))
async def restaurant_menu_handler(message: Message) -> None:
    await message.answer("Restoran menyusi", reply_markup=restaurant_menu_button())

@user_router.message(F.text.in_(["🥙 Salatlar (Taom Tanlash)", "🥙 Salats (Choose Food)"]))
async def salats_handler(message: Message) -> None:
    await message.answer("🥙 Salatlar (Taom Tanlash)", reply_markup=salats_button())

@user_router.message(F.text.in_(["🍕 Fast Food (Taom Tanlash)", "🍕 Fast Food (Choose Food)"]))
async def fastfood_handler(message: Message):
    await message.answer("🍕 Fast Food (Taom Tanlash)", reply_markup=fastfood_button())

@user_router.message(F.text.in_(["🍜 Issiq taomlar (Taom Tanlash)", "🍜 Dishes (Choose dish)"]))
async def fastfood_handler(message: Message):
    await message.answer("🍜 Issiq taomlar (Taom Tanlash)", reply_markup=dish_button())

@user_router.message(F.text.in_(["📞 Biz bilan bog'lanish", "📞 Connect with us"]))
async def connect_with_us(message: Message):
    await message.answer("📞 Contact: +998503002292\n📩 Email: usmanovj161@gmail.com")


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

    await message.answer(_("Asosiy menyu"), reply_markup=main_menu_button())




