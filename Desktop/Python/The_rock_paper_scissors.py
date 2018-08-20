import random
import time

langue = True
while langue:
    #Выбор языка
    print('Выбор языка: ')
    print('Русский')
    print('English')
    print('Deutsch')
    lang = input('> ')

#Выполнение русской части игры
    if lang == 'Русский' or lang == 'русский' or lang == 'РУССКИЙ':
        langue = False
        time.sleep(1)
        print('''
    ███─████─███─████─█─█─███─█──█─████
    ──█─█──█─█───█──█─█─█───█─█─█──█──█
    ███─████─█───████─███─███─██───████
    ──█─█──█─█───█──────█───█─█─█──█──█
    ███─█──█─█───█────███─███─█──█─█──█
        ''')
        for load in range (1, 11):
            time.sleep(0.5)
            print (end ='███─', flush = True)
        time.sleep(1)
        print('')
        print('''
    █──█─███─████─████
    █──█─█───█──█─█──█
    █─██─█───████─████
    ██─█─█───█────█──█
    █──█─█───█────█──█
        ''')
        time.sleep(1)
        print('''
    ███──███──███──███
        ''')
        time.sleep(1)
        print('''
    █──█──████──█───██─███──█──█──█
    █─█───█──█──██─███─█────█──█──█
    ██────████──█─█─██─███──████──████
    █─█───█──█──█───██─█────█──█──█──█
    █──█──█──█──█───██─███──█──█──████

    █──█──████──█─█─█──█──█──█──█──█──█───█───█
    █──█──█──█──█████──█──█──█──█──█──█───█───█
    ████──█──█───███───████──█─██──█──█───███─█
    █──█──█──█──█████──█──█──██─█──█──█───█─█─█
    █──█──████──█─█─█──█──█──█──█──█████──███─█

    ████──█─█──█───██─████──███──████
    █─────█─█──██─███─█──█──█────█──█
    ████──███──█─█─██─████──█────████
    █──█────█──█───██─█──█──█────█──█
    ████──███──█───██─█──█──█────█──█
        ''')
        print('')
        time.sleep(1)
        def games_ru():
            quit = True
            game = True
            while game:

                #выбор оппонента
                opp = random.randint(1,3)
                if opp == 1:
                    object = 'Камень'
                elif opp == 2:
                    object = 'Ножницы'
                else:
                    object = 'Бумага'

                print('1) Камень')
                time.sleep(1)
                print('2) Ножницы')
                time.sleep(1)
                print('3) Бумага')
                time.sleep(1)

                try:
                    enter = int(input('Введите номер:\n> '))
                    time.sleep(1)

                    #Проверка выйгрыша
                    if enter == 1:
                        print('')
                        print('Вы выбрали: Камень')
                        time.sleep(1)
                        print('Соперник выбрал: ' + str(object))
                        time.sleep(1)
                        print('')
                        if opp == 1:
                            print('Ничья!')
                            time.sleep(1)
                            print('')
                            game = False
                        elif opp == 2:
                            print('Вы выйграли!')
                            time.sleep(1)
                            print('')
                            game = False
                        else:
                            print('Вы проиграли!')
                            time.sleep(1)
                            print('')
                            game = False

                    elif enter == 2:
                        print('')
                        print('Вы выбрали: Ножницы')
                        time.sleep(1)
                        print('Соперник выбрал: ' + str(object))
                        time.sleep(1)
                        print('')
                        if opp == 1:
                            print('Вы проиграли!')
                            time.sleep(1)
                            print('')
                            game = False
                        elif opp == 2:
                            print('Ничья!')
                            time.sleep(1)
                            print('')
                            game = False
                        else:
                            print('Вы выйграли!')
                            time.sleep(1)
                            print('')
                            game = False


                    elif enter == 3:
                        print('')
                        print('Вы выбрали: Бумагу')
                        time.sleep(1)
                        print('Соперник выбрал: ' + str(object))
                        time.sleep(1)
                        print('')
                        if opp == 1:
                            print('Вы выйграли!')
                            time.sleep(1)
                            print('')
                            game = False
                        elif opp == 2:
                            print('Вы проиграли!')
                            time.sleep(1)
                            print('')
                            game = False
                        else:
                            print('Ничья!')
                            time.sleep(1)
                            print('')
                            game = False

                    else:
                        print('Ошибка')
                        time.sleep(1)
                        print('')
                        print('Выберите указаную цифру!')
                        time.sleep(1)
                        print('')


                except:
                    print('Ошибка')
                    time.sleep(1)
                    print('')
                    print('Напишите целую цифру от 1 до 3!!!')
                    time.sleep(1)
                    print('')

            #добавил чтобы можно было играть несколько раз подрят
            while quit:
                try:
                    exit_exit = True
                    while exit_exit:
                        exit = input('Хотите продолжить? (да/нет)\n> ')
                        time.sleep(1)
                        print('')
                        if exit == 'да' or exit == 'Да' or exit =='ДА' or exit == 'д' or exit == 'Д' or exit == 'y' or exit == 'Y':
                            games_ru()
                            quit = False
                            exit_exit = False
                        elif exit == 'нет' or exit == 'Нет' or exit =='НЕТ' or exit == 'н' or exit == 'Н' or exit == 'n' or exit == 'N':
                            quit = False
                            exit_exit = False
                        else:
                            print ('Ошибка')
                            time.sleep(1)
                            print('')
                except:
                    print ('Ошибка')
                    time.sleep(1)
                    print('')

        games_ru()
        del(games_ru)
        time.sleep(1)
        print('''
    ████──█───█─██─██─████──███
    █──██─█───█──███──█──█──█─█
    ████──███─█───█───█──█──█─█
    █──██─█─█─█──███──█──█─█████
    ████──███─█─██─██─████─█───█
        ''')

    #Execution of the English part of the game
    elif lang == 'English' or lang == 'english' or lang == 'ENGLISH':
        langue = False
        time.sleep(1)
        print('''
    █───████─████─████
    █───█──█─█──█─█──██
    █───█──█─████─█──██
    █───█──█─█──█─█──██
    ███─████─█──█─████
        ''')
        for load in range (1, 10):
            time.sleep(0.5)
            print (end ='███─', flush = True)
        time.sleep(1)
        print('')
        print('''
    ████──████──█───██─███──███
    █─────█──█──██─███─█────█
    █─██──████──█─█─██─███──███
    █──█──█──█──█───██─█──────█
    ████──█──█──█───██─███──███
        ''')
        time.sleep(1)
        print('''
    ███──███──███──███──███──███
        ''')
        time.sleep(1)
        print('''
    ███─███─████─█──█─███
    █────█──█──█─██─█─█
    ███──█──█──█─█─██─███
    ──█──█──█──█─█──█─█
    ███──█──████─█──█─███

    ███─████─███─███─███─████─████─███
    █───█──█──█──█───█───█──█─█──█─█
    ███─█─────█──███─███─█──█─████─███
    ──█─█──█──█────█───█─█──█─█─█────█
    ███─████─███─███─███─████─█─█──███

    ████─████─████─███─████
    █──█─█──█─█──█─█───█──█
    ████─████─████─███─████
    █────█──█─█────█───█─█
    █────█──█─█────███─█─█
        ''')
        print('')
        time.sleep(1)
        def games_en():
            quit = True
            game = True
            while game:

                #the choice of the opponent
                opp = random.randint(1,3)
                if opp == 1:
                    object = 'Stone'
                elif opp == 2:
                    object = 'Scissors'
                else:
                    object = 'Paper'

                print('1) Stone')
                time.sleep(1)
                print('2) Scissors')
                time.sleep(1)
                print('3) Paper')
                time.sleep(1)

                try:
                    enter = int(input('Enter the number:\n> '))
                    time.sleep(1)

                    #Win check
                    if enter == 1:
                        print('')
                        print('You chose the: Stone')
                        time.sleep(1)
                        print('The enemy chose the: ' + str(object))
                        time.sleep(1)
                        print('')
                        if opp == 1:
                            print('Draw!')
                            time.sleep(1)
                            print('')
                            game = False
                        elif opp == 2:
                            print('You win!')
                            time.sleep(1)
                            print('')
                            game = False
                        else:
                            print('You lose!')
                            time.sleep(1)
                            print('')
                            game = False

                    elif enter == 2:
                        print('')
                        print('You chose the: Scissors')
                        time.sleep(1)
                        print('The enemy chose the: ' + str(object))
                        time.sleep(1)
                        print('')
                        if opp == 1:
                            print('You lose!')
                            time.sleep(1)
                            print('')
                            game = False
                        elif opp == 2:
                            print('Draw!')
                            time.sleep(1)
                            print('')
                            game = False
                        else:
                            print('You win!')
                            time.sleep(1)
                            print('')
                            game = False


                    elif enter == 3:
                        print('')
                        print('You chose the: Paper')
                        time.sleep(1)
                        print('The enemy chose the: ' + str(object))
                        time.sleep(1)
                        print('')
                        if opp == 1:
                            print('You win!')
                            time.sleep(1)
                            print('')
                            game = False
                        elif opp == 2:
                            print('Вы lose!')
                            time.sleep(1)
                            print('')
                            game = False
                        else:
                            print('Draw!')
                            time.sleep(1)
                            print('')
                            game = False

                    else:
                        print('Error')
                        time.sleep(1)
                        print('')
                        print('Select the specified number!')
                        time.sleep(1)
                        print('')


                except:
                    print('Error')
                    time.sleep(1)
                    print('')
                    print('Write a whole number from 1 to 3!!!')
                    time.sleep(1)
                    print('')

            #added to be able to play several times in a row
            while quit:
                try:
                    exit_exit = True
                    while exit_exit:
                        exit = input('Want to continue? (yes/no)\n> ')
                        time.sleep(1)
                        print('')
                        if exit == 'yes' or exit == 'Yes' or exit =='YES' or exit == 'y' or exit == 'Y':
                            games_en()
                            quit = False
                            exit_exit = False
                        elif exit == 'no' or exit == 'No' or exit =='NO' or exit == 'n' or exit == 'N':
                            quit = False
                            exit_exit = False
                        else:
                            print ('Error')
                            time.sleep(1)
                            print('')
                except:
                    print ('Error')
                    time.sleep(1)
                    print('')

        games_en()
        del(games_en)
        time.sleep(1)
        print('''
    ███──██─██──███──███
    █─────███────█────█
    ███────█─────█────█
    █─────███────█────█
    ███──██─██──███───█
        ''')

    #Ausführen des deutschen Teils des Spiels
    elif lang == 'Deutsch' or lang == 'deutsch' or lang == 'DEUTSCH':
        langue = False
        time.sleep(1)
        print('''
    █───████─████──███─█──█
    █───█──█─█──██─█───██─█
    █───████─█──██─███─█─██
    █───█──█─█──██─█───█──█
    ███─█──█─████──███─█──█
        ''')
        for load in range (1, 10):
            time.sleep(0.5)
            print (end ='███─', flush = True)
        time.sleep(1)
        print('')
        print('''
    ███─████─███─███─█
    █───█──█──█──█───█
    ███─████──█──███─█
    ──█─█─────█──█───█
    ███─█────███─███─███
        ''')
        time.sleep(1)
        print('''
    ███──███──███──███
        ''')
        time.sleep(1)
        print('''
    ███─███─███─███─█──█
    █────█──█────█──██─█
    ███──█──███──█──█─██
    ──█──█──█────█──█──█
    ███──█──███─███─█──█

    ███─████─█──█─███─████─███
    █───█──█─█──█─█───█──█─█
    ███─█────████─███─████─███
    ──█─█──█─█──█─█───█─█──█
    ███─████─█──█─███─█─█──███

    ████─████─████─███─███─████
    █──█─█──█─█──█──█──█───█──█
    ████─████─████──█──███─████
    █────█──█─█─────█──█───█─█
    █────█──█─█────███─███─█─█
        ''')
        print('')
        time.sleep(1)
        def games_dt():
            quit = True
            game = True
            while game:

                # Gegner auswählen
                opp = random.randint(1,3)
                if opp == 1:
                    object = 'Stein'
                elif opp == 2:
                    object = 'Schere'
                else:
                    object = 'Papier'

                print('1) Stein')
                time.sleep(1)
                print('2) Schere')
                time.sleep(1)
                print('3) Papier')
                time.sleep(1)

                try:
                    enter = int(input('Geben Sie die Nummer ein:\n> '))
                    time.sleep(1)

                    # Gewinnprüfung
                    if enter == 1:
                        print('')
                        print('Sie haben Stein gewählt')
                        time.sleep(1)
                        print('Gegner wählte: ' + str(object))
                        time.sleep(1)
                        print('')
                        if opp == 1:
                            print('Unentschieden!')
                            time.sleep(1)
                            print('')
                            game = False
                        elif opp == 2:
                            print('Sie haben gewonnen!')
                            time.sleep(1)
                            print('')
                            game = False
                        else:
                            print('Sie verloren!')
                            time.sleep(1)
                            print('')
                            game = False

                    elif enter == 2:
                        print('')
                        print('Sie haben Schere gewählt')
                        time.sleep(1)
                        print('Gegner wählte: ' + str(object))
                        time.sleep(1)
                        print('')
                        if opp == 1:
                            print('Sie verloren!')
                            time.sleep(1)
                            print('')
                            game = False
                        elif opp == 2:
                            print('Unentschieden!')
                            time.sleep(1)
                            print('')
                            game = False
                        else:
                            print('Sie haben gewonnen!')
                            time.sleep(1)
                            print('')
                            game = False


                    elif enter == 3:
                        print('')
                        print('Sie haben Papier gewählt')
                        time.sleep(1)
                        print('Gegner wählte: ' + str(object))
                        time.sleep(1)
                        print('')
                        if opp == 1:
                            print('Sie haben gewonnen!')
                            time.sleep(1)
                            print('')
                            game = False
                        elif opp == 2:
                            print('Sie verloren!')
                            time.sleep(1)
                            print('')
                            game = False
                        else:
                            print('Unentschieden!')
                            time.sleep(1)
                            print('')
                            game = False

                    else:
                        print('Fehler')
                        time.sleep(1)
                        print('')
                        print('Wählen Sie die angegebene Ziffer!')
                        time.sleep(1)
                        print('')


                except:
                    print('Fehler')
                    time.sleep(1)
                    print('')
                    print('Schreiben Sie eine ganze Zahl von 1 bis 3!!!')
                    time.sleep(1)
                    print('')

            #Hinzugefügt damit man mehrmals hintereinander spielen
            while quit:
                try:
                    exit_exit = True
                    while exit_exit:
                        exit = input('Willst du weitermachen? (ja/nein)\n> ')
                        time.sleep(1)
                        print('')
                        if exit == 'ja' or exit == 'JA' or exit =='Ja' or exit == 'j' or exit == 'J' or exit == 'y' or exit == 'Y':
                            games_dt()
                            quit = False
                            exit_exit = False
                        elif exit == 'nein' or exit == 'Nein' or exit =='NEIN' or exit == 'n' or exit == 'N':
                            quit = False
                            exit_exit = False
                        else:
                            print ('Fehler')
                            time.sleep(1)
                            print('')
                except:
                    print ('Fehler')
                    time.sleep(1)
                    print('')

        games_dt()
        del(games_dt)
        time.sleep(1)
        print('''
    ████─█─█─███─████─████─█──█─████
    █──█─█─█─█───█────█──█─██─█─█
    ████─█─█─███─█─██─████─█─██─█─██
    █──█─█─█───█─█──█─█──█─█──█─█──█
    █──█─███─███─████─█──█─█──█─████
        ''')

    else:
        pass
