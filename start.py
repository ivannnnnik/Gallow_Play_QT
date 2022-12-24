import socket
import sys

from PyQt6.QtWidgets import QMainWindow, QApplication

from design.start_window import DesignStartWindow
import player_1
import player_2


class StartWindow(QMainWindow, DesignStartWindow):
    def __init__(self, user_name=''):
        super(StartWindow, self).__init__()
        self.setupUi(self)
        self.user_name = user_name

        self.save_btn.clicked.connect(self.save_name)
        self.search_btn.clicked.connect(self.search_user)
        self.search_btn.setEnabled(False)

        if user_name != '':
            self.name_line.setText(self.user_name)
            self.save_btn.setText('Change')
            self.status.setText('Nickname saved, you can continue')
            self.name_line.setEnabled(False)
            self.search_btn.setEnabled(True)

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(('127.0.0.1', 1234))

    def save_name(self):
        self.name_line.setEnabled(True)
        nickname = self.name_line.text()
        if len(nickname) < 2:
            self.status.setText('The nickname must be more than 2 characters')
            self.search_btn.setEnabled(False)
        else:
            if self.save_btn.text() == 'Change':
                self.name_line.setEnabled(True)
                self.save_btn.setText('Save')
                self.search_btn.setEnabled(True)
            else:
                self.save_btn.setText('Change')
                self.status.setText('Nickname saved, you can continue')
                self.name_line.setEnabled(False)
                self.search_btn.setEnabled(True)

    def search_user(self):
        self.name_line.setEnabled(False)
        self.save_btn.setEnabled(False)
        self.search_btn.setText("Looking for a second player...")

        QApplication.processEvents()
        print('Looking for a second player...')

        # Отправляю nickname на сервер
        self.user_name = self.name_line.text()
        self.client.send(self.user_name.encode('utf-8'))
        self.number_player = self.client.recv(1024).decode('utf-8')

        # Игрок найден
        if self.number_player == '1':
            self.next_window = player_1.Selection(client=self.client, user_name=self.user_name)
            self.next_window.show()
            self.close()
        else:
            if self.number_player == '2':
                # Окно ожидания для второго игрока
                self.next_window = player_2.Expectation(client=self.client, user_name=self.user_name)
                self.next_window.show()
                self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StartWindow()
    window.show()
    sys.exit(app.exec())
