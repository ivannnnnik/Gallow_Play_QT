import socket
import sys

from PyQt6.QtWidgets import QMainWindow, QApplication

from design.end_window import EndDesign
import start


class EndWindow(QMainWindow, EndDesign):
    def __init__(self, status, word, user_name, client):
        super(EndWindow, self).__init__()
        self.setupUi(self)
        self.status_text = status
        self.play_word = word
        self.user_name = user_name
        self.client = client

        self.label.setText(self.status_text)
        self.word.setText(self.play_word)

        self.pushButton.clicked.connect(self.play)
        self.pushButton_2.clicked.connect(self.out)

    def play(self):
        print('-- Сообщение -- Играю заново')
        self.next_window = start.StartWindow(user_name=self.user_name)
        self.next_window.show()
        self.close()

    def out(self):
        print('-- Сообщение -- Выхожу из игры')
        self.close()
