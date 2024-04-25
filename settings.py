from enum import Enum

from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.environ.get('BOT_TOKEN')
MAIN_LOGIN = os.environ.get('MAIN_LOGIN')
MAIN_PASSWORD = os.environ.get('MAIN_PASSWORD')
LOGIN_URL = os.environ.get('LOGIN_URL')
NA_YASNOY = os.environ.get('NA_YASNOY')


class MacroserverURLS(Enum):
    TEMP_RF = os.environ.get('TEMP_RF')
    K3_RF = os.environ.get('K3_RF')
    K3_SITISIT = os.environ.get('K3_SITISIT')
    H20_DOM_RU = os.environ.get('H20_DOM_RU')
    MILLENIUM_EKB_RU = os.environ.get('MILLENIUM_EKB_RU')
    M1_DOM_RU = os.environ.get('M1_DOM_RU')
    TEST_IDA_RU = os.environ.get('TEST_IDA_RU')
    ACTION_DN7_RU = os.environ.get('ACTION_DN7_RU')
    NASHEFSKOY_RU = os.environ.get('NASHEFSKOY_RU')
    GK_PRAKTIKA_RU = os.environ.get('GK_PRAKTIKA_RU')


USERS = ('albajes', 'r_dmitriev', 'goldfynjy')

MANAGERS_NA_YASNOY = {'78317': ['Татьяна Ларина', 'lanina.tl@gk-praktika.ru'],
                      '78315': ['Данил Нигматуллин', 'nigmatulin.dn@gk-praktika.ru'],
                      '78456': ['Наталия Епанчинцева', 'epanchinceva.nu@gk-praktika.ru']
                      }

MANAGERS_OTHER_OBJECTS = {'78576': ['Кагарманова Анна', 'kagarmanova.av@gk-praktika.ru'],
                          '78589': ['Ханова Лариса', 'khanova.lr@gk-praktika.ru'],
                          '77952': ['Ципан Елена', 'cipan.eg@gk-praktika.ru'],
                          '77860': ['Чернова Вера', 'chernova.vn@gk-praktika.ru'],
                          '77975': ['Страту Лариса', 'stratu.ln@gk-praktika.ru'],
                          '78653': ['Тарасов Никита', 'tarasov.nm@gk-praktika.ru'],
                          '79713': ['Соколкина Мария', 'sokolkina.mb@gk-praktika.ru']}


MEMBERS_NA_YASNOY = {'r_dmitriev': '78456', 'goldfynjy': '78315', 'albajes': '78317'}

MEMBERS = {'albajes': '78576', 'r_dmitriev': '78456', 'goldfynjy': '78315'}
