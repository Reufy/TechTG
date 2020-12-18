from PyQt5 import QtCore, QtGui, QtWidgets

class EnterDateForm_one_chat(object):
# Инициализация и создание формы окна авторизации
    def setupUi(self, EnterDateForm_one_chat):
        EnterDateForm_one_chat.setObjectName("EnterDateForm_one_chat")
        EnterDateForm_one_chat.resize(567, 515)
        EnterDateForm_one_chat.setMinimumSize(QtCore.QSize(300, 350))
        EnterDateForm_one_chat.setMaximumSize(QtCore.QSize(300, 350))
        self.centralwidget = QtWidgets.QWidget(EnterDateForm_one_chat)
        self.centralwidget.setObjectName("centralwidget")
        self.button_modal_window_auth = QtWidgets.QPushButton(self.centralwidget)
        self.button_modal_window_auth.setGeometry(QtCore.QRect(40, 260, 200, 70))
        self.button_modal_window_auth.setObjectName("button_modal_window_auth")
        #Label
        self.label_modal_windows_request = QtWidgets.QLabel(self.centralwidget)
        self.label_modal_windows_request.setGeometry(QtCore.QRect(40, 20, 231, 40))
        self.label_modal_windows_request.setObjectName("label")
        self.label_modal_windows_year = QtWidgets.QLabel(self.centralwidget)
        self.label_modal_windows_year.setGeometry(QtCore.QRect(40, 70, 231, 40))
        self.label_modal_windows_year.setObjectName("year")
        self.label_modal_windows_mouth = QtWidgets.QLabel(self.centralwidget)
        self.label_modal_windows_mouth.setGeometry(QtCore.QRect(40, 110, 231, 40))
        self.label_modal_windows_mouth.setObjectName("mouth")
        self.label_modal_windows_day = QtWidgets.QLabel(self.centralwidget)
        self.label_modal_windows_day.setGeometry(QtCore.QRect(40, 150, 231, 40))
        self.label_modal_windows_day.setObjectName("day")
        self.label_modal_windows_number_chat = QtWidgets.QLabel(self.centralwidget)
        self.label_modal_windows_number_chat.setGeometry(QtCore.QRect(40, 190, 231, 40))
        self.label_modal_windows_number_chat.setObjectName("number_chat")


        self.lineEdit_modal_windows_year = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_modal_windows_year.setGeometry(QtCore.QRect(100, 70, 100, 35))
        self.lineEdit_modal_windows_year.setCursorPosition(0)
        self.lineEdit_modal_windows_year.setFocus()
        self.lineEdit_modal_windows_year.setMaxLength(4)
        self.lineEdit_modal_windows_year.setInputMask("9999")
        self.lineEdit_modal_windows_year.setObjectName("lineEdit")
        self.lineEdit_modal_windows_mouth = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_modal_windows_mouth.setGeometry(QtCore.QRect(100, 110, 100, 35))
        self.lineEdit_modal_windows_mouth.setCursorPosition(0)
        self.lineEdit_modal_windows_mouth.setMaxLength(2)
        self.lineEdit_modal_windows_mouth.setInputMask("99")
        self.lineEdit_modal_windows_mouth.setObjectName("lineEdit")
        self.lineEdit_modal_windows_day = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_modal_windows_day.setGeometry(QtCore.QRect(100, 150, 100, 35))
        self.lineEdit_modal_windows_day.setCursorPosition(0)
        self.lineEdit_modal_windows_day.setMaxLength(2)
        self.lineEdit_modal_windows_day.setInputMask("99")
        self.lineEdit_modal_windows_day.setObjectName("lineEdit")
        self.lineEdit_modal_windows_number_chat = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_modal_windows_number_chat.setGeometry(QtCore.QRect(100, 195, 100, 35))
        self.lineEdit_modal_windows_number_chat.setCursorPosition(0)
        self.lineEdit_modal_windows_number_chat.setMaxLength(3)
        self.lineEdit_modal_windows_number_chat.setInputMask("999")
        self.lineEdit_modal_windows_number_chat.setObjectName("lineEdit")


        self.statusbar = QtWidgets.QStatusBar(EnterDateForm_one_chat)
        self.retranslateUi(EnterDateForm_one_chat)
        QtCore.QMetaObject.connectSlotsByName(EnterDateForm_one_chat)
 # Конец инициализация и создание формы окна авторизации



# Первичные данные инициализации
    def retranslateUi(self, EnterDateForm_one_chat):
        _translate = QtCore.QCoreApplication.translate
        EnterDateForm_one_chat.setWindowTitle(_translate("EnterDate", "TechTG"))
        self.lineEdit_modal_windows_year.setPlaceholderText("2020")
        self.lineEdit_modal_windows_mouth.setPlaceholderText("01")
        self.lineEdit_modal_windows_day.setPlaceholderText("01")
        self.lineEdit_modal_windows_number_chat.setPlaceholderText("1")
        self.centralwidget.setToolTip(_translate("EnterDate", "<html><head/><body><p><br/></p></body></html>"))
        self.button_modal_window_auth.setText(_translate("EnterDate", "Продолжить"))
        self.label_modal_windows_request.setText(_translate("EnterDate", "Введите интересующую дату"))
        self.label_modal_windows_year.setText(_translate("EnterDate", "Год"))
        self.label_modal_windows_mouth.setText(_translate("EnterDate", "Месяц"))
        self.label_modal_windows_day.setText(_translate("EnterDate", "День"))
        self.label_modal_windows_number_chat.setText(_translate("EnterDate", "Номер\nчата"))





# Конец Первичные данные инициализации