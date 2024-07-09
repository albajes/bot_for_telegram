import time

from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

from middleware import UserCheckMiddleware
from settings import MacroserverURLS, NA_YASNOY
from methods import set_value_to_true, set_value_to_none

router = Router()
router.message.middleware(UserCheckMiddleware())


main_keyboard = ReplyKeyboardMarkup(
            keyboard=[[KeyboardButton(text='На ясной'),
                       KeyboardButton(text='Остальные объекты')]],
            resize_keyboard=True,
            input_field_placeholder='Выберите объект')


@router.message(Command('start'))
async def first_handler(msg: Message):
    await msg.answer(f'Привет, <b>{msg.from_user.username}</b>', reply_markup=main_keyboard)


@router.message(F.text.lower() == 'в начало')
async def back_to_start(msg: Message):
    await msg.answer(text='Выберите объект', reply_markup=main_keyboard)


@router.message(F.text.lower() == 'на ясной')
async def working_na_yasnoy(msg: Message):
    kb = [
        [KeyboardButton(text='Принимать заявки "На ясной"'),
         KeyboardButton(text='Не принимать заявки "На ясной"')],
        [KeyboardButton(text='В начало')]
    ]
    keyboard = ReplyKeyboardMarkup(
                    keyboard=kb,
                    resize_keyboard=True,
                    input_field_placeholder='Выберите кнопку'
                )
    await msg.answer(f'Вы выбрали "{msg.text}"', reply_markup=keyboard)


@router.message(F.text.lower() == 'остальные объекты')
async def working_other_objects(msg: Message):
    kb = [
        [KeyboardButton(text='Принимать заявки'),
         KeyboardButton(text='Не принимать заявки')],
        [KeyboardButton(text='В начало')]
    ]
    keyboard = ReplyKeyboardMarkup(
                    keyboard=kb,
                    resize_keyboard=True,
                    input_field_placeholder='Выберите кнопку'
                )
    await msg.answer(f'Вы выбрали "{msg.text}"', reply_markup=keyboard)


@router.message(F.text.lower() == 'принимать заявки')
async def accept(msg: Message):
    await msg.reply('Буквально минутку...', reply_markup=ReplyKeyboardRemove())
    for url in MacroserverURLS:
        await set_value_to_true(username=msg.from_user.username, url=url.value)
    await msg.answer('Спасибо за ожидание! Теперь вы принимаете заявки', reply_markup=main_keyboard)


@router.message(F.text.lower() == 'не принимать заявки')
async def reject(msg: Message):
    await msg.reply('Буквально минутку...', reply_markup=ReplyKeyboardRemove())
    for url in MacroserverURLS:
        await set_value_to_none(username=msg.from_user.username, url=url.value)
    await msg.answer('Спасибо за ожидание! Теперь вы не принимаете заявки', reply_markup=main_keyboard)


@router.message(F.text.lower() == 'принимать заявки "на ясной"')
async def accept_na_yasnoy(msg: Message):
    await msg.reply('Пару секунд...', reply_markup=ReplyKeyboardRemove())
    await set_value_to_true(username=msg.from_user.username, url=NA_YASNOY)
    await msg.reply('Вы принимаете заявки "На ясной"', reply_markup=main_keyboard)


@router.message(F.text.lower() == 'не принимать заявки "на ясной"')
async def reject_na_yasnoy(msg: Message):
    await msg.reply('Пару секунд...', reply_markup=ReplyKeyboardRemove())
    await set_value_to_none(username=msg.from_user.username, url=NA_YASNOY)
    await msg.reply('Вы не принимаете заявки "На ясной"', reply_markup=main_keyboard)

