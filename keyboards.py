from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Сгенерировать креативы
keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('Сгенерировать креативы 🤖')).add(KeyboardButton('Пополнить')).insert(KeyboardButton('Баланс'))

# Выберите вид креатива
keyboard2 = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
for i in ['Классический👨🏻‍⚕️', 'Товарный 💊', '◀️Назад', 'В начало🏠']:
    keyboard2.insert(KeyboardButton(i))

# Выберите категорию оффера
keyboard3 = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
for i in ['Похудение🍏', 'Паразиты🦠', 'Гипертония🫀', 'Диабет👅', 'Простатит🥚', 'Потенция🍌', 'Зрение👀', 'Суставы🦵🏻', 'Волосы🧔🏻‍♀', 'Омоложение👶🏻', '◀️Назад']:
    keyboard3.insert(KeyboardButton(i))

# Выберите ГЕО
keyboard4 = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
for g in ['Микс🫱🏾‍🫲🏽', 'Европа👨🏼', 'Латам👨🏽‍🦱', 'Африка🧑🏿‍🦱', 'Арабы👳🏾‍♂️', 'Азия👨🏽‍🦲', '◀️Назад', 'В начало🏠']:
    keyboard4.insert(KeyboardButton(g))

# Выберите язык
keyboard5 = ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
for k in ['RU🇷🇺', 'EN🇬🇧', 'ES🇪🇸', 'IT🇮🇹', 'BG🇧🇬', 'RO🇷🇴', 'CZ🇨🇿', 'FR🇫🇷', '◀️Назад', 'В начало🏠']:
    keyboard5.insert(KeyboardButton(k))
#keyboard4.insert(KeyboardButton('Назад'))
#keyboard4.insert(KeyboardButton('В начало'))

# Выберите размер пака
keyboard6 = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
for c in ['S pack\n(5 kreo)', 'M pack\n(10 kreo)', 'L pack\n(15 kreo)', '◀️Назад', 'В начало🏠']:
    keyboard6.insert(KeyboardButton(c))

# Выберите формат креативов
keyboard7 = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard7.add(KeyboardButton('↕️ Стандарт (две рамки)'))
for t, p in enumerate(['⬆️ Рамка сверху', ' ⬇️ Рамка снизу', '⬅️ Рамка слева', '➡️ Рамка справа', '◀️Назад', 'В начало🏠']):
    if t % 2 == 0:
        keyboard7.add(KeyboardButton(p))
    else:
        keyboard7.insert(KeyboardButton(p))
