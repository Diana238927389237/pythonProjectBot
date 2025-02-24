from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton

startMenu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Рандом'),
            KeyboardButton(text='Меню'),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=False,
    input_field_placeholder='Начальное меню'
)

subMenu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Выбрать жанр'),
            KeyboardButton(text='Информация'),
        ],
        [
            KeyboardButton(text='Назад')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=False,
    input_field_placeholder='Подменю'
)

urlsMenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Сайт', url='https://lib.itmo.ru/'),
            InlineKeyboardButton(text='Tg',   url='tg://resolve?domain=ИТМО Библиотека')
        ]
    ]
)
