# Form implementation generated from reading ui file 'play_view.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow8(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1197, 809)
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("QWidget {\n"
                                 "    color: white;\n"
                                 "    background-color: #121212;\n"
                                 "    font-family: Rubik;\n"
                                 "    font-size: 16pt;\n"
                                 "    font-weight: 600;\n"
                                 "}\n"
                                 "QPushButton {\n"
                                 "    background-color: green;\n"
                                 "    border: none;\n"
                                 "}\n"
                                 "QPushButton:hover {\n"
                                 "    background-color: #7CFC00;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:pressed {\n"
                                 "    background-color: #228B22;\n"
                                 "}\n"
                                 "\n"
                                 "pushButton {\n"
                                 "    background-color: white;\n"
                                 "    border: none;\n"
                                 "}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 100, 321, 31))
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.word = QtWidgets.QLabel(self.centralwidget)
        self.word.setGeometry(QtCore.QRect(550, 90, 361, 41))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.word.setFont(font)
        self.word.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.word.setObjectName("word")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(470, 230, 301, 31))
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 270, 1181, 51))
        self.label_3.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(320, 380, 601, 421))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("img/1.png"))
        self.label_5.setScaledContents(False)
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(310, 20, 621, 31))
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.play_word = QtWidgets.QLabel(self.centralwidget)
        self.play_word.setGeometry(QtCore.QRect(550, 170, 331, 41))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.play_word.setFont(font)
        self.play_word.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.play_word.setObjectName("play_word")
        self.word_3 = QtWidgets.QLabel(self.centralwidget)
        self.word_3.setGeometry(QtCore.QRect(290, 170, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.word_3.setFont(font)
        self.word_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.word_3.setObjectName("word_3")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(470, 340, 301, 31))
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "ЗАГАДАННОЕ СЛОВО:"))
        self.word.setText(_translate("MainWindow", "АВОКАДО"))
        self.label_2.setText(_translate("MainWindow", "ДОСТУПНЫЕ БУКВЫ:"))
        self.label_3.setText(
            _translate("MainWindow", "А Б В Г Д Е Ё Ж З И Й К Л М Н О П Р С Т У Ф Х Ц Ч Ш Щ Ь Ы Ъ Э Ю Я"))
        self.label_4.setText(_translate("MainWindow", "РЕЖИМ НАБЛЮДЕНИЯ ЗА ИГРОЙ"))
        self.play_word.setText(_translate("MainWindow", "АВОКАДО"))
        self.word_3.setText(_translate("MainWindow", "ПОЛЕ ИГРОКА: "))
        self.label_6.setText(_translate("MainWindow", "СТАТУС ВИСЕЛИЦЫ:"))
