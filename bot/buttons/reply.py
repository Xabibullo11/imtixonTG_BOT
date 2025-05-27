from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.utils.i18n import gettext as _

def registration_button():
    rkb = ReplyKeyboardBuilder()
    rkb.add(*[
        KeyboardButton(text=_("Registratsiya/Kirish")),
    ])

    rkb.adjust(1)

    return rkb.as_markup(resize_keyboard=True)

def contact_button():
    rkb = ReplyKeyboardBuilder()
    rkb.add(*[
        KeyboardButton(text=_("Telefon raqam yuborish"), request_contact=True)
    ])

    rkb.adjust(1)

    return rkb.as_markup(resize_keyboard=True)

def main_menu_button():
    rkb = ReplyKeyboardBuilder()
    rkb.add(*[
        KeyboardButton(text=_("🍽 Restoran menyusi")),
        KeyboardButton(text=_("📞 Biz bilan bog'lanish")),
        KeyboardButton(text=_("💬 Til o'zgartirish"))
    ])

    rkb.adjust(1)

    return rkb.as_markup(resize_keyboard=True)

def restaurant_menu_button():
    rkb = ReplyKeyboardBuilder()
    rkb.add(*[
        KeyboardButton(text=_("🥙 Salatlar (Taom Tanlash)")),
        KeyboardButton(text=_("🍕 Fast Food (Taom Tanlash)")),
        KeyboardButton(text=_("🍜 Issiq taomlar (Taom Tanlash)")),
        KeyboardButton(text=_("⬅️ Orqaga (Asosiy menyuga qaytish)")),
    ])

    rkb.adjust(1)

    return rkb.as_markup(resize_keyboard=True)

def salats_button():
    rkb = ReplyKeyboardBuilder()
    rkb.add(*[
        KeyboardButton(text="Sezar salati"),
        KeyboardButton(text="Olivye salati"),
        KeyboardButton(text="⬅️ Orqaga (Restoran menyusiga qaytish)"),
        KeyboardButton(text="🍕 Fast Food (Taom Tanlash)")
    ])

    rkb.adjust(1)

    return rkb.as_markup(resize_keyboard=True)

def fastfood_button():
    rkb = ReplyKeyboardBuilder()
    rkb.add(*[
        KeyboardButton(text=_("Burger")),
        KeyboardButton(text=_("Hot-dog")),
        KeyboardButton(text=_("⬅️ Orqaga (Restoran menyusiga qaytish)")),
        KeyboardButton(text=_("🍜 Issiq taomlar (Taom Tanlash)"))
    ])

    rkb.adjust(1)

    return rkb.as_markup(resize_keyboard=True)

def dish_button():
    rkb = ReplyKeyboardBuilder()
    rkb.add(*[
        KeyboardButton(text=_("osh")),
        KeyboardButton(text=_("Sho'rva")),
        KeyboardButton(text=_("⬅️ Orqaga (Restoran menyusiga qaytish)"))
    ])

    rkb.adjust(1)

    return rkb.as_markup(resize_keyboard=True)

def choose_language_button():
    rkb = ReplyKeyboardBuilder()
    rkb.add(*[
        KeyboardButton(text="English"),
        KeyboardButton(text="Uzbek")
    ])

    rkb.adjust(2)

    return rkb.as_markup(resize_keyboard=True)
