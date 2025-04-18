import telebot
from telebot import types
import random


token = 'token'

bot = telebot.TeleBot(token)
hp = damage = exp = 0
lvl = 1

my_victim = ''

race_database = {
    'Эльф': {'hp': 15, 'damage': 35},
    'Гном' : {'hp': 35, 'damage' : 20},
    'Человек' : {'hp': 25, 'damage': 25}
    }
prof_database = {
    'Лучник': {'hp': 25, 'damage' : 35},
    'Воин': {'hp': 50, 'damage': 20},
    'Маг' : {'hp': 15, 'damage': 70}
}

def make_race_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for race in race_database.keys():
        markup.add(types.KeyboardButton(text=race))
    return markup

def make_prof_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for prof in prof_database.keys():
        markup.add(types.KeyboardButton(text=prof))
    return markup




def create_monster():
    rnd_name = random.choice(monster)
    rnd_hp = random.randint(30,55)
    rnd_damage = random.randint(50, 80)
    return [rnd_name, rnd_hp, rnd_damage]





def main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Начать игру")
    btn2 = types.KeyboardButton("Об игре...")
    markup.add(btn1, btn2)
    return markup


#Декоратор @message_handler реагирует на входящие сообщение
#Message – это объект из Bot API, содержащий в себе
#информацию о сообщении. Полезные поля:
#message.chat.id – идентификатор чата
#message.from.id – идентификатор пользователя
#message.text – текст сообщения
#Функция send_message принимает идентификатор чата
#(берем его из сообщения) и текст для отправки.
@bot.message_handler(commands=['start'])
def start_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Начать игру")
    btn2 = types.KeyboardButton("Об игре...")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text = 'Привет, готов поиграть?', reply_markup = markup)

def start_quest():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = 'В путь!'
    btn2 = 'Вернуться в главное меню'
    markup.add(btn1, btn2)
    return markup

@bot.message_handler(content_types=['text'])
def main(message):
    global hp, damage, exp, lvl, my_victim
    victim = create_monster()
    if (message.text == "Начать игру"):
        hp = damage = exp = 0
        bot.send_message(message.chat.id, text='Выбери расу персонажа:', reply_markup=make_race_menu())
    elif (message.text == "Вернуться в главное меню"):
        bot.send_message(message.chat.id,
                         text = 'Вы вернулись в главное меню',
                         reply_markup = main_menu())
    if (message.text == 'Эльф'):
        hp += race_database['Эльф']['hp']
        damage += race_database['Эльф']['damage']
        text = f'Вы высокородный эльф, и сейчас ваше здоровье равно:{hp}, а урон равен:{damage}. Осталось выбрать профессию'
        img = open('elf2.jpg', 'rb')        
        bot.send_photo(message.chat.id, img, caption = text, reply_markup = make_prof_menu())
        
        #bot.send_message(message.chat.id, reply_markup = make_prof_menu())
    if (message.text == 'Гном'):
        hp += race_database['Гном']['hp']
        damage += race_database['Гном']['damage']
        text =f'Вы крепкий гном, и сейчас ваше здоровье равно:{hp}, а урон равен:{damage}. Осталось выбрать профессию'
        #img = open('gnom.jpg', 'rb')
        img = open('dworf.jpg', 'rb')
        bot.send_photo(message.chat.id, img, caption = text, reply_markup = make_prof_menu())
        
    if (message.text == 'Человек'):
        hp += race_database['Человек']['hp']
        damage += race_database['Человек']['damage']
        text = f'Вы бесстрашный герой, и сейчас ваше здоровье равно:{hp}, а урон равен:{damage}. Осталось выбрать профессию'
        img = open('chel2.jpg', 'rb') 
        bot.send_photo(message.chat.id, img, caption = text, reply_markup = make_prof_menu())        
    if (message.text == 'Лучник'):
        hp += prof_database['Лучник']['hp']
        damage+= prof_database['Лучник']['damage']
        text = f'Вы высококлассный лучник, а это значит, что ваше здоровье равно:{hp}, а урон равен:{damage}. Вперед к приключениям?'
        img = open('luk-2.jpg', 'rb') 
        bot.send_photo(message.chat.id, img, caption = text, reply_markup = start_quest()) 
    if (message.text == 'Воин'):
        hp += prof_database['Воин']['hp']
        damage+= prof_database['Воин']['damage']
        text = f'Вы неудержимый боец, а это значит, что ваше здоровье равно:{hp}, а урон равен:{damage}. Вперед к приключениям?'
        img = open('sekira.jpg', 'rb') 
        bot.send_photo(message.chat.id, img, caption = text, reply_markup = start_quest()) 
    if (message.text == 'Маг'):
        hp += prof_database['Маг']['hp']
        damage+= prof_database['Маг']['damage']
        text = f'Вы могущественный маг, а это значит, что ваше здоровье равно:{hp}, а урон равен:{damage}. Вперед к приключениям?'
        img = open('posoh2.jpg', 'rb') 
        bot.send_photo(message.chat.id, img, caption = text,
                       reply_markup = start_quest()) 



    if (message.text == 'В путь!'):        
        event = random.randint(1,4)
        if event == 1 or event == 3 or event ==4:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button3 = 'В путь!'
            button4 = 'Вернуться в главное меню'
            markup.add(button3, button4)
            text = "Пока никто не встретился... Идём дальше?"
            img = open(random.choice(go_game), 'rb')
            #bot.send_message(message.chat.id, text = "Пока никто не встретился... Идём дальше?" , reply_markup = markup)
            bot.send_photo(message.chat.id, img, caption = text,
                           reply_markup = markup)
        elif event == 2:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button5 = 'Атаковать'
            button6 = 'Бежать'
            button7 = 'Вернуться в главное меню'
            victim = create_monster()
            my_victim = victim
            print(victim[2])
            print(type(victim))
            markup.add(button5, button6, button7)
            text = f"Ого! Встретился монстр! Монстра зовут {victim[0]}, у него {victim[1]} очков здоровья и вот такой урон:{victim[2]} " 
            img = open(random.choice(monster_image), 'rb')
            bot.send_photo(message.chat.id, img, caption = text,
                           reply_markup = markup)





            
    if (message.text == 'Атаковать'):       
        victim[1] -= damage 
        print(f' hp monstr: {victim[1]}')       
        if victim[1] <= 0:
            exp+=10 * lvl
            if exp >= lvl*30:
                lvl+=1
                hp+=25*lvl
                damage+=15*lvl
                bot.send_message(message.chat.id, text = f'Твой уровень повысился! \
Теперь у тебя {lvl} уровень. hp:{hp}, damage:{damage}')
            text = f'Враг повержен! За победу \
ты получаешь {10*lvl} очков опыта. Теперь у тебя: {exp} очков. Продожаем путешествие?'
            bot.send_photo(message.chat.id, (open('victory.jpg', 'rb')),
                           caption = text, reply_markup = start_quest())
        elif victim[1] > 0:
            hp -= victim[2] 
            print(f'hp hero: {hp}')
            bot.send_message(message.chat.id, text = f'Монстр атакаует!') 
            if hp <= 0:
                text = 'Победа осталась за монстром!'
                bot.send_photo(message.chat.id, (open('defeat.jpg', 'rb')),
                               caption = text,
                               reply_markup = main_menu())
            elif hp > 0:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                button5 = 'Атаковать'
                button6 = 'Бежать'
                button7 = 'Вернуться в главное меню'
                bot.send_message(message.chat.id,
                                 text = f' Теперь у монстра {victim[1]} \
очков здоровья и {victim[2]} урон, а у тебя {hp} очков здоровья. Что будешь делать?',
                                 reply_markup = markup)
    elif (message.text == 'Бежать'):
        plan=random.randint(1,2)
        if plan==1:
            bot.send_message(message.chat.id,
                             text = f'Вы сумели сбежать от монстра!Продожаем путешествие?',
                             reply_markup = start_quest())
        elif plan==2:
            hp -= victim[2] 
            bot.send_message(message.chat.id, text = f'О ужас! Побег не удался и монстр атакаует!') 
            if hp <= 0:
                text = 'Победа осталась за монстром!'
                bot.send_photo(message.chat.id,
                               (open('defeat.jpg', 'rb')),
                               caption = text, reply_markup = main_menu())
            elif hp > 0:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                button5 = 'Атаковать'
                button6 = 'Бежать'
                button7 = 'Вернуться в главное меню'
                bot.send_message(message.chat.id, text = f' Теперь у монстра {victim[1]} \
очков здоровья и {victim[2]} урон, а у тебя {hp} очков здоровья. Что будешь делать?', reply_markup = markup)
             
monster = ['Solid', 'Bag', 'Error', 'Fatal']
monster_image = ['spider.jpg', 'orc.jpg',
                 'necromant.png', 'goblin.jpg',
                 'dragon.jpg']
random_image = random.choice(monster_image)
flag_victory = 'victory-and-defeat-flag-for-game-set-flags-to-achieve-or-lose_172107-1800.jpg'
go_game = ['mir1.jpg', 'mir2.jpg', 'mir3.jpg', 'mir4.jpg', 'mir5.jpg']
bot.polling(non_stop=True)



  
