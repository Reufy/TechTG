from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TechTG(object):

    def setupUi(self, TechTG):
        TechTG.setObjectName("TechTG")
        TechTG.resize(567, 515)
        TechTG.setMinimumSize(QtCore.QSize(567, 515))
        TechTG.setMaximumSize(QtCore.QSize(567, 515))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Image/scale_1200.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        TechTG.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(TechTG)
        self.centralwidget.setObjectName("centralwidget")
        self.button_main_win_info_chat = QtWidgets.QPushButton(self.centralwidget)
        self.button_main_win_info_chat.setGeometry(QtCore.QRect(30, 110, 240, 60))
        self.button_main_win_info_chat.setObjectName("button_main_win_info_chat")
        self.button_main_win_info_chat.setToolTip("Выгрузка информации о названии чата,\nколличестве участников и сообщений\nза указанную дату")
        self.button_main_win_info_leader = QtWidgets.QPushButton(self.centralwidget)
        self.button_main_win_info_leader.setGeometry(QtCore.QRect(30, 180, 240, 60))
        self.button_main_win_info_leader.setCheckable(False)
        self.button_main_win_info_leader.setAutoRepeat(False)
        self.button_main_win_info_leader.setObjectName("button_main_win_info_leader")
        self.button_main_win_info_leader.setToolTip("Информация о лидерах чата по колличеству сообщейни")
        self.button_main_win_export_message = QtWidgets.QPushButton(self.centralwidget)
        self.button_main_win_export_message.setGeometry(QtCore.QRect(30, 250, 240, 60))
        self.button_main_win_export_message.setObjectName("button_main_win_export_message")
        self.button_main_win_export_message.setToolTip("Выгрузка всех сообщейни из чата или конкретного пользователя")
        self.button_main_win_export_user = QtWidgets.QPushButton(self.centralwidget)
        self.button_main_win_export_user.setGeometry(QtCore.QRect(30, 320, 240, 60))
        self.button_main_win_export_user.setObjectName("button_main_win_export_user")
        self.button_main_win_export_user.setToolTip("Выгрузка пользователей из чата")
        self.button_main_win_export_contact = QtWidgets.QPushButton(self.centralwidget)
        self.button_main_win_export_contact.setGeometry(QtCore.QRect(280, 110, 240, 60))
        self.button_main_win_export_contact.setObjectName("button_main_win_export_contact")
        self.button_main_win_export_contact.setToolTip("Экспорт контактов из записной книги с привязкой к ID")
        self.button_main_win_add_user = QtWidgets.QPushButton(self.centralwidget)
        self.button_main_win_add_user.setGeometry(QtCore.QRect(280, 180, 240, 60))
        self.button_main_win_add_user.setObjectName("button_main_win_add_user")
        self.button_main_win_add_user.setToolTip("Добавление пользотелей в чат")
        self.button_main_win_delete_user = QtWidgets.QPushButton(self.centralwidget)
        self.button_main_win_delete_user.setGeometry(QtCore.QRect(280, 250, 240, 60))
        self.button_main_win_delete_user.setObjectName("button_main_win_delete_user")
        self.button_main_win_delete_user.setToolTip("Удаление пользователей из чата")
        self.button_main_win_check_number = QtWidgets.QPushButton(self.centralwidget)
        self.button_main_win_check_number.setGeometry(QtCore.QRect(280, 320, 240, 60))
        self.button_main_win_check_number.setObjectName("button_main_win_check_number")
        self.button_main_win_check_number.setToolTip("Попытка добавления номера в контакты для получения его ID")
        self.button_main_win_request_number = QtWidgets.QPushButton(self.centralwidget)
        self.button_main_win_request_number.setGeometry(QtCore.QRect(30, 390, 490, 60))
        self.button_main_win_request_number.setObjectName("button_main_win_request_number")
        self.button_main_win_request_number.setToolTip("")
        # Текст в главном окне
        self.label_main_window = QtWidgets.QLabel(self.centralwidget)
        self.label_main_window.setGeometry(QtCore.QRect(40, 20, 480, 70))
        self.label_main_window.setObjectName("label")
        self.label_main_window.setToolTip("Сведения об авторизации")

        TechTG.setCentralWidget(self.centralwidget)
        # Статус бар
        self.statusbar = QtWidgets.QStatusBar(TechTG)
        self.statusbar.setObjectName("statusbar")
        TechTG.setStatusBar(self.statusbar)

        self.retranslateUi(TechTG)
        QtCore.QMetaObject.connectSlotsByName(TechTG)



    def retranslateUi(self, TechTG):
        _translate = QtCore.QCoreApplication.translate
        TechTG.setWindowTitle(_translate("TechTG", "TechTG"))
        self.centralwidget.setToolTip(_translate("TechTG", "<html><head/><body><p><br/></p></body></html>"))
        self.button_main_win_info_chat.setText(_translate("TechTG", "Информация о чатах"))
        self.button_main_win_info_leader.setText(_translate("TechTG", "Информация о лидерах\n"
                                                       "в чате"))
        self.button_main_win_export_message.setText(_translate("TechTG", "Извлечение сообщений\n"
                                                       "из чата"))
        self.button_main_win_export_user.setText(_translate("TechTG", "Извлечение пользователей\n"
                                                       "из чата"))
        self.button_main_win_export_contact.setText(_translate("TechTG", "Извлечение контактов\n"
                                                       "из учётной записи"))
        self.button_main_win_add_user.setText(_translate("TechTG", "Добавление пользователей\n"
                                                       "в чат\n"
                                                       "(Требуются права администратора)"))
        self.button_main_win_delete_user.setText(_translate("TechTG", "Удаление пользователей\n"
                                                       "из чата\n"
                                                       "(Требуются права администратора)"))
        self.button_main_win_check_number.setText(_translate("TechTG", "Проверка номера\n"
                                                        "на наличие "))
        self.button_main_win_request_number.setText(_translate("TechTG", ""))
        self.label_main_window.setFont(QtGui.QFont('SansSerif', 14))
        self.label_main_window.setText(_translate("TechTG",
                                      "Для использования программы необходимо\nосуществлить авторизацию через меню \"Файл\""))
