import socket
import sys

from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QMainWindow, QApplication

import lobi_players
from design.expectation import ExpectationDesign
from design.mode_selection_window import SelectionWindow
import gallow_play
from design.lobi import LobiDesign


# Выбор режима --> Загадывает слово & Угадывает
class Selection(QMainWindow, SelectionWindow):
    def __init__(self, client, user_name):
        super(Selection, self).__init__()
        self.setupUi(self)
        self.client = client
        self.user_name = user_name

        self.play_btn.clicked.connect(self.conceive)  # Загадываю
        self.play_btn_3.clicked.connect(self.guess)  # Отгадываю

        self.play_btn_4.setEnabled(False)
        self.lineEdit.setEnabled(False)

        self.play_btn_4.hide()
        self.lineEdit.hide()

        self.lineEdit.setMaxLength(25)
        self.play_btn_4.clicked.connect(self.conceive_word)

    # Отгадывать
    def guess(self):
        self.client.send('Буду отгадывать)-=!3'.encode('utf-8'))
        message = self.client.recv(1024).decode('utf-8')

        if message:
            print('Сообщение пришло')
            self.next_window = Expectation(client=self.client, user_name=self.user_name)
            self.next_window.show()
            self.close()

    # Переход к окну

    # Загадать
    def conceive(self):
        self.play_btn_4.show()
        self.lineEdit.show()

        self.play_btn_4.setEnabled(True)
        self.lineEdit.setEnabled(True)

        self.play_btn.hide()
        self.play_btn_3.hide()

    def conceive_word(self):
        check_symb = list(map(chr, range(65, 91))) + list(map(chr, range(97, 123)))
        word = self.lineEdit.text()
        check_word = True

        if len(word) < 2:
            self.status.setText('THE WORD MUST BE AT LEAST 2 CHARACTERS LONG')
            check_word = False

        for i in range(len(word)):
            if word[i] not in check_symb:
                self.status.setText('ENTER THE CORRECT WORD')
                check_word = False

        if check_word is True:
            self.client.send(f'{word}'.encode('utf-8'))
            self.next_window = lobi_players.Lobi(client=self.client, word=word.upper(), user_name=self.user_name,
                                                 status='Загадываю')
            self.next_window.show()
            self.close()
            print(f'Игрок загадал слово: {word} ')


# Выбирает отгадываю --> Окно ожидания
class Expectation(QMainWindow, ExpectationDesign):
    def __init__(self, client, user_name):
        super(Expectation, self).__init__()
        self.setupUi(self)

        self.client = client
        self.user_name = user_name

        QTimer.singleShot(1, self.receive)

    def receive(self):
        message = self.client.recv(1024).decode('utf-8')
        print(f'Слово для игры: {message}')
        if message:
            self.next_window = lobi_players.Lobi(client=self.client, word=message, user_name=self.user_name,
                                                 status='Отгадываю')
            self.next_window.show()
            self.close()
