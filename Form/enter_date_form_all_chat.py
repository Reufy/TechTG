from PyQt5 import QtCore, QtGui, QtWidgets

class EnterDateForm(object):
# Инициализация и создание формы окна авторизации
    def setupUi(self, EnterDate):
        EnterDate.setObjectName("EnterDateForm")
        EnterDate.resize(567, 515)
        EnterDate.setMinimumSize(QtCore.QSize(300, 270))
        EnterDate.setMaximumSize(QtCore.QSize(300, 270))
        self.centralwidget = QtWidgets.QWidget(EnterDate)
        self.centralwidget.setObjectName("centralwidget")
        self.button_modal_window_auth = QtWidgets.QPushButton(self.centralwidget)
        self.button_modal_window_auth.setGeometry(QtCore.QRect(40, 190, 200, 70))
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


        self.statusbar = QtWidgets.QStatusBar(EnterDate)
        self.retranslateUi(EnterDate)
        QtCore.QMetaObject.connectSlotsByName(EnterDate)
 # Конец инициализация и создание формы окна авторизации



# Первичные данные инициализации
    def retranslateUi(self, EnterDate):
        _translate = QtCore.QCoreApplication.translate
        EnterDate.setWindowTitle(_translate("EnterDate", "TechTG"))
        self.lineEdit_modal_windows_year.setPlaceholderText("2020")
        self.lineEdit_modal_windows_mouth.setPlaceholderText("01")
        self.lineEdit_modal_windows_day.setPlaceholderText("01")
        self.centralwidget.setToolTip(_translate("EnterDate", "<html><head/><body><p><br/></p></body></html>"))
        self.button_modal_window_auth.setText(_translate("EnterDate", "Продолжить"))
        self.label_modal_windows_request.setText(_translate("EnterDate", "Введите интересующую дату"))
        self.label_modal_windows_year.setText(_translate("EnterDate", "Год"))
        self.label_modal_windows_mouth.setText(_translate("EnterDate", "Месяц"))
        self.label_modal_windows_day.setText(_translate("EnterDate", "День"))





# Конец Первичные данные инициализации