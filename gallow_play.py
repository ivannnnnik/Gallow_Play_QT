import socket
import sys

from PyQt6 import QtGui, QtWidgets
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton
from design.play_window import PLayWindowDesign
from design.play_view_window import PlayViewDesign
from end import EndWindow


# Основное окно игры
class Play(QMainWindow, PLayWindowDesign):
    def __init__(self, client, word, user_name):
        super(Play, self).__init__()
        self.setupUi(self)

        self.client = client
        self.play_word = word
        self.user_name = user_name
        self.counter_png = 1
        self.word.setText(self.play_word)
        self.pushButton.clicked.connect(self.guess_push)

    def guess_push(self):
        line_letter = self.lineEdit.text()
        if len(line_letter) == 0:
            self.label_4.setText('ENTER THE LETTER')
        else:
            # Отправляю букву
            self.client.send(line_letter.encode('utf-8'))
            # Принимаю ответ (Угадал или Не угадал)
            status = self.client.recv(1024).decode('utf-8')
            print(f'status: {status}')

            if status == 'Выберите букву из списка':
                self.label_4.setText('INACCESSIBLE LETTER')

            elif status == 'Угадал':
                word = self.client.recv(1024).decode('utf-8')
                self.client.send('Слово пришло'.encode('utf-8'))
                list_letters = self.client.recv(1024).decode('utf-8')

                self.label_4.setText('ENTER A LETTER')
                self.word.setText(word)
                self.label_3.setText(list_letters)

            elif status == 'Не угадал':
                self.counter_png += 1

                list_letters = self.client.recv(1024).decode('utf-8')

                self.label_4.setText('ENTER A LETTER')
                self.label_3.setText(list_letters)
                self.label_5.setPixmap(QtGui.QPixmap(f"img/{self.counter_png}.png"))

            elif status == 'Ты проиграл':
                self.counter_png += 1

                list_letters = self.client.recv(1024).decode('utf-8')
                self.client.send('flag'.encode('utf-8'))
                word = self.client.recv(1024).decode('utf-8')

                self.label_3.setText(list_letters)
                self.label_5.setPixmap(QtGui.QPixmap(f"img/{self.counter_png}.png"))

                self.next_window = EndWindow(status="YOU'VE LOST", word=word, user_name=self.user_name,
                                             client=self.client)
                self.next_window.show()
                self.close()

            else:
                if status == 'Ты выиграл':
                    word = self.client.recv(1024).decode('utf-8')
                    self.client.send('flag'.encode('utf-8'))
                    list_letters = self.client.recv(1024).decode('utf-8')

                    self.word.setText(word)
                    self.label_3.setText(list_letters)

                    self.next_window = EndWindow(status='YOU WIN !!!', word=word, user_name=self.user_name,
                                                 client=self.client)
                    self.next_window.show()
                    self.close()


# Окно для просмотра игры
class PlayView(QMainWindow, PlayViewDesign):
    def __init__(self, client, word, user_name):
        super(PlayView, self).__init__()
        self.setupUi(self)

        self.client = client
        self.g_word = word  # Загаданное слово
        self.play_word.setText(' ' + ' '.join(['_' for i in range(len(word))]))
        self.user_name = user_name
        self.counter_png = 1
        self.word.setText(self.g_word)

        QTimer.singleShot(1, self.receive)

    def receive(self):
        while True:
            status = self.client.recv(1024).decode('utf-8')
            print(f'status: {status}')

            if status == 'Угадал':
                word = self.client.recv(1024).decode('utf-8')
                self.client.send('Слово пришло'.encode('utf-8'))
                list_letters = self.client.recv(1024).decode('utf-8')

                self.label_3.setText(list_letters)
                self.play_word.setText(word)

                QApplication.processEvents()

            elif status == 'Не угадал':
                self.counter_png += 1

                list_letters = self.client.recv(1024).decode('utf-8')

                self.label_3.setText(list_letters)
                self.label_5.setPixmap(QtGui.QPixmap(f"img/{self.counter_png}.png"))

                QApplication.processEvents()

            elif status == 'Ты проиграл':
                self.counter_png += 1

                list_letters = self.client.recv(1024).decode('utf-8')
                self.client.send('flag'.encode('utf-8'))
                word = self.client.recv(1024).decode('utf-8')

                self.label_3.setText(list_letters)
                self.label_5.setPixmap(QtGui.QPixmap(f"img/{self.counter_png}.png"))

                QApplication.processEvents()

                self.next_window = EndWindow(status='THE OPPONENT LOST', word=word, user_name=self.user_name,
                                             client=self.client)
                self.next_window.show()
                self.close()
                break

            else:
                if status == 'Ты выиграл':
                    word = self.client.recv(1024).decode('utf-8')
                    self.client.send('flag'.encode('utf-8'))
                    list_letters = self.client.recv(1024).decode('utf-8')

                    self.word.setText(word)
                    self.label_3.setText(list_letters)
                    self.next_window = EndWindow(status='THE OPPONENT WIN', word=word, user_name=self.user_name,
                                                 client=self.client)
                    self.next_window.show()
                    self.close()
                    break
