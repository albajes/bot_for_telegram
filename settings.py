from enum import Enum

from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.environ.get('BOT_TOKEN')
MAIN_LOGIN = os.environ.get('MAIN_LOGIN')
MAIN_PASSWORD = os.environ.get('MAIN_PASSWORD')
LOGIN_URL = os.environ.get('LOGIN_URL')
NA_YASNOY = os.environ.get('NA_YASNOY')

MEMBERS = {'albajes': '78456', 'r_dmitriev': '77975', 'epanchintsevan': '78456',
           'danil_praktika': '78315', 'Praktika_development': '78589', 'PraktikaAnna': '78576',
           'PraktikaPRODAGI': '77860', 'gk_temp': '77952', 'Mariapraktika': '79713',
           'Nikita_praktika': '78653', 'LaninaTL': '78317', 'Pratika_Larisa': '77975'}

MANAGERS = {'78576': ['Кагарманова Анна', 'kagarmanova.av@gk-praktika.ru'],
            '78589': ['Ханова Лариса', 'khanova.lr@gk-praktika.ru'],
            '77952': ['Ципан Елена', 'cipan.eg@gk-praktika.ru'],
            '77860': ['Чернова Вера', 'chernova.vn@gk-praktika.ru'],
            '77975': ['Страту Лариса', 'stratu.ln@gk-praktika.ru'],
            '78653': ['Тарасов Никита', 'tarasov.nm@gk-praktika.ru'],
            '79713': ['Соколкина Мария', 'sokolkina.mb@gk-praktika.ru'],
            '78317': ['Татьяна Ларина', 'lanina.tl@gk-praktika.ru'],
            '78315': ['Данил Нигматуллин', 'nigmatulin.dn@gk-praktika.ru'],
            '78456': ['Наталия Епанчинцева', 'epanchinceva.nu@gk-praktika.ru']}


class MacroserverURLS(Enum):
    TEMP_RF = os.environ.get('TEMP_RF')
    K3_RF = os.environ.get('K3_RF')
    K3_SITISIT = os.environ.get('K3_SITISIT')
    H20_DOM_RU = os.environ.get('H20_DOM_RU')
    MILLENIUM_EKB_RU = os.environ.get('MILLENIUM_EKB_RU')
    M1_DOM_RU = os.environ.get('M1_DOM_RU')
    NASHEFSKOY_RU = os.environ.get('NASHEFSKOY_RU')
    GK_PRAKTIKA_RU = os.environ.get('GK_PRAKTIKA_RU')
    TEST_IDA_RU = os.environ.get('TEST_IDA_RU')
    ACTION_DN7_RU = os.environ.get('ACTION_DN7_RU')
