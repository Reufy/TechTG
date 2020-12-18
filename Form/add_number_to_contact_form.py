from PyQt5 import QtCore, QtGui, QtWidgets


class EnterNumberToContact(object):
# Инициализация и создание формы окна авторизации
    def setupUi(self, EnterNumberToContact):
        EnterNumberToContact.setObjectName("EnterNumberToContact")
        EnterNumberToContact.resize(567, 515)
        EnterNumberToContact.setMinimumSize(QtCore.QSize(300, 300))
        EnterNumberToContact.setMaximumSize(QtCore.QSize(300, 300))
        self.centralwidget = QtWidgets.QWidget(EnterNumberToContact)
        self.centralwidget.setObjectName("centralwidget")
        self.button_modal_window_auth = QtWidgets.QPushButton(self.centralwidget)
        self.button_modal_window_auth.setGeometry(QtCore.QRect(40, 130, 230, 70))
        self.button_modal_window_auth.setObjectName("button_modal_window_auth")
        self.label_modal_windows_auth = QtWidgets.QLabel(self.centralwidget)
        self.label_modal_windows_auth.setGeometry(QtCore.QRect(40, 20, 231, 40))
        self.label_modal_windows_auth.setObjectName("label")
        self.lineEdit_modal_windows_auth = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_modal_windows_auth.setGeometry(QtCore.QRect(40, 70, 230, 40))
        self.lineEdit_modal_windows_auth.setCursorPosition(0)
        self.lineEdit_modal_windows_auth.setFocus()
        self.lineEdit_modal_windows_auth.setMaxLength(12)
        self.lineEdit_modal_windows_auth.setInputMask("999999999999")
        self.lineEdit_modal_windows_auth.setObjectName("lineEdit")
        self.statusbar = QtWidgets.QStatusBar(EnterNumberToContact)
        self.retranslateUi(EnterNumberToContact)
        QtCore.QMetaObject.connectSlotsByName(EnterNumberToContact)

 # Конец инициализация и создание формы окна авторизации



# Первичные данные инициализации
    def retranslateUi(self, TechTG2):
        _translate = QtCore.QCoreApplication.translate
        TechTG2.setWindowTitle(_translate("TechTG", "TechTG"))
        self.lineEdit_modal_windows_auth.setPlaceholderText("375291111111")
        self.centralwidget.setToolTip(_translate("TechTG", "<html><head/><body><p><br/></p></body></html>"))
        self.button_modal_window_auth.setText(_translate("TechTG", "Продолжить"))
        self.label_modal_windows_auth.setText(_translate("TechTG", "Введите номер телефона"))

# Конец Первичные данные инициализации

