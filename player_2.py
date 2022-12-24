import socket
import sys

from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QMainWindow, QApplication

import lobi_players
from design.exp2 import Ui_MainWindow3
from design.selection_word import SelectionWordDesign
import gallow_play
from design.expectation import ExpectationDesign


# Окно ожидания для второго игрока
class Expectation(QMainWindow, ExpectationDesign):
    def __init__(self, client, user_name):
        super(Expectation, self).__init__()
        self.setupUi(self)

        self.client = client
        self.user_name = user_name

        QTimer.singleShot(1, self.receive)

    def receive(self):
        message = self.client.recv(1024).decode('utf-8')
        print(f'Cообщение принял игрок 2: {message}')
        if message == 'Будет загадывать игрок 2':
            self.next_window = SelectWord(client=self.client, user_name=self.user_name)
            self.next_window.show()
            self.close()
        else:
            if message == 'Отгадываю':
                # Окно отгадывания
                word = self.client.recv(1024).decode('utf-8')
                print(f'Слово для игры: {word}')

                self.next_window = lobi_players.Lobi(client=self.client, word=word, user_name=self.user_name,
                                                     status='Отгадываю')
                self.next_window.show()
                self.close()


# Игрок_1 отдал право выбрать --> Игрок_2 переходит в это окно
# Окно для загадывания слова
class SelectWord(QMainWindow, SelectionWordDesign):
    def __init__(self, client, user_name):
        super(SelectWord, self).__init__()
        self.setupUi(self)

        self.client = client
        self.user_name = user_name

        self.play_btn_4.clicked.connect(self.conceive_word)
        self.lineEdit.setMaxLength(30)

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
