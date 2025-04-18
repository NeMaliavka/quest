def quiz():
    q = {'Какое любимое блюдо Наруто Удзумаки ?': [['Данго',
                                                           'Рамен',
                                                           'Суши'],
                                                           ['Рамен', '2']],
                 'Как звали наставницу Сакуры Харуно ?': [['Цунаде',
                                                          'Гурен',
                                                          'Шизуне'],
                                                          ['Цунаде','1']],
                 
                 'Какой из перечисленных техник обладал Саске Учиха ?':[['Магнитный Расенган',
                                                                         'Воздушные пули',
                                                                         'Портал Риннегана'],['Портал Риннегана','3']],
                 'Сколько всего Хвостатых ?': [['9',
                                               '10',
                                               '12'],['9','2']],
                 'В каком эпизоде Саске Учиха покинул деревню ?': [['205',
                                                                    '444',
                                                                    '366'], ['444','2']],
                 'Кто убил Асуму Сарутоби ?':[['Хидан',
                                               'Дейдара',
                                               'Какузу'],['Хидан' ,'1']],
                 'Когда вышел первой эпизод аниме Наруто ?': [['3 октября 2002 года',
                                                               '1 января 2003 года',
                                                               '24 июня 2001 года'],['3 октября 2002 года', '1']],
                 'Кто был втором по счету Хокаге ?': [['Хирузен Сарутоби',
                                                       'Тобирама Сенджу',
                                                       'Минато Намиказе'],['Тобирама Сенджу', '2']],
                 'Какой иероглиф изображен на лбу Гаары ?': [['恋',
                                                              '感',
                                                              '愛'], ['愛', '3']],
                 'Какое животное мог призывать Джирайя ?':[['Собаку',
                                                            'Улитку',
                                                            'Жабу'],['Жабу', '3']]}
    return q

def game_quiz(name, flag):
    global answer_dict, count
    game_flag = True
    if flag:
        print(f'''
Правила данной игры:
Я буду задавать вопросы, а Вам {name},
предстоит дать как можно больше правильных ответов.
Будьте внимательны при ответе,
ведь Вам будет дана лишь одна попытка.
(Можно вводить сам ответ или только его номер).

Всего вопросов в викторине {len(quiz())}
Чем больше правильных ответов Вы мне дадите,
тем больше очков я Вам начислю.

Игру можно прервать, просто написав слово "стоп"

Удачи! \N{winking face}
''')
        flag = False
    while game_flag:
        game = 1
        quiz_questions = quiz()
        for q in quiz_questions:
            print(f'''
Вопрос: {game}
{q}''')
            print(f'''
Варианты ответов:
1 {quiz_questions[q][0][0]}
2 {quiz_questions[q][0][1]}
3 {quiz_questions[q][0][2]}''')
            u_a = input(f'Ваш ответ, {name}: ')
            if u_a.lower() == quiz_questions[q][1][0].lower() or u_a == quiz_questions[q][1][1]:
                print(f'Вы абсолютно правы! {quiz_questions[q][1][0]}')
                count+=1
            elif u_a.lower() == 'стоп':
                print(f'''
Игра остановлена.
За время игры очков было набрано: {count}
Из максимально доступных: {len(quiz())}
Всего доброго!
Приходите играть ещё!''')
                game_flag = False
                break
            else:
                print(f'Ты ответил {u_a}, но правильным ответом является: {quiz_questions[q][1][0]}')
            game+=1
            answer_dict[q] = {'Правильный ответ: ': [quiz_questions[q][1][0],
                                                   quiz_questions[q][1][1]],
                              'Ответ игрока: ': u_a}
        else:
            print(f'''
Невероятно!
{name}, ты полностью прошел игру!
Твой счёт {count} очков из возможных {len(quiz())}.
Спасибо за интересную игру!''')
            game_flag = False                              

def hello(name = 'Гость'):
    if name == 'Гость':
        user_name = input('Как я могу к Вам обращаться? ').title()
        while True:
            if user_name:
                hello(user_name)
                break
            else:
                user_name = input('Как я могу к Вам обращаться? ').title()
    else:
        print(f'''
Привет, {name}!
Хотели бы Вы пройти викторину?
(Варианты ответов: да/нет)''')
        flag = True
        answer = input(f'Каков будет твой ответ, {name}: ').lower()
        if answer == 'да':
            game_quiz(name, flag)
        elif answer == 'нет':
            print('Мне очень жаль.. :(')
            print('Заходи поиграть!')
        else:
            print('Я не понимаю твой ответ...')
            print('Может попробуем ещё раз? ')
            answer = input(f'Каков будет твой ответ, {name}: ').lower()
            if answer == 'да':
                game_quiz(name, flag)
            else:
                print('Пока-пока!')
                

answer_dict = {}
count = 0
hello()

with open('game_over.txt', 'a', encoding = 'utf-8') as file:
    for i in answer_dict:
        file.write(i)
        file.write('\n')
        for j in answer_dict[i]:
            file.write(j)
            file.write(': ')
            if len(answer_dict[i][j]) == 2:
                file.write(answer_dict[i][j][0])
                file.write(', ')
                file.write(answer_dict[i][j][1])
                file.write('\n')
            else:
                file.write(answer_dict[i][j][0])
        file.write('\n')
        file.write('-*-*-')
        file.write('\n')
    if count == len(quiz()):
        file.write('Отличный результат')
    elif count >= len(quiz())//2:
        file.write('Хороший результат')
    elif count < len(quiz())//2 and count >= len(quiz())//3:           
        file.write('Средний результат')
    else:
        file.write('Низкий результат')
file.close()
















        

