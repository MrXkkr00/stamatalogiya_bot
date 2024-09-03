from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

bosh_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📝Qabulga yozilish"),
        ],
        [
            KeyboardButton(text="📲️Kontaktlar"),
            KeyboardButton(text="📍Lokatsiya")
        ],
        [
            KeyboardButton(text="💵Bonuslarim"),
            KeyboardButton(text="📝Navbatim"),
            KeyboardButton(text="🇷🇺Русский")
        ],

    ],resize_keyboard=True
)

bosh_menu_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📝Записаться на приём")
        ],
        [
            KeyboardButton(text="📲️Контакты", ),
            KeyboardButton(text="📍Локация")
        ],
        [
            KeyboardButton(text="💵Мои бонусы"),
            KeyboardButton(text="📝Моя очередь"),
            KeyboardButton(text="🇺🇿Uzbek")
        ],

    ], resize_keyboard=True
)

til_tanlash = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🇺🇿Uzbek"),
            KeyboardButton(text="🇷🇺Русский")
        ],

    ], resize_keyboard=True
)

contact_keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                               keyboard=[
                                   [
                                       KeyboardButton(text="📱Kontakt",
                                                      request_contact=True)
                                   ]
                               ])


contact_keyboard_ru = ReplyKeyboardMarkup(resize_keyboard=True,
                               keyboard=[
                                   [
                                       KeyboardButton(text="📱Контакт",
                                                      request_contact=True)
                                   ]
                               ])


bosh_m = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🏠Bosh Menu"),
        ],

    ], resize_keyboard=True
)


bosh_m_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🏠Главное меню"),
        ],

    ], resize_keyboard=True
)


davom = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Davom ettirish"),
        ],

    ], resize_keyboard=True
)

admin_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="/navbat"),
            KeyboardButton(text="/bonus"),
        ],
        [
            KeyboardButton(text="/exel"),
            KeyboardButton(text="/band_qilish"),
        ],
        [
            KeyboardButton(text="/Eslatma"),
        ],
    ], resize_keyboard=True
)

admin_admin = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="/admin"),
        ],
    ], resize_keyboard=True
)