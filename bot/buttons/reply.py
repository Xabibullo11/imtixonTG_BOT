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
        KeyboardButton(text=_("📕 Kitoblar katalogi")),
        KeyboardButton(text=_("📞 Aloqa")),
        KeyboardButton(text=_("💬 Til o'zgartirish"))
    ])

    rkb.adjust(1)

    return rkb.as_markup(resize_keyboard=True)

def book_catalog_button():
    rkb = ReplyKeyboardBuilder()
    rkb.add(*[
        KeyboardButton(text=_("📕 Badiiy adabiyot ")),
        KeyboardButton(text=_("📖 Ilmiy-ommabop ")),
        KeyboardButton(text=_("📘 Biznes va rivojlanish ")),
        KeyboardButton(text=_("⬅️ Orqaga (Asosiy menyuga qaytish)")),
    ])

    rkb.adjust(1)

    return rkb.as_markup(resize_keyboard=True)

def badiiy_button():
    rkb = ReplyKeyboardBuilder()
    rkb.add(*[
        KeyboardButton(text="📕O'tkan kunlar - Abdulla Qodiriy"),
        KeyboardButton(text="📕Mehrobdan chyon - Cho'lpon"),
        KeyboardButton(text="⬅️ Orqaga (Kitoblar katalogiga qaytish)")
    ])

    rkb.adjust(1)

    return rkb.as_markup(resize_keyboard=True)

def Ilmiy_ommabop_button():
    rkb = ReplyKeyboardBuilder()
    rkb.add(*[
        KeyboardButton(text=_("📖Qiziqarli fizika - Perelman")),
        KeyboardButton(text=_("📖Tibbiyot mo'jizalari - David Agus")),
        KeyboardButton(text=_("⬅️ Orqaga (Kitoblar katalogiga qaytish)"))
    ])

    rkb.adjust(1)

    return rkb.as_markup(resize_keyboard=True)

def biznes_button():
    rkb = ReplyKeyboardBuilder()
    rkb.add(*[
        KeyboardButton(text=_("📘Boy ota, kambag'al ota - Robert Kiyosaki")),
        KeyboardButton(text=_("📘Muvaffaqiyat odatlari - Stephen Covey")),
        KeyboardButton(text=_("⬅️ Orqaga (Kitoblar katalogiga qaytish)"))
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
