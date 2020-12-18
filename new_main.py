from PyQt5.QtWidgets import QAction, qApp, QMessageBox
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import pyqtSlot, pyqtSignal

from telethon.errors.rpcerrorlist import SessionPasswordNeededError
from telethon.sessions import StringSession
from telethon import TelegramClient

from functools import partial
import threading
import asyncio
import os.path
import shelve
import time
import sys
import os

from Form.main_form import Ui_TechTG
from Form.phone_form import Ui_TechTG2
from Form.chat_info_form import Chat_info_Form_Class
from Form.enter_date_form_all_chat import EnterDateForm
from Form.enter_date_form_one_chat import EnterDateForm_one_chat
from Form.export_leader_chat import Export_Leader_Form_Class
from Form.enter_number_leader_form import  Enter_Number_Leader_Form
from Form.export_chat_message_form import Export_Chat_Message_Form_Class
from Form.enter_number_export_chat_message_form import Enter_Number_Export_Message_Form
from Form.enter_user_id_export_chat_message_one_chat_form import Enter_User_ID_Export_Message_One_Chat_Form
from Form.enter_user_id_export_chat_message_all_chat_form import Enter_User_ID_Export_Message_All_Chat_Form
from Form.export_user_form import Export_User_Form_Class
from Form.enter_number_chat_export_user_form import Enter_Number_User_Form
from Form.enter_user_add_form import Add_User_Form_Class
from Form.enter_number_chat_user_add_form import Enter_Number_Chat_Add_User_Form
from Form.enter_number_chat_user_delete_form import Enter_Number_Delete_User_Form
from Form.delete_user_chat import Delete_User_Form_Class
from Form.add_number_to_contact_form import EnterNumberToContact


from operations.export_contact import get_address_book
from operations.info_chat import info_chat_result, info_chat_result_one_group
from operations.chat_name import chat_names_intro
from operations.export_leader_chat import leader_one_chat, leader_all_chat
from operations.export_chat import dump_one_chat_message, dump_all_chat_message, dump_one_chat_message_user_id, dump_all_chat_message_user_id
from operations.export_user import dump_users_one_chat, dump_users_all_chat
from operations.enter_user import enter_user_group
from operations.delete_user import delete_user_group
from operations.add_number_to_contact_list import add_number_to_contact



########################################################################################################################

# Начало функции потоков
def _run_aio_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()


aio_loop = asyncio.new_event_loop()
t = threading.Thread(target=partial(_run_aio_loop, aio_loop))
t.daemon = True
t.start()

# Конец функции потоков

########################################################################################################################

# Начала запуска функций окна аутентификации в потоке
def modal_window_session(auth_number_form, auth_2fa_code):  # Поток функции авторизации
    asyncio.run_coroutine_threadsafe(auth_telegram_session_function(auth_number_form, auth_2fa_code), aio_loop)

# #Конец запуска функций окна аутентификации в потоке

########################################################################################################################

# Начало функций для аутентификации
async def auth_telegram_session_function(auth_number_form, auth_2fa_code):
    client = TelegramClient(StringSession(), api_id, api_hash)
    await client.connect()
    if not await client.is_user_authorized():
        await client.send_code_request(auth_number_form)
        time.sleep(12)
        try:
            global auth_code_tg
            await client.sign_in(auth_number_form, auth_code_tg)
            me = await client.get_me()
            global auth_user_info
            auth_user_info = f'Выполнен вход от имени пользователя: \n{me.first_name} {me.last_name} {me.username} \n{me.id}  {me.phone}'
            pass
        except SessionPasswordNeededError:
            await client.sign_in(password=auth_2fa_code)
        finally:
            global auth_session_string
            auth_session_string = client.session.save()
            f = shelve.open("Session/auth")
            f["session"] = auth_session_string
            f.close()
            # Функция получения информации о чатах
            chat_name_request_thread()





# Конец функций  окна аутентификации

########################################################################################################################

# Старт объявление класса модального окна менюбара ввод пароля
class ModalWindowAuthCode(QtWidgets.QWidget):
    closeDialog_modal_code = pyqtSignal()
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.ui = Ui_TechTG2()
        self.ui.setupUi(self)
        self.ui.label_modal_windows_auth.setText("Введите код подтверждения")
        self.ui.label_modal_windows_auth_code.hide()
        self.ui.lineEdit_modal_windows_code.hide()
        self.ui.lineEdit_modal_windows_auth.clear()
        self.ui.lineEdit_modal_windows_auth.setPlaceholderText("12345")
        self.ui.lineEdit_modal_windows_auth.setCursorPosition(0)
        self.ui.lineEdit_modal_windows_auth.setFocus()
        self.ui.lineEdit_modal_windows_auth.setMaxLength(5)
        self.ui.lineEdit_modal_windows_auth.setInputMask("99999")
        self.ui.button_modal_window_auth.setText("Подтвердить")
        self.ui.button_modal_window_auth.clicked.connect(self.label_auth)
        self.ui.button_modal_window_auth.clicked.connect(self.on_click)

    def label_auth(self):
        self.ui.label_modal_windows_auth.setText("Авторизация...")

    # Функция ввода кода Телеграмм
    @pyqtSlot()
    def on_click(self):
        global auth_code_tg
        auth_code_tg = self.ui.lineEdit_modal_windows_auth.text()
        time.sleep(10)
        self.close()

    def closeEvent(self, event):
        self.closeDialog_modal_code.emit()

# Конец объявления класса модального окна менюбара ввод пароля

########################################################################################################################

# Объявление класса модального окна менюбара ввод номера и 2фа
class ModalWindowAuthPhone(QtWidgets.QWidget):
    closeDialog_modal_phone = pyqtSignal()

    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.ui = Ui_TechTG2()
        self.ui.setupUi(self)
        self._modal = ModalWindowAuthCode(self)
        self.ui.thread = None
        self.ui.button_modal_window_auth.clicked.connect(self.fun_button_start_thread_modal_auth_code)

    def fun_button_start_thread_modal_auth_code(self):
        self.hide()
        if self.ui.thread is None:
            self.ui.thread = WorkThread()
            self.ui.thread.threadSignal.connect(self.fun_signal_thread_button_start_modal_auth_code)
            self.ui.thread.start()
        else:
            self.ui.thread.terminate()
            self.ui.thread = None

    def fun_signal_thread_button_start_modal_auth_code(self):
        if not self._modal.isVisible():
            # Значения номера и 2фа из поля первого модального окна
            auth_number_form = self.ui.lineEdit_modal_windows_auth.text()
            auth_2fa_code = self.ui.lineEdit_modal_windows_code.text()
            modal_window_session(auth_number_form, auth_2fa_code)
            # Показ второго модального окна
            self._modal.show()
            self._modal.closeDialog_modal_code.connect(self.dialog_signal_slot_modal_code)

    def dialog_signal_slot_modal_code(self):
        self.close()

    def closeEvent(self, event):
        self.closeDialog_modal_phone.emit()


# Конец объявления класса модального окна менюбара для номера и 2фа

########################################################################################################################

# Функция обработки сигнала для окна пароля при аутентификации
class WorkThread(QtCore.QThread):
    threadSignal = QtCore.pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def run(self):
        te = ModalWindowAuthPhone(QtWidgets.QWidget)
        auth_number_form = te.ui.lineEdit_modal_windows_auth.text()
        self.threadSignal.emit(auth_number_form)
        return QtCore.QThread.run(self)


########################################################################################################################

#Начало обработки выгрузики информации из чатов

# Класс начала выгрузка информации по одному чату
class ModalWindowDateFormOneChat(QtWidgets.QWidget):
    closeDialog_modal_window_chat_one_info_date = pyqtSignal()

    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.ui = EnterDateForm_one_chat()
        self.ui.setupUi(self)
        self.ui.button_modal_window_auth.clicked.connect(self.get_date_function)

    # Функция получения даты и запуска функции получения информации по одному чату
    def get_date_function(self):
        modal_window_date_year = self.ui.lineEdit_modal_windows_year.text()
        modal_window_date_mouth = self.ui.lineEdit_modal_windows_mouth.text()
        modal_window_date_day = self.ui.lineEdit_modal_windows_day.text()
        modal_window_number_chat = self.ui.lineEdit_modal_windows_number_chat.text()
        res_date = str(modal_window_date_year) + '-' + str(modal_window_date_mouth) + '-' + str(modal_window_date_day)
        # запуск функции поулчения информации по всем чатам
        self.hide()
        cion = chat_info_thread_one_chat(res_date, modal_window_number_chat)
        msg_end = QMessageBox()
        msg_end.setText(
            f"Выгрузка информации по чатам завершена \nПолученный файл info_chat_one_№{modal_window_number_chat}.txt сохранён в каталоге result")
        msg_end.exec()
        self.ui.lineEdit_modal_windows_year.clear()
        self.ui.lineEdit_modal_windows_mouth.clear()
        self.ui.lineEdit_modal_windows_day.clear()
        self.ui.lineEdit_modal_windows_number_chat.clear()
        self.close()

    def closeEvent(self, event):
        self.closeDialog_modal_window_chat_one_info_date.emit()

# Класс начала выгрузка информации по всем чатам
class ModalWindowDateFormAllChat(QtWidgets.QWidget):
    closeDialog_modal_window_chat_info_all_date = pyqtSignal()

    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.ui = EnterDateForm()
        self.ui.setupUi(self)
        self.ui.button_modal_window_auth.clicked.connect(self.get_date_function)

    # Функция получения даты и запуска функции получения информации по всем чатам
    def get_date_function(self):
        modal_window_date_year = self.ui.lineEdit_modal_windows_year.text()
        modal_window_date_mouth = self.ui.lineEdit_modal_windows_mouth.text()
        modal_window_date_day = self.ui.lineEdit_modal_windows_day.text()
        res_date = str(modal_window_date_year) + '-' + str(modal_window_date_mouth) + '-' + str(modal_window_date_day)
        # запуск функции поулчения информации по всем чатам
        self.hide()
        ciac = chat_info_thread_all_chat(res_date)
        msg_end = QMessageBox()
        msg_end.setText(
            "Выгрузка информации по чатам завершена \nПолученный файл info_chat_all.txt сохранён в каталоге result")
        msg_end.exec()
        self.ui.lineEdit_modal_windows_year.clear()
        self.ui.lineEdit_modal_windows_mouth.clear()
        self.ui.lineEdit_modal_windows_day.clear()
        self.close()

    def closeEvent(self, event):
        self.closeDialog_modal_window_chat_info_all_date.emit()

class ModalWindowsChatInfo(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.ui = Chat_info_Form_Class()
        global chat_name
        self.ui.add_chat(chat_name)
        self.open_date_form_all_chat = ModalWindowDateFormAllChat(self)
        self.ui.button_export_all_chat.clicked.connect(self.open_date_window_all_chat)
        self.open_date_form_all_chat.closeDialog_modal_window_chat_info_all_date.connect(
            self.dialog_signal_slot_chat_info_all_function)

        self.open_date_form_one_chat = ModalWindowDateFormOneChat(self)
        self.ui.button_export_one_chat.clicked.connect(self.open_date_window_one_chat)
        self.open_date_form_one_chat.closeDialog_modal_window_chat_one_info_date.connect(
            self.dialog_signal_slot_chat_info_one_function)

    # Все чаты окна чат инфо
    # Функция открытия модального окна для всех чатов
    def open_date_window_all_chat(self):
        self.ui.button_export_all_chat.setEnabled(False)
        self.open_date_form_all_chat.show()

    # Сигнал модального окна для всех чатов
    def dialog_signal_slot_chat_info_all_function(self):
        self.ui.button_export_all_chat.setEnabled(True)

    # Один чат окна чат инфо
    # Функция открытия модального окна для всех чатов
    def open_date_window_one_chat(self):
        self.ui.button_export_one_chat.setEnabled(False)
        self.open_date_form_one_chat.show()

    # Сигнал модального окна для всех чатов
    def dialog_signal_slot_chat_info_one_function(self):
        self.ui.button_export_one_chat.setEnabled(True)

# Все чаты
def chat_info_thread_all_chat(res_date):  # Поток кнопки информации о всех чатах
    ciac = asyncio.run_coroutine_threadsafe(chat_info_all_chat_async_func(res_date), aio_loop)
    return ciac.result()

async def chat_info_all_chat_async_func(res_date):
    global auth_session_string
    client = TelegramClient(StringSession(auth_session_string), api_id, api_hash)
    await client.start()
    await info_chat_result(client, res_date)

# Один чат
def chat_info_thread_one_chat(res_date, modal_window_number_chat):  # Поток кнопки информации о всех чатах
    cion = asyncio.run_coroutine_threadsafe(chat_info_one_chat_async_func(res_date, modal_window_number_chat), aio_loop)
    return cion.result()

async def chat_info_one_chat_async_func(res_date, modal_window_number_chat):
    global auth_session_string
    client = TelegramClient(StringSession(auth_session_string), api_id, api_hash)
    await client.start()
    await info_chat_result_one_group(client, res_date, modal_window_number_chat)

#Конец обработки выгрузики информации из чатов

########################################################################################################################

#Начало обработки выгрузики сообщений из чата

# Класс начала выгрузка сообщений по одному чату и ID
class ModalWindowNumberFormExportMessageChatOneUserID(QtWidgets.QWidget):
    closeDialog_modal_window_export_message_chat_one_user_id = pyqtSignal()

    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.ui = Enter_User_ID_Export_Message_One_Chat_Form()
        self.ui.setupUi(self)
        self.ui.button_modal_window_auth.clicked.connect(self.get_date_function)

    # Функция получения даты и запуска функции получения информации по одному чату
    def get_date_function(self):
        modal_window_number_chat = self.ui.lineEdit_modal_windows_number_chat.text()
        modal_window_user_id_one = self.ui.lineEdit_modal_windows_user_id.text()
        # запуск функции поулчения информации по всем чатам
        self.hide()
        cemoci = chat_export_message_thread_one_chat_id(modal_window_number_chat, modal_window_user_id_one)
        msg_end = QMessageBox()
        msg_end.setText(
            f"Выгрузка информации по чатам завершена \nПолученный файл сохранён в каталоге result")
        msg_end.exec()
        self.ui.lineEdit_modal_windows_number_chat.clear()
        self.ui.lineEdit_modal_windows_user_id.clear()
        self.close()

    def closeEvent(self, event):
        self.closeDialog_modal_window_export_message_chat_one_user_id.emit()

# Класс начала выгрузка сообщений по всем чатам ID
class ModalWindowNumberFormExportMessageChatAllUserID(QtWidgets.QWidget):
    closeDialog_modal_window_export_message_chat_all_user_id = pyqtSignal()

    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.ui = Enter_User_ID_Export_Message_All_Chat_Form()
        self.ui.setupUi(self)
        self.ui.button_modal_window_auth.clicked.connect(self.get_date_function)

    # Функция получения даты и запуска функции получения информации по одному чату
    def get_date_function(self):
        modal_window_user_id = self.ui.lineEdit_modal_windows_number_chat.text()
        # запуск функции поулчения информации по всем чатам
        self.hide()
        ceaci = chat_export_message_thread_all_chat_id(modal_window_user_id)
        msg_end = QMessageBox()
        msg_end.setText(
            f"Выгрузка информации по чатам завершена \nПолученный файл {modal_window_user_id}_export_message_all_chat.txt сохранён в каталоге result")
        msg_end.exec()
        self.ui.lineEdit_modal_windows_number_chat.clear()
        self.close()

    def closeEvent(self, event):
        self.closeDialog_modal_window_export_message_chat_all_user_id.emit()


# Класс начала выгрузка сообщений по одному чату
class ModalWindowNumberFormExportMessageChat(QtWidgets.QWidget):
    closeDialog_modal_window_export_message_chat = pyqtSignal()

    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.ui = Enter_Number_Export_Message_Form()
        self.ui.setupUi(self)
        self.ui.button_modal_window_auth.clicked.connect(self.get_date_function)

    # Функция получения даты и запуска функции получения информации по одному чату
    def get_date_function(self):
        modal_window_number_chat = self.ui.lineEdit_modal_windows_number_chat.text()
        # запуск функции поулчения информации по всем чатам
        self.hide()
        ceoc = chat_export_message_thread_one_chat(modal_window_number_chat)
        msg_end = QMessageBox()
        msg_end.setText(
            f"Выгрузка информации по чатам завершена \nПолученный файл сохранён в каталоге result")
        msg_end.exec()
        self.ui.lineEdit_modal_windows_number_chat.clear()
        self.close()

    def closeEvent(self, event):
        self.closeDialog_modal_window_export_message_chat.emit()

class ModalWindowsExportMessageChat(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.ui = Export_Chat_Message_Form_Class()
        global chat_name
        self.ui.add_chat(chat_name)
        #Выгрузка из одного чата
        self.open_date_form_one_chat = ModalWindowNumberFormExportMessageChat(self)
        self.ui.button_export_one_chat.clicked.connect(self.open_number_window_one_chat_message_export)
        self.open_date_form_one_chat.closeDialog_modal_window_export_message_chat.connect(
            self.dialog_signal_slot_chat_message_export)
        #Выгрузка из всех чатов
        self.ui.button_export_all_chat.clicked.connect(self.all_chat_message_export)
        #Выгрузка из одного чата по ID
        self.open_date_form_one_chat_id = ModalWindowNumberFormExportMessageChatOneUserID(self)
        self.ui.button_export_one_chat_user_id.clicked.connect(self.open_number_window_one_chat_message_export_user_id)
        self.open_date_form_one_chat_id.closeDialog_modal_window_export_message_chat_one_user_id.connect(
            self.closeDialog_modal_window_export_message_chat_one_user_id)
        #Выгрузка из всех чатов по ID
        self.open_date_form_all_chat_id = ModalWindowNumberFormExportMessageChatAllUserID(self)
        self.ui.button_export_all_chat_user_id.clicked.connect(self.open_number_window_all_chat_message_export_user_id)
        self.open_date_form_all_chat_id.closeDialog_modal_window_export_message_chat_all_user_id.connect(
            self.closeDialog_modal_window_export_message_chat_all_user_id)

    # Один чат окна чат инфо
    # Функция открытия модального окна для всех чатов
    def open_number_window_one_chat_message_export(self):
        self.ui.button_export_one_chat.setEnabled(False)
        self.open_date_form_one_chat.show()

    # Сигнал модального окна для всех чатов
    def dialog_signal_slot_chat_message_export(self):
        self.ui.button_export_one_chat.setEnabled(True)

    #Все чаты функция
    def all_chat_message_export(self):
        self.ui.button_export_all_chat.setEnabled(False)
        ceac = chat_export_message_thread_all_chat()
        msg_end = QMessageBox()
        msg_end.setText(
            f"Выгрузка информации по чатам завершена \nПолученные файлы сохранены в каталоге result")
        msg_end.exec()
        self.ui.button_export_all_chat.setEnabled(True)

    # Один чат окна сообщения по ИД
    # Функция открытия модального окна для одного чата по ИД
    def open_number_window_one_chat_message_export_user_id(self):
        self.ui.button_export_one_chat_user_id.setEnabled(False)
        self.open_date_form_one_chat_id.show()

    # Сигнал модального окна для одного чата по ИД
    def closeDialog_modal_window_export_message_chat_one_user_id(self):
        self.ui.button_export_one_chat_user_id.setEnabled(True)


    # Все чаты окна сообщения по ИД
    # Функция открытия модального окна для всех чатов по ИД
    def open_number_window_all_chat_message_export_user_id(self):
        self.ui.button_export_all_chat_user_id.setEnabled(False)
        self.open_date_form_all_chat_id.show()

    # Сигнал модального окна для всех чата по ИД
    def closeDialog_modal_window_export_message_chat_all_user_id(self):
        self.ui.button_export_all_chat_user_id.setEnabled(True)

# Все чаты
def chat_export_message_thread_all_chat():  # Поток кнопки информации о всех чатах
    cemac = asyncio.run_coroutine_threadsafe(chat_export_message_all_chat_async_func(), aio_loop)
    return cemac.result()

async def chat_export_message_all_chat_async_func():  # Функция кнопки информации о всех чатах
    global auth_session_string
    client = TelegramClient(StringSession(auth_session_string), api_id, api_hash)
    await client.start()
    await dump_all_chat_message(client)


# Один чат
def chat_export_message_thread_one_chat(modal_window_number_chat):  # Поток кнопки информации о всех чатах
    cemoc = asyncio.run_coroutine_threadsafe(chat_export_message_one_chat_async_func(modal_window_number_chat), aio_loop)
    return cemoc.result()


async def chat_export_message_one_chat_async_func(modal_window_number_chat):  # Функция кнопки информации о всех чатах
    global auth_session_string
    client = TelegramClient(StringSession(auth_session_string), api_id, api_hash)
    await client.start()
    await dump_one_chat_message(client, modal_window_number_chat)

# Все чаты ID
def chat_export_message_thread_all_chat_id(modal_window_user_id):  # Поток кнопки информации о всех чатах
    cemaci = asyncio.run_coroutine_threadsafe(chat_export_message_all_chat_id_async_func(modal_window_user_id), aio_loop)
    return cemaci.result()


async def chat_export_message_all_chat_id_async_func(modal_window_user_id):  # Функция кнопки информации о всех чатах
    global auth_session_string
    client = TelegramClient(StringSession(auth_session_string), api_id, api_hash)
    await client.start()
    await dump_all_chat_message_user_id(client, modal_window_user_id)


# Один чат ID
def chat_export_message_thread_one_chat_id(modal_window_number_chat, modal_window_user_id_one):  # Поток кнопки информации о всех чатах
    cemoci = asyncio.run_coroutine_threadsafe(chat_export_message_one_chat_id_async_func(modal_window_number_chat, modal_window_user_id_one), aio_loop)
    return cemoci.result()

async def chat_export_message_one_chat_id_async_func(modal_window_number_chat, modal_window_user_id_one):  # Функция кнопки информации о всех чатах
    global auth_session_string
    client = TelegramClient(StringSession(auth_session_string), api_id, api_hash)
    await client.start()
    await dump_one_chat_message_user_id(client, modal_window_number_chat, modal_window_user_id_one)

# #Конец обработки выгрузики сообщений чатов

########################################################################################################################

#Начало обработки выгрузики лидеров чатов

# Класс начала выгрузка лидеров по одному чату
class ModalWindowNumberFormLeaderChat(QtWidgets.QWidget):
    closeDialog_modal_window_chat_one_leader = pyqtSignal()

    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.ui = Enter_Number_Leader_Form()
        self.ui.setupUi(self)
        self.ui.button_modal_window_auth.clicked.connect(self.get_date_function)

    # Функция получения даты и запуска функции получения информации по одному чату
    def get_date_function(self):
        modal_window_number_chat = self.ui.lineEdit_modal_windows_number_chat.text()
        # запуск функции поулчения информации по всем чатам
        self.hide()
        cloc = chat_leader_thread_one_chat(modal_window_number_chat)
        msg_end = QMessageBox()
        msg_end.setText(
            f"Выгрузка информации по чатам завершена \nПолученный файл сохранён в каталоге result")
        msg_end.exec()
        self.ui.lineEdit_modal_windows_number_chat.clear()
        self.close()

    def closeEvent(self, event):
        self.closeDialog_modal_window_chat_one_leader.emit()


class ModalWindowsLeaderChat(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.ui = Export_Leader_Form_Class()
        global chat_name
        self.ui.add_chat(chat_name)

        self.open_date_form_one_chat = ModalWindowNumberFormLeaderChat(self)
        self.ui.button_export_one_chat.clicked.connect(self.open_number_window_one_chat_leader)
        self.open_date_form_one_chat.closeDialog_modal_window_chat_one_leader.connect(
            self.dialog_signal_slot_chat_leader_function)
        self.ui.button_export_all_chat.clicked.connect(self.all_chat_leader)


    # Один чат окна чат инфо
    # Функция открытия модального окна для всех чатов
    def open_number_window_one_chat_leader(self):
        self.ui.button_export_one_chat.setEnabled(False)
        self.open_date_form_one_chat.show()

    # Сигнал модального окна для всех чатов
    def dialog_signal_slot_chat_leader_function(self):
        self.ui.button_export_one_chat.setEnabled(True)

    #Все чаты функция
    def all_chat_leader(self):
        self.ui.button_export_all_chat.setEnabled(False)
        clac = chat_leader_thread_all_chat()
        msg_end = QMessageBox()
        msg_end.setText(
            f"Выгрузка информации по чатам завершена \nПолученные файлы сохранены в каталоге result")
        msg_end.exec()
        self.ui.button_export_all_chat.setEnabled(True)


# Все чаты
def chat_leader_thread_all_chat():  # Поток кнопки информации о всех чатах
    clac = asyncio.run_coroutine_threadsafe(chat_leader_all_chat_async_func(), aio_loop)
    return clac.result()

async def chat_leader_all_chat_async_func():  # Функция кнопки информации о всех чатах
    global auth_session_string
    client = TelegramClient(StringSession(auth_session_string), api_id, api_hash)
    await client.start()
    await leader_all_chat(client)

# Один чат
def chat_leader_thread_one_chat(modal_window_number_chat):  # Поток кнопки информации о всех чатах
    cloc = asyncio.run_coroutine_threadsafe(chat_leader_one_chat_async_func(modal_window_number_chat), aio_loop)
    return cloc.result()

async def chat_leader_one_chat_async_func(modal_window_number_chat):  # Функция кнопки информации о всех чатах
    global auth_session_string
    client = TelegramClient(StringSession(auth_session_string), api_id, api_hash)
    await client.start()
    await leader_one_chat(client, modal_window_number_chat)

#Конец обработки выгрузики лидеров чатов

########################################################################################################################

#Начало обработки выгрузики участников чатов

# Класс начала выгрузка учаcтников из одного чата
class ModalWindowNumberFormUserExportChat(QtWidgets.QWidget):
    closeDialog_modal_window_chat_one_user_export = pyqtSignal()

    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.ui = Enter_Number_User_Form()
        self.ui.setupUi(self)
        self.ui.button_modal_window_auth.clicked.connect(self.get_date_function)

    # Функция выгрузки участников из одного чата
    def get_date_function(self):
        modal_window_number_chat = self.ui.lineEdit_modal_windows_number_chat.text()
        # запуск функции поулчения информации по всем чатам
        self.hide()
        ceuoc = chat_export_user_thread_one_chat(modal_window_number_chat)
        msg_end = QMessageBox()
        msg_end.setText(
            f"Выгрузка информации по чатам завершена \nПолученный файл сохранён в каталоге result")
        msg_end.exec()
        self.ui.lineEdit_modal_windows_number_chat.clear()
        self.close()

    def closeEvent(self, event):
        self.closeDialog_modal_window_chat_one_user_export.emit()



class ModalWindowsUserExportChat(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.ui = Export_User_Form_Class()
        global chat_name
        self.ui.add_chat(chat_name)

        self.open_date_form_one_chat = ModalWindowNumberFormUserExportChat(self)
        self.ui.button_export_one_chat.clicked.connect(self.open_number_window_one_chat_export_user)
        self.open_date_form_one_chat.closeDialog_modal_window_chat_one_user_export.connect(
            self.dialog_signal_slot_chat_export_user_function)
        self.ui.button_export_all_chat.clicked.connect(self.all_chat_leader)


    # Один чат окна чат инфо
    # Функция открытия модального окна для всех чатов
    def open_number_window_one_chat_export_user(self):
        self.ui.button_export_one_chat.setEnabled(False)
        self.open_date_form_one_chat.show()

    # Сигнал модального окна для всех чатов
    def dialog_signal_slot_chat_export_user_function(self):
        self.ui.button_export_one_chat.setEnabled(True)

    #Все чаты функция
    def all_chat_leader(self):
        self.ui.button_export_all_chat.setEnabled(False)
        ceuac = chat_export_user_thread_all_chat()
        msg_end = QMessageBox()
        msg_end.setText(
            f"Выгрузка информации по чатам завершена \nПолученные файлы сохранены в каталоге result")
        msg_end.exec()
        self.ui.button_export_all_chat.setEnabled(True)


# Все чаты
def chat_export_user_thread_all_chat():
    ceuac = asyncio.run_coroutine_threadsafe(chat_export_user_all_chat_async_func(), aio_loop)
    return ceuac.result()


async def chat_export_user_all_chat_async_func():
    global auth_session_string
    client = TelegramClient(StringSession(auth_session_string), api_id, api_hash)
    await client.start()
    await dump_users_all_chat(client)

# Один чат
def chat_export_user_thread_one_chat(modal_window_number_chat):
    ceuoc = asyncio.run_coroutine_threadsafe(chat_export_user_one_chat_async_func(modal_window_number_chat), aio_loop)
    return ceuoc.result()

async def chat_export_user_one_chat_async_func(modal_window_number_chat):  # Функция кнопки информации о всех чатах
    global auth_session_string
    client = TelegramClient(StringSession(auth_session_string), api_id, api_hash)
    await client.start()
    await dump_users_one_chat(client, modal_window_number_chat)

#Конец обработки выгрузики участников чатов

########################################################################################################################

#Начало обработки добавления пользователей в чат

# Класс начала добавления пользователй в чат
class ModalWindowNumberFormAddUserChat(QtWidgets.QWidget):
    closeDialog_modal_window_chat_add_user = pyqtSignal()

    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.ui = Enter_Number_Chat_Add_User_Form()
        self.ui.setupUi(self)
        self.ui.button_modal_window_auth.clicked.connect(self.get_date_function)

    # Функция получения даты и запуска функции получения информации по одному чату
    def get_date_function(self):
        modal_window_number_chat = self.ui.lineEdit_modal_windows_number_chat.text()
        user_name_add = self.ui.qText_modal_windows_user_name_add.toPlainText().split('\n')
        self.hide()
        cauoc = chat_add_user_thread_one_chat(modal_window_number_chat, user_name_add)
        msg_end = QMessageBox()
        msg_end.setText(
            f"Пользователи добавленны в чат")
        msg_end.exec()
        self.ui.lineEdit_modal_windows_number_chat.clear()
        self.ui.qText_modal_windows_user_name_add.clear()

    def closeEvent(self, event):
        self.closeDialog_modal_window_chat_add_user.emit()

class ModalWindowsAddUserChat(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.ui = Add_User_Form_Class()
        global chat_name
        self.ui.add_chat(chat_name)

        self.open_date_form_add_user_chat = ModalWindowNumberFormAddUserChat(self)
        self.ui.button_export_one_chat.clicked.connect(self.open_number_window_one_chat_leader)
        self.open_date_form_add_user_chat.closeDialog_modal_window_chat_add_user.connect(
            self.dialog_signal_slot_chat_leader_function)



    def open_number_window_one_chat_leader(self):
        self.ui.button_export_one_chat.setEnabled(False)
        self.open_date_form_add_user_chat.show()


    def dialog_signal_slot_chat_leader_function(self):
        self.ui.button_export_one_chat.setEnabled(True)


# Один чат
def chat_add_user_thread_one_chat(modal_window_number_chat, user_name_add):  # Поток кнопки информации о всех чатах
    cauoc = asyncio.run_coroutine_threadsafe(chat_add_user_one_chat_async_func(modal_window_number_chat, user_name_add), aio_loop)
    return cauoc.result()


async def chat_add_user_one_chat_async_func(modal_window_number_chat, user_name_add):
    global auth_session_string
    client = TelegramClient(StringSession(auth_session_string), api_id, api_hash)
    await client.start()
    await enter_user_group(client, modal_window_number_chat, user_name_add)

#Конец обработки добавления пользователей

########################################################################################################################

#Начало обработки удаления пользователей

# Класс начала удаления пользователей из чата
class ModalWindowNumberFormDeleteUserChat(QtWidgets.QWidget):
    closeDialog_modal_window_chat_delete_user = pyqtSignal()

    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.ui = Enter_Number_Delete_User_Form()
        self.ui.setupUi(self)
        self.ui.button_modal_window_auth.clicked.connect(self.get_date_function)

    def get_date_function(self):
        modal_window_number_chat = self.ui.lineEdit_modal_windows_number_chat.text()
        self.hide()
        cduoc = chat_delete_user_thread_one_chat(modal_window_number_chat)
        msg_end = QMessageBox()
        msg_end.setText(
            f"Пользователи удалены из чата")
        msg_end.exec()
        self.ui.lineEdit_modal_windows_number_chat.clear()


    def closeEvent(self, event):
        self.closeDialog_modal_window_chat_delete_user.emit()


class ModalWindowsDeleteUserChat(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.ui = Delete_User_Form_Class()
        global chat_name
        self.ui.add_chat(chat_name)
        msg_info = QMessageBox()
        msg_info.setText(
            f"Удаление из чата осуществляется по 200 \nпользователей с перерывом 15 минут. \nПовторный запуск программы не требуется")
        msg_info.exec()
        self.open_date_form_delete_user_chat = ModalWindowNumberFormDeleteUserChat(self)
        self.ui.button_export_one_chat.clicked.connect(self.open_number_window_one_chat_leader)
        self.open_date_form_delete_user_chat.closeDialog_modal_window_chat_delete_user.connect(
            self.dialog_signal_slot_chat_delete_user_function)


    def open_number_window_one_chat_leader(self):
        self.ui.button_export_one_chat.setEnabled(False)
        self.open_date_form_delete_user_chat.show()

    def dialog_signal_slot_chat_delete_user_function(self):
        self.ui.button_export_one_chat.setEnabled(True)


def chat_delete_user_thread_one_chat(modal_window_number_chat):  # Поток кнопки информации о всех чатах
    cduoc = asyncio.run_coroutine_threadsafe(chat_delete_user_one_chat_async_func(modal_window_number_chat), aio_loop)
    return cduoc.result()


async def chat_delete_user_one_chat_async_func(modal_window_number_chat):
    global auth_session_string
    client = TelegramClient(StringSession(auth_session_string), api_id, api_hash)
    await client.start()
    await delete_user_group(client, modal_window_number_chat)

#Конец обработки удаления пользователей

########################################################################################################################

#Начало обработки добавления номера

# Класс начала добавления пользователей в чата
class ModalWindowAddNumberToContactChat(QtWidgets.QWidget):
    closeDialog_modal_window_add_number_to_contact = pyqtSignal()
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.ui = EnterNumberToContact()
        self.ui.setupUi(self)
        self.ui.button_modal_window_auth.clicked.connect(self.get_date_function)
        msg_info = QMessageBox()
        msg_info.setText(
            f"Данная функция осуществляет попытку\nдобавления номера в список контактов.\nНе используйте её чаще чем раз в 12 часов")
        msg_info.exec()

    def get_date_function(self):
        modal_window_number_phone = self.ui.lineEdit_modal_windows_auth.text()
        self.hide()
        amoc = add_number_thread_one_chat(modal_window_number_phone)
        msg_end = QMessageBox()
        msg_end.setText(
            f"Попытка добавления номера проведена\nпроверьте номер в контактах")
        msg_end.exec()
        self.ui.lineEdit_modal_windows_auth.clear()
        self.close()

    def closeEvent(self, event):
        self.closeDialog_modal_window_add_number_to_contact.emit()


def add_number_thread_one_chat(modal_window_number_phone):
    anoc = asyncio.run_coroutine_threadsafe(add_phone_number_to_contact_async_func(modal_window_number_phone), aio_loop)
    return anoc.result()

async def add_phone_number_to_contact_async_func(modal_window_number_phone):
    global auth_session_string
    client = TelegramClient(StringSession(auth_session_string), api_id, api_hash)
    await client.start()
    await add_number_to_contact(client, modal_window_number_phone)


#Конец обработки добавления номера

########################################################################################################################

# Начала запуска функций кнопок основного окна в потоке

def main_window_export_contact_thread():  # Поток кнопки экспорта контактов
    mwec = asyncio.run_coroutine_threadsafe(export_contact_function(), aio_loop)
    return mwec.result()



def chat_name_request_thread():  # Поток кнопки экспорта всех чатов
    asyncio.run_coroutine_threadsafe(chat_name_request_async_func(), aio_loop)



def check_auth_start_program_thread():  # Поток проверки авторизации при старте
    global auth_session_string
    if auth_session_string != '':
        asyncio.run_coroutine_threadsafe(check_auth_start(), aio_loop)
        time.sleep(3)
        chat_name_request_thread()
        global auth_user_info
        return auth_user_info
    else:
        pass


# Конец запуска функций основного окна в потоке

########################################################################################################################

# Начало функций для основного окна


# Начало экспорт контактов
async def export_contact_function():
    global auth_session_string
    client = TelegramClient(StringSession(auth_session_string), api_id, api_hash)
    await client.start()
    await get_address_book(client, auth_session_string)


# Начало функции о найденных чатах
async def chat_name_request_async_func():
    global auth_session_string
    client = TelegramClient(StringSession(auth_session_string), api_id, api_hash)
    await client.start()
    global chat_name
    chat_name = await chat_names_intro(client)



# Конец функции о найденных чатах


# Функция проверки авторизации при старте
async def check_auth_start():
    global auth_session_string
    client = TelegramClient(StringSession(auth_session_string), api_id, api_hash)
    await client.start()
    me = await client.get_me()
    global auth_user_info
    auth_user_info = f'Выполнен вход от имени пользователя: \n{me.first_name} {me.last_name} {me.username} \n{me.id}  {me.phone}'




# Конец функций для основного окна

########################################################################################################################

# Инициализация окна
class MainWindow(QtWidgets.QMainWindow):
    # Конструктор
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_TechTG()
        self.ui.setupUi(self)
        # Начало менюбар!!!
        # Инициализация кнопки авторизация
        self._modal = ModalWindowAuthPhone(self)
        auth_action = QAction('&Авторизация', self)
        auth_action.setShortcut('Ctrl+N')
        auth_action.setStatusTip('Авторизоваться под новым пользователем')
        auth_action.triggered.connect(self._modal.show)
        self._modal.closeDialog_modal_phone.connect(self.modal_window_signal_slot_auth)

        auth_session = QAction('&Выйти и удалить текущую сессию', self)
        auth_session.setShortcut('Ctrl+L')
        auth_session.setStatusTip('Выйти и удалить текущую сессию')
        auth_session.triggered.connect(self.auth_delete_session)
        auth_session.triggered.connect(qApp.quit)

        # Инициализация кнопки выход
        exit_action = QAction('&Выход', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Выйти из приложения')
        exit_action.triggered.connect(qApp.quit)

        help_action = QAction('&Справка', self)
        help_action.setShortcut('Ctrl+H')
        help_action.setStatusTip('Справка')
        help_action.triggered.connect(self.help_information)

        dev_action = QAction('&Разработка', self)
        dev_action.setShortcut('Ctrl+D')
        dev_action.setStatusTip('Разработка')
        dev_action.triggered.connect(self.dev_information)
        self.information()


        # Инициализация меню
        self.statusBar()
        menubar = self.menuBar()
        file_menu = menubar.addMenu('&Файл')
        file_menu.addAction(auth_action)
        file_menu.addAction(auth_session)
        file_menu.addAction(exit_action)
        self.setGeometry(300, 300, 300, 200)
        help_menu = menubar.addMenu('&Справка')
        help_menu.addAction(help_action)
        help_menu.addAction(dev_action)
        self.setGeometry(300, 300, 300, 200)
        # Имя главного окна
        self.setWindowTitle('TechTG')
        # Конец менюбар!!!
        auth_check_test = check_auth_start_program_thread()
        if auth_check_test != None:
            self.ui.label_main_window.setText(auth_check_test)
        else:
            pass

        # Начала обработчика нажатия кнопок основного окна

        # Кнопка 1 Информация о чатах
        self.ui.button_main_win_info_chat.clicked.connect(self.call_main_win_info_chat)

        # Кнопка 2 Информация о лидерах чата
        self.ui.button_main_win_info_leader.clicked.connect(self.call_main_win_leader_chat)

        # Кнопка 3 Выгрузка сообщений из чата
        self.ui.button_main_win_export_message.clicked.connect(self.call_main_win_export_message_chat)

        # Кнопка 4 Выгрузка пользователей из чата
        self.ui.button_main_win_export_user.clicked.connect(self.call_main_win_export_user)

        # Кнопка 5 Выгрузка контактов
        self.ui.button_main_win_export_contact.clicked.connect(self.call_main_win_export_contact)

        # Кнопка 6 Добавление пользователей
        self.ui.button_main_win_add_user.clicked.connect(self.call_main_win_add_user)

        # Кнопка 7 Удаление пользователей
        self.ui.button_main_win_delete_user.clicked.connect(self.call_main_win_delete_user)

        # Кнопка 8 Проверка номера
        self.ui.button_main_win_check_number.clicked.connect(self.call_main_win_add_to_contact_number)


    def information(self):
        msg_help = QMessageBox()
        msg_help.setText("При первом запуске программы изучите меню 'Справка'")
        msg_help.exec()


    #Меню бар
    def auth_delete_session(self):
        folder_path = './Session'
        for file_object in os.listdir(folder_path):
            file_object_path = os.path.join(folder_path, file_object)
            if os.path.isfile(file_object_path):
                os.unlink(file_object_path)

    def help_information(self):
        msg_help = QMessageBox()
        msg_help.setText(
            f"Справка:\n"
            f"1.Данное программное обеспечение разработано с целью осуществления анализа сведений мессенджера 'Telegram'\n"
            f"2.Перед началом работы, по средствам меню 'Файл' необходио осуществить авторизацию в учётной записи\n"
            f"3.При дальнейшей работе и использовании функций ПО, необходимо дожидаться окончания их работы\n"
            f"4.При сбоях в работе программы (отсутствия информации в открывашемся окне функции), закрыть программу через пункт меню 'Выйти и удалить текущую сессию', после чего авторизоваться заново \n"
            f"5.В виду значительных объёмов обрабатываемых данных, ОС, может сообщать о зависании программы, не рекомендуется выключать её до завершения работы выбранной функции и получения уведомления об окончании работы\n"
            f"6.При каждом запуске программы каталог 'result' будет автоматически очищен")
        msg_help.exec()

    def dev_information(self):
        msg_dev = QMessageBox()
        msg_dev.setText(
            f"Все предложения об улучшении данного ПО\nнаправлять на 'vlad_kugan@hotmail.com")
        msg_dev.exec()

    # Функция обработки сигналов
    def modal_window_signal_slot_auth(self):
        global auth_user_info
        self.ui.label_main_window.setText(auth_user_info)

    def modal_window_signal_slot_add_number_to_contact(self):
        self.ui.button_main_win_check_number.setEnabled(True)

    def modal_window_signal_slot_send_id(self):
        self.ui.button_main_win_request_number.setEnabled(True)


    # Функция кнопки 1
    def call_main_win_info_chat(self):
        self._modal = ModalWindowsChatInfo(self)


    # Функция кнопки 2
    def call_main_win_leader_chat(self):
        self._modal = ModalWindowsLeaderChat(self)

    #Функция кнопки 3
    def call_main_win_export_message_chat(self):
        self._modal = ModalWindowsExportMessageChat(self)

    #Функция кнопки 4
    def call_main_win_export_user(self):
        self._modal = ModalWindowsUserExportChat(self)

    #Функция кнопки 5
    def call_main_win_export_contact(self):
        self.ui.button_main_win_export_contact.setEnabled(False)
        mwect = main_window_export_contact_thread()
        msg_end = QMessageBox()
        msg_end.setText(
            f"Выгрузка контактов завершена \nПолученные файлы сохранены в каталоге result")
        msg_end.exec()
        self.ui.button_main_win_export_contact.setEnabled(True)


    #Функция кнопки 6
    def call_main_win_add_user(self):
        self._modal = ModalWindowsAddUserChat(self)

    #Функция кнопки 7
    def call_main_win_delete_user(self):
        self._modal = ModalWindowsDeleteUserChat(self)
    #Функция кнопки 8
    def call_main_win_add_to_contact_number(self):
        self._modal = ModalWindowAddNumberToContactChat(self)
        self._modal.closeDialog_modal_window_add_number_to_contact.connect(self.modal_window_signal_slot_add_number_to_contact)
        self._modal.show()
        self.ui.button_main_win_check_number.setEnabled(False)
    #Функция кнопки 9
    # Конец обработчика нажатия кнопок основного окна

    ########################################################################################################################

    # Начала обработчика заставки

    def load_data(self, sp):
        for i in range(4, 11):  # Имитируем процесс
            time.sleep(0.3)  # Что-то загружаем
            sp.showMessage("Загрузка данных... {0}%".format(i * 10),
                           QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom, QtCore.Qt.white)
            QtWidgets.qApp.processEvents()  # Запускаем оборот цикла

    # Конец обработчика заставки

    ########################################################################################################################

    # Начала обработчика выхода из приложения

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Уведомление',
                                     "Вы действительно хотите выйти?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


# Конец обработчика выхода из приложения

########################################################################################################################

# Запуск программы
if __name__ == '__main__':
    # глобальые переменные
    api_id = ''
    api_hash = ''
    op_string = ''
    chat_name = {}
    if os.path.exists("Session/auth.dat"):
        f = shelve.open("Session/auth")
        op_string = f.get('session', '')
        f.close()
    time.sleep(3)
    auth_session_string = op_string
    auth_number_tg = ''
    auth_code_tg = ''
    auth_user_info = ''
    test = None
    folder_path = './result'
    for file_object in os.listdir(folder_path):
        file_object_path = os.path.join(folder_path, file_object)
        if os.path.isfile(file_object_path):
            os.unlink(file_object_path)
    app = QtWidgets.QApplication([])
    splash = QtWidgets.QSplashScreen(QtGui.QPixmap("Image/fon.png"))
    splash.showMessage("Загрузка данных... 30%",
                       QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom, QtCore.Qt.white)
    splash.show()
    QtWidgets.qApp.processEvents()  # Запускаем оборот цикла
    application = MainWindow()
    application.load_data(splash)
    application.show()
    splash.finish(application)
    sys.exit(app.exec())

