from PyQt5 import QtCore, QtGui, QtWidgets

class Enter_Number_Chat_Add_User_Form(object):
# Инициализация и создание формы окна авторизации
    def setupUi(self, Enter_Number_Chat_Add_User_Form):
        Enter_Number_Chat_Add_User_Form.setObjectName("EnterDateForm_one_chat")
        Enter_Number_Chat_Add_User_Form.resize(567, 515)
        Enter_Number_Chat_Add_User_Form.setMinimumSize(QtCore.QSize(567, 515))
        Enter_Number_Chat_Add_User_Form.setMaximumSize(QtCore.QSize(567, 515))
        self.centralwidget = QtWidgets.QWidget(Enter_Number_Chat_Add_User_Form)
        self.centralwidget.setObjectName("centralwidget")
        self.button_modal_window_auth = QtWidgets.QPushButton(self.centralwidget)
        self.button_modal_window_auth.setGeometry(QtCore.QRect(40, 430, 200, 70))
        self.button_modal_window_auth.setObjectName("button_modal_window_auth")
        #Label
        self.label_modal_windows_request = QtWidgets.QLabel(self.centralwidget)
        self.label_modal_windows_request.setGeometry(QtCore.QRect(40, 20, 231, 40))
        self.label_modal_windows_request.setObjectName("label")
        self.label_modal_windows_number_chat = QtWidgets.QLabel(self.centralwidget)
        self.label_modal_windows_number_chat.setGeometry(QtCore.QRect(40, 70, 231, 40))
        self.label_modal_windows_number_chat.setObjectName("number_chat")
        self.label_modal_windows_add_user = QtWidgets.QLabel(self.centralwidget)
        self.label_modal_windows_add_user.setGeometry(QtCore.QRect(40, 120, 400, 70))
        self.label_modal_windows_add_user.setObjectName("number_chat")


        self.lineEdit_modal_windows_number_chat = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_modal_windows_number_chat.setGeometry(QtCore.QRect(170, 75, 100, 35))
        self.lineEdit_modal_windows_number_chat.setCursorPosition(0)
        self.lineEdit_modal_windows_number_chat.setMaxLength(3)
        self.lineEdit_modal_windows_number_chat.setInputMask("999")
        self.lineEdit_modal_windows_number_chat.setObjectName("lineEdit")

        self.qText_modal_windows_user_name_add = QtWidgets.QTextEdit(self.centralwidget)
        self.qText_modal_windows_user_name_add.setGeometry(QtCore.QRect(40, 200, 300, 200))
        self.qText_modal_windows_user_name_add.setPlaceholderText("@random_name\n@random_name")
        self.qText_modal_windows_user_name_add.setObjectName("lineEdit")


        self.statusbar = QtWidgets.QStatusBar(Enter_Number_Chat_Add_User_Form)
        self.retranslateUi(Enter_Number_Chat_Add_User_Form)
        QtCore.QMetaObject.connectSlotsByName(Enter_Number_Chat_Add_User_Form)
 # Конец инициализация и создание формы окна авторизации



# Первичные данные инициализации
    def retranslateUi(self, Enter_Number_Chat_Add_User_Form):
        _translate = QtCore.QCoreApplication.translate
        Enter_Number_Chat_Add_User_Form.setWindowTitle(_translate("EnterDate", "TechTG"))
        self.lineEdit_modal_windows_number_chat.setPlaceholderText("1")
        self.centralwidget.setToolTip(_translate("EnterDate", "<html><head/><body><p><br/></p></body></html>"))
        self.button_modal_window_auth.setText(_translate("EnterDate", "Продолжить"))
        self.label_modal_windows_request.setText(_translate("EnterDate", "Введите номер чата"))
        self.label_modal_windows_number_chat.setText(_translate("EnterDate", "Номер чата"))
        self.label_modal_windows_add_user.setText(_translate("EnterUser", "Столбиком внесите '@user_name' \nпользователя для добавления в чат\n(Не более 20 пользователей раз в час)"))





# Конец Первичные данные инициализации