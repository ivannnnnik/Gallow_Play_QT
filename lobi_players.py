import threading

from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QMainWindow, QApplication

import gallow_play
from design.lobi_players import LobiPlayersDesign


class Lobi(QMainWindow, LobiPlayersDesign):
    def __init__(self, word, client, user_name, status):
        super(Lobi, self).__init__()
        self.setupUi(self)

        self.client = client
        self.user_name = user_name
        self.word = word
        self.status = status
        self.start_game.clicked.connect(self.start)

        QTimer.singleShot(1, self.receive)

    def receive(self):
        self.client.send('Лобби'.encode('utf-8'))
        nickname_player = self.client.recv(1024).decode('utf-8')

        self.message.setText(f'{nickname_player} waiting for the game with you !')

    def start(self):
        self.client.send(f'{self.user_name} готов'.encode('utf-8'))
        self.start_game.setText('We are waiting for the second player...')
        QApplication.processEvents()
        message = self.client.recv(1024).decode('utf-8')
        if message == 'Начинаем':
            if self.status == 'Отгадываю':
                self.next_window = gallow_play.Play(client=self.client, word=self.word.upper(),
                                                    user_name=self.user_name)
                self.next_window.show()
                self.close()
            else:
                self.next_window = gallow_play.PlayView(client=self.client, word=self.word.upper(),
                                                        user_name=self.user_name)
                self.next_window.show()
                self.close()
