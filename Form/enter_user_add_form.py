from PyQt5.QtWidgets import QApplication, \
    QWidget, QScrollArea, QVBoxLayout, QGroupBox, QLabel, QPushButton, QFormLayout, QCheckBox, QGridLayout
from PyQt5 import QtGui, QtCore
import sys
import time


class Add_User_Form_Class(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "TechTG"
        self.top = 200
        self.left = 500
        self.width = 1000
        self.height = 515
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.resize(900, 515)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.formLayout = QFormLayout()
        self.buttonLayot = QFormLayout()

        # Секция чатов
        self.groupBox = QGroupBox("Список чатов")
        self.comboList = []

        self.groupBox.setLayout(self.formLayout)
        self.scroll = QScrollArea()
        self.scroll.setWidget(self.groupBox)
        self.scroll.setWidgetResizable(True)
        self.scroll.setFixedHeight(550)
        self.scroll.setFixedWidth(1000)
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.scroll)

        # Секция нижних кнопок
        self.button_box = QGroupBox("")
        self.button_export_one_chat = QPushButton("Добавить пользователей в чат")
        self.button_export_one_chat.setMinimumWidth(300)
        self.button_export_one_chat.setMinimumHeight(30)
        self.buttonLayot.addRow(self.button_export_one_chat)
        self.button_box.setLayout(self.buttonLayot)
        self.layout.addWidget(self.button_box)
        self.show()



    def add_chat(self, name):
        for j, i in name.items():
            name = str(i)
            self.button_scroll = QPushButton(name)
            self.button_scroll.setMinimumWidth(300)
            self.button_scroll.setMinimumHeight(30)
            self.button_scroll.setEnabled(True)
            self.comboList.append(self.button_scroll)
            j = int(j) - 1
            self.formLayout.addRow(self.comboList[int(j)])
