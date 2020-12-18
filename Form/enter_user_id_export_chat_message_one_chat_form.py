from PyQt5 import QtCore, QtGui, QtWidgets

class Enter_User_ID_Export_Message_One_Chat_Form(object):
# Инициализация и создание формы окна авторизации
    def setupUi(self, EnterDateForm_one_chat_id):
        EnterDateForm_one_chat_id.setObjectName("EnterDateForm_one_chat")
        EnterDateForm_one_chat_id.resize(567, 515)
        EnterDateForm_one_chat_id.setMinimumSize(QtCore.QSize(300, 300))
        EnterDateForm_one_chat_id.setMaximumSize(QtCore.QSize(300, 300))
        self.centralwidget = QtWidgets.QWidget(EnterDateForm_one_chat_id)
        self.centralwidget.setObjectName("centralwidget")
        self.button_modal_window_auth = QtWidgets.QPushButton(self.centralwidget)
        self.button_modal_window_auth.setGeometry(QtCore.QRect(40, 200, 200, 70))
        self.button_modal_window_auth.setObjectName("button_modal_window_auth")
        #Label
        self.label_modal_windows_request = QtWidgets.QLabel(self.centralwidget)
        self.label_modal_windows_request.setGeometry(QtCore.QRect(40, 20, 231, 40))
        self.label_modal_windows_request.setObjectName("label")
        self.label_modal_windows_number_chat = QtWidgets.QLabel(self.centralwidget)
        self.label_modal_windows_number_chat.setGeometry(QtCore.QRect(40, 70, 231, 40))
        self.label_modal_windows_number_chat.setObjectName("number_chat")
        self.label_modal_windows_request_user = QtWidgets.QLabel(self.centralwidget)
        self.label_modal_windows_request_user.setGeometry(QtCore.QRect(40, 115, 231, 40))
        self.label_modal_windows_request_user.setObjectName("user_id")



        self.lineEdit_modal_windows_number_chat = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_modal_windows_number_chat.setGeometry(QtCore.QRect(100, 75, 100, 35))
        self.lineEdit_modal_windows_number_chat.setCursorPosition(0)
        self.lineEdit_modal_windows_number_chat.setMaxLength(3)
        self.lineEdit_modal_windows_number_chat.setInputMask("999")
        self.lineEdit_modal_windows_number_chat.setObjectName("lineEdit")
        self.lineEdit_modal_windows_user_id = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_modal_windows_user_id.setGeometry(QtCore.QRect(100, 120, 100, 35))
        self.lineEdit_modal_windows_user_id.setCursorPosition(0)
        self.lineEdit_modal_windows_user_id.setInputMask("999999999999999")
        self.lineEdit_modal_windows_user_id.setObjectName("lineEdit")



        self.statusbar = QtWidgets.QStatusBar(EnterDateForm_one_chat_id)
        self.retranslateUi(EnterDateForm_one_chat_id)
        QtCore.QMetaObject.connectSlotsByName(EnterDateForm_one_chat_id)
 # Конец инициализация и создание формы окна авторизации



# Первичные данные инициализации
    def retranslateUi(self, EnterDateForm_one_chat_id):
        _translate = QtCore.QCoreApplication.translate
        EnterDateForm_one_chat_id.setWindowTitle(_translate("EnterDate", "TechTG"))
        self.lineEdit_modal_windows_number_chat.setPlaceholderText("1")
        self.lineEdit_modal_windows_user_id.setPlaceholderText("111111111")
        self.centralwidget.setToolTip(_translate("EnterDate", "<html><head/><body><p><br/></p></body></html>"))
        self.button_modal_window_auth.setText(_translate("EnterDate", "Продолжить"))
        self.label_modal_windows_request.setText(_translate("EnterDate", "Введите номер чата и ID \nискомого пользователя"))
        self.label_modal_windows_number_chat.setText(_translate("EnterDate", "Номер\nчата"))
        self.label_modal_windows_request_user.setText(_translate("EnterDate", "User\nID"))






# Конец Первичные данные инициализации