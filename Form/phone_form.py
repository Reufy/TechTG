from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TechTG2(object):
# Инициализация и создание формы окна авторизации
    def setupUi(self, TechTG2):
        TechTG2.setObjectName("TechTG")
        TechTG2.resize(567, 515)
        TechTG2.setMinimumSize(QtCore.QSize(300, 300))
        TechTG2.setMaximumSize(QtCore.QSize(300, 300))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../Загрузки/scale_1200.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        TechTG2.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(TechTG2)
        self.centralwidget.setObjectName("centralwidget")
        self.button_modal_window_auth = QtWidgets.QPushButton(self.centralwidget)
        self.button_modal_window_auth.setGeometry(QtCore.QRect(40, 215, 230, 70))
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

        self.label_modal_windows_auth_code = QtWidgets.QLabel(self.centralwidget)
        self.label_modal_windows_auth_code.setGeometry(QtCore.QRect(40, 115, 231, 40))
        self.label_modal_windows_auth_code.setObjectName("label")
        self.lineEdit_modal_windows_code = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_modal_windows_code.setGeometry(QtCore.QRect(40, 165, 230, 40))
        self.lineEdit_modal_windows_code.setCursorPosition(0)
        self.lineEdit_modal_windows_code.setObjectName("lineEdit")
        self.statusbar = QtWidgets.QStatusBar(TechTG2)
        self.retranslateUi(TechTG2)
        QtCore.QMetaObject.connectSlotsByName(TechTG2)
 # Конец инициализация и создание формы окна авторизации



# Первичные данные инициализации
    def retranslateUi(self, TechTG2):
        _translate = QtCore.QCoreApplication.translate
        TechTG2.setWindowTitle(_translate("TechTG", "TechTG"))
        self.lineEdit_modal_windows_auth.setPlaceholderText("375291111111")
        self.centralwidget.setToolTip(_translate("TechTG", "<html><head/><body><p><br/></p></body></html>"))
        self.button_modal_window_auth.setText(_translate("TechTG", "Продолжить"))
        self.label_modal_windows_auth.setText(_translate("TechTG", "Введите номер телефона"))
        self.label_modal_windows_auth_code.setText(_translate("TechTG", "Облачный пароль(при наличии)"))
        self.lineEdit_modal_windows_code.setPlaceholderText("2FA")

# Конец Первичные данные инициализации

