# Form implementation generated from reading ui file 'serv.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow2(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1195, 827)
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
        self.label.setGeometry(QtCore.QRect(0, 10, 1191, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.status = QtWidgets.QLabel(self.centralwidget)
        self.status.setGeometry(QtCore.QRect(10, 110, 1181, 51))
        self.status.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.status.setObjectName("status")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 190, 1191, 121))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(10, 20, 561, 71))
        self.lineEdit.setObjectName("lineEdit")
        self.play_btn_4 = QtWidgets.QPushButton(self.groupBox)
        self.play_btn_4.setGeometry(QtCore.QRect(600, 20, 581, 71))
        self.play_btn_4.setCheckable(False)
        self.play_btn_4.setChecked(False)
        self.play_btn_4.setObjectName("play_btn_4")
        self.play_btn = QtWidgets.QPushButton(self.centralwidget)
        self.play_btn.setGeometry(QtCore.QRect(10, 380, 561, 111))
        self.play_btn.setCheckable(False)
        self.play_btn.setChecked(False)
        self.play_btn.setObjectName("play_btn")
        self.play_btn_3 = QtWidgets.QPushButton(self.centralwidget)
        self.play_btn_3.setGeometry(QtCore.QRect(600, 380, 581, 111))
        self.play_btn_3.setCheckable(False)
        self.play_btn_3.setChecked(False)
        self.play_btn_3.setObjectName("play_btn_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Gallows"))
        self.label.setText(_translate("MainWindow", "ВИСЕЛИЦА"))
        self.status.setText(_translate("MainWindow", "ВЫБЕРИТЕ РЕЖИМ"))
        self.play_btn_4.setText(_translate("MainWindow", "ЗАГАДАТЬ"))
        self.play_btn.setText(_translate("MainWindow", "ЗАГАДЫВАЮ"))
        self.play_btn_3.setText(_translate("MainWindow", "ОТГАДЫВАЮ"))
