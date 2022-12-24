import os
import socket
import threading
import random

host = '127.0.0.1'
port = 1234

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

games = {}
nicknames = {}
clients = []


def create_game(client):
    if len(clients) == 1:
        clients.append(client)

        game_number = random.randint(1000, 9999)
        games[game_number] = [clients[0], clients[1]]

        clients[0].send('1'.encode('utf-8'))
        clients[1].send('2'.encode('utf-8'))

        print(f'Игра: #{game_number} началась ! ')

        thread = threading.Thread(target=handle, args=(game_number,))
        thread.start()
        clients.clear()
    else:
        clients.append(client)


def handle(game_number):
    player_1 = games[game_number][0]
    player_2 = games[game_number][1]

    # Спрашиваю про режим игры
    message = player_1.recv(1024).decode('utf-8')
    if message == 'Буду отгадывать)-=!3':
        print(f'-- Сообщение --  Игрок 1: {message}')

        player_2.send('Будет загадывать игрок 2'.encode('utf-8'))
        player_1.send('Игрок 2 загадывает слово'.encode('utf-8'))

        word = player_2.recv(1024).decode('utf-8')
        word = word.upper()
        word_play = ' ' + ' '.join(['_' for i in range(len(word))])

        player_1.send(word_play.encode('utf-8'))

        print(f'-- Сообщение -- Игрок 2: загадывает слово: {word}')
        looking_player = player_2
        playing_player = player_1

        flag_1 = player_1.recv(1024).decode('utf-8')
        flag_2 = player_2.recv(1024).decode('utf-8')
        if flag_1 and flag_2:
            looking_player.send(nicknames[player_2].encode('utf-8'))
            playing_player.send(nicknames[player_1].encode('utf-8'))

    else:
        print('Игрок 1 будет загадывать')
        print(f'-- Сообщение --  Игрок 1: Загадывает слово: {message}')

        player_2.send('Отгадываю'.encode('utf-8'))

        word = message.upper()
        word_play = ' ' + ' '.join(['_' for i in range(len(word))])

        player_2.send(word_play.encode('utf-8'))

        looking_player = player_1
        playing_player = player_2

        flag_1 = player_1.recv(1024).decode('utf-8')
        flag_2 = player_2.recv(1024).decode('utf-8')
        if flag_1 and flag_2:
            looking_player.send(nicknames[player_1].encode('utf-8'))
            playing_player.send(nicknames[player_2].encode('utf-8'))

    # Lobbi
    message_p_1 = looking_player.recv(1024).decode('utf-8')
    message_p_2 = playing_player.recv(1024).decode('utf-8')
    looking_player.send('Начинаем'.encode('utf-8'))
    playing_player.send('Начинаем'.encode('utf-8'))


    list_letters = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z '
    counter_trouble = 0
    stop = True
    while stop:
        letter = playing_player.recv(1024).decode('utf-8')
        letter = letter.upper()
        # Подставляю буквы вместо _ в слове
        if letter in list_letters and letter != ' ':
            if letter in word:
                word_play = list(word_play)
                for i in range(len(word)):
                    if letter == word[i]:
                        word_play[i * 2 + 1] = letter
                word_play = ''.join(word_play)

                if word_play.find('_') == -1:  # Выиграл
                    playing_player.send('Ты выиграл'.encode('utf-8'))
                    looking_player.send('Ты выиграл'.encode('utf-8'))

                    list_letters = list_letters.replace(f'{letter} ', '')

                    playing_player.send(word_play.encode('utf-8'))
                    looking_player.send(word_play.encode('utf-8'))

                    flag_1 = playing_player.recv(1024).decode('utf-8')
                    flag_2 = looking_player.recv(1024).decode('utf-8')

                    if flag_1 and flag_2:
                        playing_player.send(list_letters.encode('utf-8'))
                        looking_player.send(list_letters.encode('utf-8'))
                        stop = False

                else:  # Угадал
                    playing_player.send('Угадал'.encode('utf-8'))
                    looking_player.send('Угадал'.encode('utf-8'))

                    list_letters = list_letters.replace(f'{letter} ', '')

                    playing_player.send(word_play.encode('utf-8'))
                    looking_player.send(word_play.encode('utf-8'))

                    flag_1 = playing_player.recv(1024).decode('utf-8')
                    flag_2 = looking_player.recv(1024).decode('utf-8')

                    if flag_1 and flag_2:
                        playing_player.send(list_letters.encode('utf-8'))
                        looking_player.send(list_letters.encode('utf-8'))

            # Не угадал
            else:
                counter_trouble += 1
                if counter_trouble == 6:
                    playing_player.send('Ты проиграл'.encode('utf-8'))
                    looking_player.send('Ты проиграл'.encode('utf-8'))

                    list_letters = list_letters.replace(f'{letter} ', '')

                    playing_player.send(list_letters.encode('utf-8'))
                    looking_player.send(list_letters.encode('utf-8'))

                    flag_1 = playing_player.recv(1024).decode('utf-8')
                    flag_2 = looking_player.recv(1024).decode('utf-8')

                    if flag_1 and flag_2:
                        playing_player.send(word.encode('utf-8'))
                        looking_player.send(word.encode('utf-8'))
                        stop = False
                else:
                    playing_player.send('Не угадал'.encode('utf-8'))
                    looking_player.send('Не угадал'.encode('utf-8'))

                    list_letters = list_letters.replace(f'{letter} ', '')

                    playing_player.send(list_letters.encode('utf-8'))
                    looking_player.send(list_letters.encode('utf-8'))
        else:
            playing_player.send('Выберите букву из списка'.encode('utf-8'))
            looking_player.send('Выберите букву из списка'.encode('utf-8'))

    games.pop(game_number)
    print(f'Игра : #{game_number} завершена !')


def receive():
    while True:
        client, address = server.accept()
        print("Connected with {}".format(str(address)))
        nickname = client.recv(1024).decode('utf-8')
        nicknames[client] = nickname
        print("Nickname is {}".format(nickname))
        create_game(client)


# os.system('clear')
receive()
