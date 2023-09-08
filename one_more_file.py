import os
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import IDFilter
import zipfile
import chop
import tempfile
from keyboards import *
from configuration_file import TOKEN_API, list_of_appropriate_users


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

list_of_appropriate_users = list_of_appropriate_users
filter = IDFilter(list_of_appropriate_users)


async def on_startup(_):
    print('Bot has been switched on!')


@dp.message_handler(commands=['start'])
async def main(message: types.Message):
    if message.from_user.id in list_of_appropriate_users:
        await message.answer(text='Добро пожаловать в лучший генератор креативов на Нутру - KreoPic Bot 🤖\n\nЯ буду твоим верным помощником в заливах👾', reply_markup=keyboard1)
    #await message.answer(text=f'{message.from_user.id}', reply_markup=keyboard1)
    else:
        await message.answer(text='У вас нет доступа к боту 🔐')


@dp.message_handler(commands=['give'])
async def bot_start(message: types.Message):
    await bot.send_sticker(chat_id=message.from_user.id, sticker="CAACAgIAAxkBAAEKBMpk2i-xj81o4YuEuPHgEa8xX2KFTwAC6QEAAll7vwN8MkD8fnPP6TAE")


a = ''
choose = None
@dp.message_handler(filter)
async def main(message: types.Message):
    global a
    global choose

    if message.text == 'Сгенерировать креативы 🤖':
        a = ''
        choose = await bot.send_message(chat_id=message.chat.id, text='Выбери категорию оффера 🙇🏻‍♂️', reply_markup=keyboard3)
    elif message.text in ['Похудение🍏', 'Паразиты🦠', 'Гипертония🫀', 'Диабет👅', 'Простатит🥚', 'Потенция🍌', 'Зрение👀', 'Суставы🦵🏻', 'Волосы🧔🏻‍♀', 'Омоложение👶🏻']:
        a += message.text.rstrip('🍏🦠🫀👅🥚🍌👀🦵🏻🧔🏻‍♀👶🏻')
        print(a)
        #choose = await message.answer(text='Выбери вид креатива🤷🏻‍♂️', reply_markup=keyboard2)
        choose = await message.answer(text='Выбери ГЕО 🌎', reply_markup=keyboard4)
    elif message.text == 'Товарный 💊':
        #a += ', ' + message.text[:-2]
        a += ', ' + 'товарные'

        print(a)
        choose = await message.answer(text='Выбери размер пака 💁🏻‍♂️', reply_markup=keyboard6)
    elif message.text == 'Классический👨🏻‍⚕️':
        a += ', ' + message.text[:-5]
        print(a)
        choose = await message.answer(text='Выбери формат баннера👨🏻‍🔧', reply_markup=keyboard7)
    elif message.text in ['↕️ Стандарт (две рамки)', '⬆️ Рамка сверху', '⬇️ Рамка снизу', '⬅️ Рамка слева', '➡️ Рамка справа']:
        a += ', ' + message.text[3:]
        print(a)
        choose = await message.answer(text='Выбери размер пака 💁🏻‍♂️', reply_markup=keyboard6)
    elif message.text in ['Микс🫱🏾‍🫲🏽', 'Европа👨🏼', 'Латам👨🏽‍🦱', 'Африка🧑🏿‍🦱', 'Арабы👳🏾‍♂️', 'Азия👨🏽‍🦲']:
        a += ', ' + message.text.rstrip('🫱🏾‍🫲🏽👨🏼👨🏽‍🦱🧑🏿‍🦱👳🏾‍♂️👨🏽‍🦲')
        print(a)
        choose = await message.answer(text='Выбери язык 💆🏻‍♂️', reply_markup=keyboard5)
    elif message.text in ['RU🇷🇺', 'EN🇬🇧', 'ES🇪🇸', 'IT🇮🇹', 'BG🇧🇬', 'RO🇷🇴', 'CZ🇨🇿', 'FR🇫🇷']:
        a += ', ' + message.text[:-2]
        print(a)
        choose = await message.answer(text='Выбери вид креатива👨🏻‍💻', reply_markup=keyboard2)
    elif message.text in ['S pack\n(5 kreo)', 'M pack\n(10 kreo)', 'L pack\n(15 kreo)']:
        # sent_message = await bot.send_message(message.chat.id, text='Подождите немного, формируется ваш пак...')
        sent_message = await bot.send_sticker(chat_id=message.from_user.id,
                               sticker="CAACAgEAAxkBAAEKNcBk9GOLTc0Pbz3mSTj1cNDK6Kqm1gACLQIAAqcjIUQ9QDDJ7YO0tjAE")

        await bot.send_chat_action(message.chat.id, action=types.ChatActions.TYPING)  # отправляем "типинг"
        a += ', ' + message.text[0]
        print(a)

        archive_name = f'{a.split(", ")[-1]}-pack Kreopic.zip'
        # Мы будем в цикле создавать временные файлы, добавлять их в архив и закрывать и удалять их
        try:
            #sent_message = await bot.send_message(message.chat.id, text='Подождите немного, формируется ваш пак...')
            with zipfile.ZipFile(archive_name, 'w') as zipf:
                # Launch the cycle

                for i, k in enumerate(chop.zip_function(a)):
                    # Creating a tempfile
                    temp_file = tempfile.NamedTemporaryFile(suffix=".png", delete=False)
                    # Uploading our image into the tempfile
                    k.save(temp_file.name)
                    # Uploading the tempfile into the archive
                    zipf.write(temp_file.name, arcname=f"banner_kreopic_{i + 1}.png")
                    # Удаление временного файла
                    temp_file.close()
                    os.remove(temp_file.name)


            # Отправляем архив пользователю
            with open(archive_name, 'rb') as file:
                await bot.send_document(message.chat.id, file, caption='Твой пак готов!\nУспешных заливов💙', reply_markup=keyboard1)
                await sent_message.delete()
        except Exception as error:
            await sent_message.delete()
            await bot.send_message(message.chat.id, text='Выбирайте пока только похудение на испанском!', reply_markup=keyboard1)
            print('Ошибка: ' + str(error))

        # Удаляем архив после отправки
        if os.path.exists(archive_name):
            os.remove(archive_name)
    elif choose and message.text in ['◀️Назад', 'В начало🏠']:
        if message.text == '◀️Назад':
            await message.delete()
            if choose.text == 'Выбери категорию оффера 🙇🏻‍♂️':
                choose = await bot.send_message(message.chat.id,
                                                text='Добро пожаловать в лучший генератор креативов на Нутру - KreoPic Bot 🤖\n\nЯ буду твоим верным помощником в заливах👾',
                                                reply_markup=keyboard1)

            elif choose.text == 'Выбери вид креатива👨🏻‍💻':
                choose = await message.answer(text='Выбери язык 💆🏻‍♂️', reply_markup=keyboard5)

            elif choose.text == 'Выбери ГЕО 🌎':
                choose = await bot.send_message(chat_id=message.chat.id, text='Выбери категорию оффера 🙇🏻‍♂️',
                                                reply_markup=keyboard3)

            elif choose.text == 'Выбери язык 💆🏻‍♂️':
                choose = await bot.send_message(message.chat.id, text='Выбери ГЕО 🌎',
                                                reply_markup=keyboard4)

            elif choose.text == 'Выбери размер пака 💁🏻‍♂️' and a.split(', ')[-1] == 'товарные':
                choose = await message.answer(text='Выбери вид креатива👨🏻‍💻', reply_markup=keyboard2)
            elif choose.text == 'Выбери размер пака 💁🏻‍♂️':
                choose = await message.answer(text='Выбери формат баннера👨🏻‍🔧', reply_markup=keyboard7)
            elif choose.text == 'Выбери формат баннера👨🏻‍🔧':
                choose = await bot.send_message(message.chat.id, text='Выбери вид креатива👨🏻‍💻', reply_markup=keyboard2)
            a = ', '.join(a.split(', ')[:-1])
        elif message.text == 'В начало🏠':
            a = ''
            choose = await bot.send_message(message.chat.id,
                                            text='Добро пожаловать в лучший генератор креативов на Нутру - KreoPic Bot 🤖\n\nЯ буду твоим верным помощником в заливах👾',
                                            reply_markup=keyboard1)
        print(a)
    else:
        #await bot.send_sticker(message.from_user.id, sticker='CAACAgIAAxkBAAEKCJBk27zIuale7D5Iz_Z81pwKENCIBAAC5AEAAll7vwPhXL60VTV21DAE')
        choose = await bot.send_message(message.chat.id, text='Нихуя не понял, но очень интересно!', reply_markup=keyboard1)
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

# Все что готово из нового на данный момент - формирование строки. Так же разумеется есть блок кода создающий архив и кладущий в него файлы изображений.
# Сейчас неприятная задача - построить правильную папочную структуру
# Папочная структура построена четко по чертежу. Дальше мне надо оформить верную цепочку действий с кнопками Назад и В начало
# Цепочка действий готова, следующим шагом начинаем работу... Придется путешествовать по папкам с помощью модуля os. Надо будет продумать работу
# со всеми алгоритмами и создать адаптивные функции для создания изображений.



# Нужно будет вспомнить работу с ГИТ
# Сука, попались два одинаковых текста...
