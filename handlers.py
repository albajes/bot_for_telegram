from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


from settings import MacroserverURLS, USERS, MEMBERS, MAIN_LOGIN, MAIN_PASSWORD, LOGIN_URL, NA_YASNOY
from selenium import webdriver
router = Router()

main_keyboard = ReplyKeyboardMarkup(
            keyboard=[[KeyboardButton(text='На ясной'),
                       KeyboardButton(text='Остальные объекты')]],
            resize_keyboard=True,
            input_field_placeholder='Выберите объект')


@router.message(Command('start'))
async def first_handler(msg: Message):
    if msg.from_user.username not in USERS:
        await msg.answer('Вы не зарегистрированы в системе, '
                         'обратитесь к администратору для добавления вас в список пользователей')
    else:
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
        [KeyboardButton(text='В начало', callback_data='start')]
    ]
    keyboard = ReplyKeyboardMarkup(
                    keyboard=kb,
                    resize_keyboard=True,
                    input_field_placeholder='Выберите кнопку'
                )
    await msg.answer(f'Вы выбрали "{msg.text}"', reply_markup=keyboard)


@router.message(F.text.lower() == 'принимать заявки')
async def accept(msg: Message):
    await msg.reply('Минутку...')
    await change_value(msg)
    await msg.answer('Теперь вы принимаете заявки')


@router.message(F.text.lower() == 'не принимать заявки')
async def reject(msg: Message):
    await msg.reply('Минутку...')
    await change_value(msg)
    await msg.answer('Теперь вы не принимаете заявки')


@router.message(F.text.lower() == 'принимать заявки "на ясной"')
async def accept_na_yasnoy(msg: Message):
    await msg.reply('Минутку...')
    driver = await login_in_macroserver()
    value = await check_mark(username=msg.from_user.username, driver=driver, url=NA_YASNOY)
    if value:
        await msg.reply('Вы уже принимаете заявки "На ясной"')
    else:
        await click_and_save(driver=driver, username=msg.from_user.username)
        await msg.reply('Теперь вы принимаете заявки "На ясной"')


@router.message(F.text.lower() == 'не принимать заявки "на ясной"')
async def reject_na_yasnoy(msg: Message):
    await msg.reply('Минутку...')
    driver = await login_in_macroserver()
    value = await check_mark(username=msg.from_user.username, driver=driver, url=NA_YASNOY)
    if value is None:
        await msg.reply('Вы уже не принимаете заявки "На ясной"')
    else:
        await click_and_save(driver=driver, username=msg.from_user.username)
        await msg.reply('Теперь вы не принимаете заявки "На ясной"')


async def change_value(msg: Message):
    driver = await login_in_macroserver()
    for url in MacroserverURLS:
        await set_value(username=msg.from_user.username, driver=driver, url=url.value)


async def set_value(url, username: str, driver: webdriver) -> None:
    value = await check_mark(driver=driver, username=username, url=url)
    if value is None:
        await click_and_save(driver=driver, username=username)


async def login_in_macroserver() -> webdriver:
    options = Options()
    options.add_argument('--headless=new')
    driver = webdriver.Chrome(options=options)
    driver.get(LOGIN_URL)
    login_element = driver.find_element(By.CLASS_NAME, 'form-control')
    login_element.send_keys(MAIN_LOGIN)
    password_element = driver.find_element(By.NAME, 'password')
    password_element.send_keys(MAIN_PASSWORD)
    button_element = driver.find_element(By.XPATH, "//button[@type='submit']")
    button_element.click()
    return driver


async def check_mark(username: str, driver: webdriver, url: str) -> bool | None:
    driver.get(url)
    distribution_button = driver.find_elements(By.XPATH, '//select')
    select = Select(distribution_button[17])
    select.select_by_value('round_robin')
    button_element_of_members = driver.find_elements(By.XPATH, "//div[@class='ui-multiselect']")
    button_element_of_members[7].click()
    button_element_check = driver.find_element(By.XPATH, f"//input[@type='checkbox'][@value='{MEMBERS[username]}']")
    value = button_element_check.get_attribute('checked')
    return value


async def click_and_save(driver: webdriver, username: str) -> None:
    button_element_check = driver.find_element(By.XPATH, f"//input[@type='checkbox'][@value='{MEMBERS[username]}']")
    button_element_check.click()
    button_element_save = driver.find_element(By.XPATH, "//button[@type='submit'][@class='btn btn-success m-b-16']")
    button_element_save.click()
