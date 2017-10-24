# -*- coding: utf-8 -*-

import telebot
import array
import time
from telebot import types

bot = telebot.TeleBot("475804097:AAHvaamrh3bpiA1ci0z2lBD1jN_y9OpvjFI")
# задаю векторы для накопления данных опроса
data1 = [0] * 8
data2 = [0] * 8
data3 = [0] * 8
data4 = [0] * 8
data5 = [0] * 8
data6 = [0] * 8
data7 = [0] * 8
j = 10

def q2(m):                                     # второй вопрос первого блока
   print('второй вопрос первого блока')
   keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
   keyboard.add(*[types.KeyboardButton(name) for name in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']])
   bot.send_message(m.chat.id,'баллы оставшиеся для ответа: '+str(j))
   msg = bot.send_message(m.chat.id,'Я могу успешно работать с самыми разными людьми.', reply_markup=keyboard)
   bot.register_next_step_handler(msg,name2)

def q3(m):                                     # третий вопрос первого блока
   print('третий вопрос первого блока')
   keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
   keyboard.add(*[types.KeyboardButton(name) for name in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']])
   bot.send_message(m.chat.id,'баллы оставшиеся для ответа: '+str(j))
   msg = bot.send_message(m.chat.id,'Генерация идей — моё врожденное достоинство.', reply_markup=keyboard)
   bot.register_next_step_handler(msg,name3)

def q4(m):                                     # четвертый вопрос первого блока
   print('четвертый вопрос первого блока')
   keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
   keyboard.add(*[types.KeyboardButton(name) for name in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']])
   bot.send_message(m.chat.id,'баллы оставшиеся для ответа: '+str(j))
   msg = bot.send_message(m.chat.id,'Моим достоинством является умение находить людей, способных принести пользу команде.', reply_markup=keyboard)
   bot.register_next_step_handler(msg,name4)

def q5(m):                                     # пятый вопрос первого блока
   print('пятый вопрос первого блока')
   keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
   keyboard.add(*[types.KeyboardButton(name) for name in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']])
   bot.send_message(m.chat.id,'баллы оставшиеся для ответа: '+str(j))
   msg = bot.send_message(m.chat.id,'Моя способность доводить всё до конца во многом обеспечила мою профессиональную эффективность.', reply_markup=keyboard)
   bot.register_next_step_handler(msg,name5)

def q6(m):                                     # шестой вопрос первого блока
   print('шестой вопрос первого блока')
   keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
   keyboard.add(*[types.KeyboardButton(name) for name in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']])
   bot.send_message(m.chat.id,'баллы оставшиеся для ответа: '+str(j))
   msg = bot.send_message(m.chat.id,'Я готов перенести временную непопулярность, если вижу, что мои действия принесут в конечном счете полезные результаты. ', reply_markup=keyboard)
   bot.register_next_step_handler(msg,name6)

def q7(m):                                     # седьмой вопрос первого блока
   print('седьмой вопрос первого блока')
   keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
   keyboard.add(*[types.KeyboardButton(name) for name in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']])
   bot.send_message(m.chat.id,'баллы оставшиеся для ответа: '+str(j))
   msg = bot.send_message(m.chat.id,'Я быстро выясняю, что сработает в данной ситуации, если в подобную ситуацию я уже попадал.', reply_markup=keyboard)
   bot.register_next_step_handler(msg,name7)

def q8(m):                                     # восьмой вопрос первого блока
   print('восьмой вопрос первого блока')
   keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
   keyboard.add(*[types.KeyboardButton(name) for name in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']])
   bot.send_message(m.chat.id,'баллы оставшиеся для ответа: '+str(j))
   msg = bot.send_message(m.chat.id,'Личные заблуждения и предубеждения не мешают мне находить и доказывать преимущества альтернативных действий.', reply_markup=keyboard)
   bot.register_next_step_handler(msg,name8)

#######################################################второй блок вопросов#####################################################################

def q2_1(m):                                     # первый вопрос второго блока
   global j
   print('первый вопрос второго блока')
   j = 10 # 10 баллов на следующий этап теста
   keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
   keyboard.add(*[types.KeyboardButton(name) for name in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']])
   bot.send_message(m.chat.id,'Часть 4 из 7. Особенности моего стиля работы в команде:\n 1) Я постоянно стараюсь лучше узнать своих коллег.\n 2) Я неохотно возражаю своим коллегам и не люблю сам быть в меньшинстве.\n 3) Я обычно нахожу вескую аргументацию против плохих предложений.\n 4) Я полагаю, что обладаю талантом быстро организовать исполнение одобренных планов.\n 5) Я обладаю способностью избегать очевидных решений и умею находить неожиданные.\n 6) Я стремлюсь добиться совершенства при исполнении любой роли в командной работе.\n 7) Я умею устанавливать контакты с внешним окружением команды.\n 8) Я способен воспринимать любые высказываемые мнения, но без колебаний подчиняюсь мнению большинства после принятия решения.\n ')
   msg = bot.send_message(m.chat.id,'Я чувствую себя неуверенно на совещании, если отсутствуют четкая повестка дня и контроль за её соблюдением.', reply_markup=keyboard)
   bot.register_next_step_handler(msg,name2_1)  ## нужно списать нужный номер функции

def q2_2(m):                                     # второй вопрос второго блока
   print('второй вопрос второго блока')
   keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
   keyboard.add(*[types.KeyboardButton(name) for name in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']])
   bot.send_message(m.chat.id,'баллы оставшиеся для ответа: '+str(j))
   msg = bot.send_message(m.chat.id,'Я склонен быть слишком великодушным к людям, имеющим правильную точку зрения, но не высказывающим её открыто.', reply_markup=keyboard)
   bot.register_next_step_handler(msg,name2_2)  ## нужно списать нужный номер функции

def q2_3(m):                                     # третий вопрос второго блока
   print('третий вопрос второго блока')
   keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
   keyboard.add(*[types.KeyboardButton(name) for name in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']])
   bot.send_message(m.chat.id,'баллы оставшиеся для ответа: '+str(j))
   msg = bot.send_message(m.chat.id,'Я склонен слишком много говорить, когда в группе обсуждаются новые идеи.', reply_markup=keyboard)
   bot.register_next_step_handler(msg,name2_3)  ## нужно списать нужный номер функции

def q2_4(m):                                     # четвертый вопрос второго блока
   print('четвертый вопрос второго блока')
   keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
   keyboard.add(*[types.KeyboardButton(name) for name in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']])
   bot.send_message(m.chat.id,'баллы оставшиеся для ответа: '+str(j))
   msg = bot.send_message(m.chat.id,'Вследствие моей осмотрительности я не склонен быстро и с энтузиазмом присоединяться к мнению коллег.', reply_markup=keyboard)
   bot.register_next_step_handler(msg,name2_4)  ## нужно списать нужный номер функции

def q2_5(m):                                     # пятый вопрос второго блока
   print('пятый вопрос второго блока')
   keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
   keyboard.add(*[types.KeyboardButton(name) for name in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']])
   bot.send_message(m.chat.id,'баллы оставшиеся для ответа: '+str(j))
   msg = bot.send_message(m.chat.id,'Я иногда выгляжу авторитарным и нетерпимым, когда чувствую необходимость достичь чего-то.', reply_markup=keyboard)
   bot.register_next_step_handler(msg,name2_5)  ## нужно списать нужный номер функции

def q2_6(m):                                     # шестой вопрос второго блока
   print('шестой вопрос второго блока')
   keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
   keyboard.add(*[types.KeyboardButton(name) for name in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']])
   bot.send_message(m.chat.id,'баллы оставшиеся для ответа: '+str(j))
   msg = bot.send_message(m.chat.id,'Мне трудно повести людей за собой, поскольку я слишком подвержен влиянию атмосферы, царящей в группе.', reply_markup=keyboard)
   bot.register_next_step_handler(msg,name2_6)  ## нужно списать нужный номер функции

def q2_7(m):                                     # седьмой вопрос второго блока
   print('седьмой вопрос второго блока')
   keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
   keyboard.add(*[types.KeyboardButton(name) for name in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']])
   bot.send_message(m.chat.id,'баллы оставшиеся для ответа: '+str(j))
   msg = bot.send_message(m.chat.id,'Я слишком захвачен идеями, которые мне приходят в голову, и поэтому плохо слежу за тем, что происходит вокруг.', reply_markup=keyboard)
   bot.register_next_step_handler(msg,name2_7)  ## нужно списать нужный номер функции

def q2_8(m):                                     # восьмой вопрос второго блока
   print('восьмой вопрос второго блока')
   keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
   keyboard.add(*[types.KeyboardButton(name) for name in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']])
   bot.send_message(m.chat.id,'баллы оставшиеся для ответа: '+str(j))
   msg = bot.send_message(m.chat.id,'Мои коллеги находят, что я слишком много внимания уделяю деталям и чрезмерно беспокоюсь о том, что дела идут неправильно.', reply_markup=keyboard)
   bot.register_next_step_handler(msg,name2_8)  ## нужно списать нужный номер функции

#######################################################конец второго блока#####################################################################



#######################################################третий блок вопросов#####################################################################

def q3_1(m):                                     # первый вопрос третьего блока
   global j
   print('первый вопрос третьего блока')
   j = 10 # 10 баллов на следующий этап теста
   keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
   keyboard.add(*[types.KeyboardButton(name) for name in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']])
   bot.send_message(m.chat.id,'Часть 3 из 7. Участие в совместном проекте:\n 1) Я умею влиять на людей, не оказывая на них давления.\n 2) Врожденная осмотрительность предохраняет меня от ошибок, возникающих из-за невнимательности.\n 3) Я готов оказать давление, чтобы совещание не превращалось в пустую трату времени и не терялась из виду основная цель обсуждения.\n 4) Можно рассчитывать на поступление от меня оригинальных предложений.\n 5) Я всегда готов поддержать любое предложение, если оно служит общим интересам.\n 6) Я энергично ищу среди новых идей и разработок свежайшие.\n 7) Я надеюсь, что моя способность выносить беспристрастные суждения признаётся всеми, кто меня знает.\n 8) На меня можно возложить обязанности следить за тем, чтобы наиболее существенная работа была организована должным образом.\n ')
   msg = bot.send_message(m.chat.id,'Я умею влиять на людей, не оказывая на них давления.', reply_markup=keyboard)
   bot.register_next_step_handler(msg,name3_1)  ## нужно списать нужный номер функции

def q3_2(m):                                     # второй вопрос третьего блока
   print('второй вопрос третьего блока')
   keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
   keyboard.add(*[types.KeyboardButton(name) for name in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']])
   bot.send_message(m.chat.id,'баллы оставшиеся для ответа: '+str(j))
   msg = bot.send_message(m.chat.id,'Врожденная осмотрительность предохраняет меня от ошибок, возникающих из-за невнимательности.', reply_markup=keyboard)
   bot.register_next_step_handler(msg,name3_2)  ## нужно списать нужный номер функции

def q3_3(m):                                     # третий вопрос третьего блока
   print('третий вопрос третьего блока')
   keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
   keyboard.add(*[types.KeyboardButton(name) for name in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']])
   bot.send_message(m.chat.id,'баллы оставшиеся для ответа: '+str(j))
   msg = bot.send_message(m.chat.id,'Я готов оказать давление, чтобы совещание не превращалось в пустую трату времени и не терялась из виду основная цель обсуждения.', reply_markup=keyboard)
   bot.register_next_step_handler(msg,name3_3)  ## нужно списать нужный номер функции

def q3_4(m):                                     # четвертый вопрос третьего блока
   print('четвертый вопрос третьего блока')
   keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
   keyboard.add(*[types.KeyboardButton(name) for name in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']])
   bot.send_message(m.chat.id,'баллы оставшиеся для ответа: '+str(j))
   msg = bot.send_message(m.chat.id,'Можно рассчитывать на поступление от меня оригинальных предложений.', reply_markup=keyboard)
   bot.register_next_step_handler(msg,name3_4)  ## нужно списать нужный номер функции

def q3_5(m):                                     # пятый вопрос третьего блока
   print('пятый вопрос третьего блока')
   keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
   keyboard.add(*[types.KeyboardButton(name) for name in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']])
   bot.send_message(m.chat.id,'баллы оставшиеся для ответа: '+str(j))
   msg = bot.send_message(m.chat.id,'Я всегда готов поддержать любое предложение, если оно служит общим интересам.', reply_markup=keyboard)
   bot.register_next_step_handler(msg,name3_5)  ## нужно списать нужный номер функции

def q3_6(m):                                     # шестой вопрос третьего блока
   print('шестой вопрос третьего блока')
   keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
   keyboard.add(*[types.KeyboardButton(name) for name in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']])
   bot.send_message(m.chat.id,'баллы оставшиеся для ответа: '+str(j))
   msg = bot.send_message(m.chat.id,'Я энергично ищу среди новых идей и разработок свежайшие.', reply_markup=keyboard)
   bot.register_next_step_handler(msg,name3_6)  ## нужно списать нужный номер функции

def q3_7(m):                                     # седьмой вопрос третьего блока
   print('седьмой вопрос третьего блока')
   keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
   keyboard.add(*[types.KeyboardButton(name) for name in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']])
   bot.send_message(m.chat.id,'баллы оставшиеся для ответа: '+str(j))
   msg = bot.send_message(m.chat.id,'Я надеюсь, что моя способность выносить беспристрастные суждения признаётся всеми, кто меня знает.', reply_markup=keyboard)
   bot.register_next_step_handler(msg,name3_7)  ## нужно списать нужный номер функции

def q3_8(m):                                     # восьмой вопрос третьего блока
   print('восьмой вопрос третьего блока')
   keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
   keyboard.add(*[types.KeyboardButton(name) for name in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']])
   bot.send_message(m.chat.id,'баллы оставшиеся для ответа: '+str(j))
   msg = bot.send_message(m.chat.id,'На меня можно возложить обязанности следить за тем, чтобы наиболее существенная работа была организована должным образом.', reply_markup=keyboard)
   bot.register_next_step_handler(msg,name3_8)  ## нужно списать нужный номер функции

#######################################################конец третьего блока#####################################################################



#######################################################четвертый блок вопросов#####################################################################

def q4_1(m):                                     # первый вопрос четвертого блока
   global j
   print('первый вопрос четвертого блока')
   j = 10 # 10 баллов на следующий этап теста
   keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
   keyboard.add(*[types.KeyboardButton(name) for name in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']])
   bot.send_message(m.chat.id,'Часть 4 из 7. Особенности моего стиля работы в команде:\n 1) Я постоянно стараюсь лучше узнать своих коллег.\n 2) Я неохотно возражаю своим коллегам и не люблю сам быть в меньшинстве.\n 3) Я обычно нахожу вескую аргументацию против плохих предложений.\n 4) Я полагаю, что обладаю талантом быстро организовать исполнение одобренных планов.\n 5) Я обладаю способностью избегать очевидных решений и умею находить неожиданные.\n 6) Я стремлюсь добиться совершенства при исполнении любой роли в командной работе.\n 7) Я умею устанавливать контакты с внешним окружением команды.\n 8) Я способен воспринимать любые высказываемые мнения, но без колебаний подчиняюсь мнению большинства после принятия решения.\n ')
   msg = bot.send_message(m.chat.id,'Я постоянно стараюсь лучше узнать своих коллег.', reply_markup=keyboard)
   bot.register_next_step_handler(msg,name4_1)  ## нужно списать нужный номер функции

def q4_2(m):                                     # второй вопрос четвертого блока
   print('второй вопрос четвертого блока')
   keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
   keyboard.add(*[types.KeyboardButton(name) for name in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']])
   bot.send_message(m.chat.id,'баллы оставшиеся для ответа: '+str(j))
   msg = bot.send_message(m.chat.id,'Я неохотно возражаю своим коллегам и не люблю сам быть в меньшинстве.', reply_markup=keyboard)
   bot.register_next_step_handler(msg,name4_2)  ## нужно списать нужный номер функции

def q4_3(m):                                     # третий вопрос четвертого блока
   print('третий вопрос четвертого блока')
   keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
   keyboard.add(*[types.KeyboardButton(name) for name in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']])
   bot.send_message(m.chat.id,'баллы оставшиеся для ответа: '+str(j))
   msg = bot.send_message(m.chat.id,'Я обычно нахожу вескую аргументацию против плохих предложений.', reply_markup=keyboard)
   bot.register_next_step_handler(msg,name4_3)  ## нужно списать нужный номер функции

def q4_4(m):                                     # четвертый вопрос четвертого блока
   print('четвертый вопрос четвертого блока')
   keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
   keyboard.add(*[types.KeyboardButton(name) for name in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']])
   bot.send_message(m.chat.id,'баллы оставшиеся для ответа: '+str(j))
   msg = bot.send_message(m.chat.id,'Я полагаю, что обладаю талантом быстро организовать исполнение одобренных планов.', reply_markup=keyboard)
   bot.register_next_step_handler(msg,name4_4)  ## нужно списать нужный номер функции

def q4_5(m):                                     # пятый вопрос четвертого блока
   print('пятый вопрос четвертого блока')
   keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
   keyboard.add(*[types.KeyboardButton(name) for name in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']])
   bot.send_message(m.chat.id,'баллы оставшиеся для ответа: '+str(j))
   msg = bot.send_message(m.chat.id,'Я обладаю способностью избегать очевидных решений и умею находить неожиданные.', reply_markup=keyboard)
   bot.register_next_step_handler(msg,name4_5)  ## нужно списать нужный номер функции

def q4_6(m):                                     # шестой вопрос четвертого блока
   print('шестой вопрос четвертого блока')
   keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
   keyboard.add(*[types.KeyboardButton(name) for name in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']])
   bot.send_message(m.chat.id,'баллы оставшиеся для ответа: '+str(j))
   msg = bot.send_message(m.chat.id,'Я стремлюсь добиться совершенства при исполнении любой роли в командной работе.', reply_markup=keyboard)
   bot.register_next_step_handler(msg,name4_6)  ## нужно списать нужный номер функции

def q4_7(m):                                     # седьмой вопрос четвертого блока
   print('седьмой вопрос четвертого блока')
   keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
   keyboard.add(*[types.KeyboardButton(name) for name in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']])
   bot.send_message(m.chat.id,'баллы оставшиеся для ответа: '+str(j))
   msg = bot.send_message(m.chat.id,'Я умею устанавливать контакты с внешним окружением команды.', reply_markup=keyboard)
   bot.register_next_step_handler(msg,name4_7)  ## нужно списать нужный номер функции

def q4_8(m):                                     # восьмой вопрос четвертого блока
   print('восьмой вопрос четвертого блока')
   keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
   keyboard.add(*[types.KeyboardButton(name) for name in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']])
   bot.send_message(m.chat.id,'баллы оставшиеся для ответа: '+str(j))
   msg = bot.send_message(m.chat.id,'Я способен воспринимать любые высказываемые мнения, но без колебаний подчиняюсь мнению большинства после принятия решения.', reply_markup=keyboard)
   bot.register_next_step_handler(msg,name4_8)  ## нужно списать нужный номер функции

#######################################################конец четвертого блока#####################################################################


#######################################################пятый блок вопросов#####################################################################

def q5_1(m):                                     # первый вопрос пятого блока
   global j
   print('первый вопрос пятого блока')
   j = 10 # 10 баллов на следующий этап теста
   keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
   keyboard.add(*[types.KeyboardButton(name) for name in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']])
   bot.send_message(m.chat.id,'Часть 5 из 7. Я получаю удовлетворение от работы, потому что:\n 1) Мне доставляет удовольствие анализ ситуаций и взвешивание всех шансов.\n 2) Мне нравится находить практические решения проблем.\n 3) Мне нравиться сознавать, что я создаю хорошие рабочие взаимоотношения.\n 4) Я способен оказывать сильное влияние на принятие решений.\n 5) Я получаю возможность встретиться с людьми, способными предложить что-то новое для меня.\n 6) Я способен добиться согласия людей на реализацию необходимого курса действий.\n 7) Я чувствую себя в своей стихии, когда могу уделить задаче все мое внимание.\n 8) Мне нравится находить задачи, требующие напряжения воображения.\n')
   msg = bot.send_message(m.chat.id,'Мне доставляет удовольствие анализ ситуаций и взвешивание всех шансов.', reply_markup=keyboard)
   bot.register_next_step_handler(msg,name5_1)  ## нужно списать нужный номер функции

def q5_2(m):                                     # второй вопрос пятого блока
   print('второй вопрос пятого блока')
   keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
   keyboard.add(*[types.KeyboardButton(name) for name in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']])
   bot.send_message(m.chat.id,'баллы оставшиеся для ответа: '+str(j))
   msg = bot.send_message(m.chat.id,'Мне нравится находить практические решения проблем.', reply_markup=keyboard)
   bot.register_next_step_handler(msg,name5_2)  ## нужно списать нужный номер функции

def q5_3(m):                                     # третий вопрос пятого блока
   print('третий вопрос пятого блока')
   keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
   keyboard.add(*[types.KeyboardButton(name) for name in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']])
   bot.send_message(m.chat.id,'баллы оставшиеся для ответа: '+str(j))
   msg = bot.send_message(m.chat.id,'Мне нравиться сознавать, что я создаю хорошие рабочие взаимоотношения.', reply_markup=keyboard)
   bot.register_next_step_handler(msg,name5_3)  ## нужно списать нужный номер функции

def q5_4(m):                                     # четвертый вопрос пятого блока
   print('четвертый вопрос пятого блока')
   keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
   keyboard.add(*[types.KeyboardButton(name) for name in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']])
   bot.send_message(m.chat.id,'баллы оставшиеся для ответа: '+str(j))
   msg = bot.send_message(m.chat.id,'Я способен оказывать сильное влияние на принятие решений.', reply_markup=keyboard)
   bot.register_next_step_handler(msg,name5_4)  ## нужно списать нужный номер функции

def q5_5(m):                                     # пятый вопрос пятого блока
   print('пятый вопрос пятого блока')
   keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
   keyboard.add(*[types.KeyboardButton(name) for name in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']])
   bot.send_message(m.chat.id,'баллы оставшиеся для ответа: '+str(j))
   msg = bot.send_message(m.chat.id,'Я получаю возможность встретиться с людьми, способными предложить что-то новое для меня.', reply_markup=keyboard)
   bot.register_next_step_handler(msg,name5_5)  ## нужно списать нужный номер функции

def q5_6(m):                                     # шестой вопрос пятого блока
   print('шестой вопрос пятого блока')
   keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
   keyboard.add(*[types.KeyboardButton(name) for name in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']])
   bot.send_message(m.chat.id,'баллы оставшиеся для ответа: '+str(j))
   msg = bot.send_message(m.chat.id,'Я способен добиться согласия людей на реализацию необходимого курса действий.', reply_markup=keyboard)
   bot.register_next_step_handler(msg,name5_6)  ## нужно списать нужный номер функции

def q5_7(m):                                     # седьмой вопрос пятого блока
   print('седьмой вопрос пятого блока')
   keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
   keyboard.add(*[types.KeyboardButton(name) for name in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']])
   bot.send_message(m.chat.id,'баллы оставшиеся для ответа: '+str(j))
   msg = bot.send_message(m.chat.id,'Я чувствую себя в своей стихии, когда могу уделить задаче все мое внимание.', reply_markup=keyboard)
   bot.register_next_step_handler(msg,name5_7)  ## нужно списать нужный номер функции

def q5_8(m):                                     # восьмой вопрос пятого блока
   print('восьмой вопрос пятого блока')
   keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
   keyboard.add(*[types.KeyboardButton(name) for name in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']])
   bot.send_message(m.chat.id,'баллы оставшиеся для ответа: '+str(j))
   msg = bot.send_message(m.chat.id,'Мне нравится находить задачи, требующие напряжения воображения.', reply_markup=keyboard)
   bot.register_next_step_handler(msg,name5_8)  ## нужно списать нужный номер функции

#######################################################конец пятого блока#####################################################################



#######################################################шестой блок вопросов#####################################################################

def q6_1(m):                                     # первый вопрос шестого блока
   global j
   print('первый вопрос шестого блока')
   j = 10 # 10 баллов на следующий этап теста
   keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
   keyboard.add(*[types.KeyboardButton(name) for name in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']])
   bot.send_message(m.chat.id,'Часть 6 из 7. Если мне неожиданно предложат решить трудную задачу за ограниченное время с незнакомыми людьми, то:\n 1) Я бы почувствовал необходимость сначала в одиночестве обдумать пути выхода из тупика, прежде чем начать действовать.\n 2) Я был бы готов работать с человеком, указавшим наиболее позитивный подход, каковы бы ни были связанные с этим трудности.\n 3) Я бы попытался найти способ разбиения задачи на части в соответствии с тем, что лучше всего умеют делать отдельные члены команды.\n 4) Присущая мне обязательность помогла бы нам не отстать от графика.\n 5) Я надеюсь, мне бы удалось сохранить хладнокровие и способность логически мыслить.\n 6) Я бы упорно добивался достижения цели, несмотря ни на какие помехи.\n 7) Я был бы готов действовать силой положительного примера при появлении признаков отсутствия прогресса в командной работе.\n 8) Я бы организовал дискуссию, чтобы стимулировать выдвижение новых идей и придать начальный импульс командной работе.\n ')
   msg = bot.send_message(m.chat.id,'Я бы почувствовал необходимость сначала в одиночестве обдумать пути выхода из тупика, прежде чем начать действовать.', reply_markup=keyboard)
   bot.register_next_step_handler(msg,name6_1)  ## нужно списать нужный номер функции

def q6_2(m):                                     # второй вопрос шестого блока
   print('второй вопрос шестого блока')
   keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
   keyboard.add(*[types.KeyboardButton(name) for name in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']])
   bot.send_message(m.chat.id,'баллы оставшиеся для ответа: '+str(j))
   msg = bot.send_message(m.chat.id,'Я был бы готов работать с человеком, указавшим наиболее позитивный подход, каковы бы ни были связанные с этим трудности.', reply_markup=keyboard)
   bot.register_next_step_handler(msg,name6_2)  ## нужно списать нужный номер функции

def q6_3(m):                                     # третий вопрос шестого блока
   print('третий вопрос шестого блока')
   keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
   keyboard.add(*[types.KeyboardButton(name) for name in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']])
   bot.send_message(m.chat.id,'баллы оставшиеся для ответа: '+str(j))
   msg = bot.send_message(m.chat.id,'Я бы попытался найти способ разбиения задачи на части в соответствии с тем, что лучше всего умеют делать отдельные члены команды.', reply_markup=keyboard)
   bot.register_next_step_handler(msg,name6_3)  ## нужно списать нужный номер функции

def q6_4(m):                                     # четвертый вопрос шестого блока
   print('четвертый вопрос шестого блока')
   keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
   keyboard.add(*[types.KeyboardButton(name) for name in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']])
   bot.send_message(m.chat.id,'баллы оставшиеся для ответа: '+str(j))
   msg = bot.send_message(m.chat.id,'Присущая мне обязательность помогла бы нам не отстать от графика.', reply_markup=keyboard)
   bot.register_next_step_handler(msg,name6_4)  ## нужно списать нужный номер функции

def q6_5(m):                                     # пятый вопрос шестого блока
   print('пятый вопрос шестого блока')
   keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
   keyboard.add(*[types.KeyboardButton(name) for name in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']])
   bot.send_message(m.chat.id,'баллы оставшиеся для ответа: '+str(j))
   msg = bot.send_message(m.chat.id,'Я надеюсь, мне бы удалось сохранить хладнокровие и способность логически мыслить.', reply_markup=keyboard)
   bot.register_next_step_handler(msg,name6_5)  ## нужно списать нужный номер функции

def q6_6(m):                                     # шестой вопрос шестого блока
   print('шестой вопрос шестого блока')
   keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
   keyboard.add(*[types.KeyboardButton(name) for name in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']])
   bot.send_message(m.chat.id,'баллы оставшиеся для ответа: '+str(j))
   msg = bot.send_message(m.chat.id,'Я бы упорно добивался достижения цели, несмотря ни на какие помехи.', reply_markup=keyboard)
   bot.register_next_step_handler(msg,name6_6)  ## нужно списать нужный номер функции

def q6_7(m):                                     # седьмой вопрос шестого блока
   print('седьмой вопрос шестого блока')
   keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
   keyboard.add(*[types.KeyboardButton(name) for name in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']])
   bot.send_message(m.chat.id,'баллы оставшиеся для ответа: '+str(j))
   msg = bot.send_message(m.chat.id,'Я был бы готов действовать силой положительного примера при появлении признаков отсутствия прогресса в командной работе.', reply_markup=keyboard)
   bot.register_next_step_handler(msg,name6_7)  ## нужно списать нужный номер функции

def q6_8(m):                                     # восьмой вопрос шестого блока
   print('восьмой вопрос шестого блока')
   keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
   keyboard.add(*[types.KeyboardButton(name) for name in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']])
   bot.send_message(m.chat.id,'баллы оставшиеся для ответа: '+str(j))
   msg = bot.send_message(m.chat.id,'Я бы организовал дискуссию, чтобы стимулировать выдвижение новых идей и придать начальный импульс командной работе.', reply_markup=keyboard)
   bot.register_next_step_handler(msg,name6_8)  ## нужно списать нужный номер функции

#######################################################конец шестого блока#####################################################################


#######################################################седьмой блок вопросов#####################################################################

def q7_1(m):                                     # первый вопрос седьмого блока
   global j
   print('первый вопрос седьмого блока')
   j = 10 # 10 баллов на следующий этап теста
   keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
   keyboard.add(*[types.KeyboardButton(name) for name in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']])
   bot.send_message(m.chat.id,'Часть 7 заключительная. Проблемы, с которыми я сталкиваюсь, работая в команде:\n 1) Я склонен проявлять нетерпимость по отношению к людям, мешающим, по моему мнению, прогрессу в делах группы.\n 2) Окружающие иногда критикуют меня за чрезмерный рационализм и неспособность к интуитивным решениям.\n 3) Мое стремление обеспечить условия, чтобы работа выполнялась правильно, может приводить к снижению темпов.\n 4) Я слишком быстро утрачиваю энтузиазм и стараюсь почерпнуть его у наиболее активных членов группы.\n 5) Я тяжел на подъем, если не имею ясных целей.\n 6) Мне иногда бывает очень трудно разобраться во встретившихся мне сложностях.\n 7) Я стесняюсь обратиться за помощью к другим, когда не могу что-либо сделать сам.\n 8) Я испытываю затруднения при обосновании своей точки зрения, когда сталкиваюсь с серьезными возражениями.\n')
   msg = bot.send_message(m.chat.id,'Я склонен проявлять нетерпимость по отношению к людям, мешающим, по моему мнению, прогрессу в делах группы.', reply_markup=keyboard)
   bot.register_next_step_handler(msg,name7_1)  ## нужно списать нужный номер функции

def q7_2(m):                                     # второй вопрос седьмого блока
   print('второй вопрос седьмого блока')
   keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
   keyboard.add(*[types.KeyboardButton(name) for name in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']])
   bot.send_message(m.chat.id,'баллы оставшиеся для ответа: '+str(j))
   msg = bot.send_message(m.chat.id,'Окружающие иногда критикуют меня за чрезмерный рационализм и неспособность к интуитивным решениям.', reply_markup=keyboard)
   bot.register_next_step_handler(msg,name7_2)  ## нужно списать нужный номер функции

def q7_3(m):                                     # третий вопрос седьмого блока
   print('третий вопрос седьмого блока')
   keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
   keyboard.add(*[types.KeyboardButton(name) for name in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']])
   bot.send_message(m.chat.id,'баллы оставшиеся для ответа: '+str(j))
   msg = bot.send_message(m.chat.id,'Мое стремление обеспечить условия, чтобы работа выполнялась правильно, может приводить к снижению темпов.', reply_markup=keyboard)
   bot.register_next_step_handler(msg,name7_3)  ## нужно списать нужный номер функции

def q7_4(m):                                     # четвертый вопрос седьмого блока
   print('четвертый вопрос седьмого блока')
   keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
   keyboard.add(*[types.KeyboardButton(name) for name in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']])
   bot.send_message(m.chat.id,'баллы оставшиеся для ответа: '+str(j))
   msg = bot.send_message(m.chat.id,'Я слишком быстро утрачиваю энтузиазм и стараюсь почерпнуть его у наиболее активных членов группы.', reply_markup=keyboard)
   bot.register_next_step_handler(msg,name7_4)  ## нужно списать нужный номер функции

def q7_5(m):                                     # пятый вопрос седьмого блока
   print('пятый вопрос седьмого блока')
   keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
   keyboard.add(*[types.KeyboardButton(name) for name in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']])
   bot.send_message(m.chat.id,'баллы оставшиеся для ответа: '+str(j))
   msg = bot.send_message(m.chat.id,'Я тяжел на подъем, если не имею ясных целей.', reply_markup=keyboard)
   bot.register_next_step_handler(msg,name7_5)  ## нужно списать нужный номер функции

def q7_6(m):                                     # шестой вопрос седьмого блока
   print('шестой вопрос седьмого блока')
   keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
   keyboard.add(*[types.KeyboardButton(name) for name in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']])
   bot.send_message(m.chat.id,'баллы оставшиеся для ответа: '+str(j))
   msg = bot.send_message(m.chat.id,'Мне иногда бывает очень трудно разобраться во встретившихся мне сложностях.', reply_markup=keyboard)
   bot.register_next_step_handler(msg,name7_6)  ## нужно списать нужный номер функции

def q7_7(m):                                     # седьмой вопрос седьмого блока
   print('седьмой вопрос седьмого блока')
   keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
   keyboard.add(*[types.KeyboardButton(name) for name in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']])
   bot.send_message(m.chat.id,'баллы оставшиеся для ответа: '+str(j))
   msg = bot.send_message(m.chat.id,'Я стесняюсь обратиться за помощью к другим, когда не могу что-либо сделать сам.', reply_markup=keyboard)
   bot.register_next_step_handler(msg,name7_7)  ## нужно списать нужный номер функции

def q7_8(m):                                     # восьмой вопрос седьмого блока
   print('восьмой вопрос седьмого блока')
   keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
   keyboard.add(*[types.KeyboardButton(name) for name in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']])
   bot.send_message(m.chat.id,'баллы оставшиеся для ответа: '+str(j))
   msg = bot.send_message(m.chat.id,'Я испытываю затруднения при обосновании своей точки зрения, когда сталкиваюсь с серьезными возражениями.', reply_markup=keyboard)
   bot.register_next_step_handler(msg,name7_8)  ## нужно списать нужный номер функции

#######################################################конец седьмого блока#####################################################################


@bot.message_handler(commands=['start'])
def start(m):
   msg = bot.send_message(m.chat.id,'Привет, я бот который проводит тест Белбина, вам будет нужно ответить на ряд вопросов а потом я рассчитаю для вас результат, для начала тестирования введите команду /yes для выхода введите команду /no')

@bot.message_handler(commands=['yes'])
def yes(m):                                    #ввод имени
   print('функция ввода имени')
   msg = bot.send_message(m.chat.id,'Напишите своё имя')
   bot.register_next_step_handler(msg,name_init)

def input(m):  
   global j  
   j = 10                                #начало теста
   print('первый вопрос первого блока')
   keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
   keyboard.add(*[types.KeyboardButton(name) for name in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']])
   bot.send_message(m.chat.id,'Часть 1 из 7. Какой вклад я могу внести в работу команды? \n 1) Я думаю, что способен быстро замечать новые возможности и извлекать из них выгоды. \n 2) Я могу успешно работать с самыми разными людьми. \n 3) Генерация идей — моё врожденное достоинство.\n 4) Моим достоинством является умение находить людей, способных принести пользу команде.\n 5) Моя способность доводить всё до конца во многом обеспечила мою профессиональную эффективность.\n 6) Я готов перенести временную непопулярность, если вижу, что мои действия принесут в конечном счете полезные результаты.\n 7) Я быстро выясняю, что сработает в данной ситуации, если в подобную ситуацию я уже попадал.\n 8) Личные заблуждения и предубеждения не мешают мне находить и доказывать преимущества альтернативных действий.')
   msg = bot.send_message(m.chat.id,'Я думаю, что способен быстро замечать новые возможности и извлекать из них выгоды. ', reply_markup=keyboard)
   bot.register_next_step_handler(msg,name)

@bot.message_handler(commands=['no'])
def no(m):                                     #выход из теста
   print('выход из теста')
   bot.send_message(m.chat.id,'Ну тогда пока))')

####################################################запись имени#########################################################################################
def name_init(m):
     global neme_data
     neme_data = m.text
     print(neme_data)
     input(m)

####################################################обработка результата#################################################################################
def out(m):
     data_out = [0] * 8
     global j
     j = 10
     print('name_data')
     # логирование в файлик.
     my_file = open("log.txt", 'a')
     my_file.write(m.chat.id)
     my_file.write(neme_data)
     print(neme_data)
     bot.send_message(m.chat.id,'Отчет о тестировании')
     bot.send_message(m.chat.id,'Имя жертвы: '+str(neme_data))
     for k in range(0,7): # собираю данные по всему тесту
       data_out[k] = data1[k]+data2[k]+data3[k]+data4[k]+data5[k]+data6[k]+data7[k]
     # определю максимальный элемент
     data_max = max(data_out)
     for k in range(0,8): # собираю данные по всему тесту
       if data_out[k] == data_max:
           test_exit = k
     if test_exit == 0:
         bot.send_message(m.chat.id,'Исполнитель (И) \n Это  член  команды,  выражающий  ее  сущность,  потому  что  цели  Исполнителя  идентичны целям  команды.  Часто  Исполнитель  является именно тем руководите лем, выполняющим задания, которые другие не всегда хотят выполнять. Исполнитель систематически составляет планы и эффективно претворяет их в производство. Стиль Исполнителя в команде - организация работ. Он может иметь недостаток гибкости и не любит непроверенные идеи.')
         my_file.write('Исполнитель')
     if test_exit == 1:
         bot.send_message(m.chat.id,'Председатель (или Координатор) (П) \n Этот  тип  руководителя  организует  работу  команды  и  использование  ресурсов  в соответствии с групповыми целями. Председатель имеет ясное представление о сильных и слабых сторонах команды и работает с максимальным использованием потенциала каждого члена команды. Председатель может не обладать блестящим интеллектом, но он хорошо руководит  людьми.  Главная  личная  черта  характера  Председателя - это  сильное доминирование  и  преданность  групповым  целям.  Председатель  является  спокойным, несуетливым,   само дисциплинированным,   поощряющим   и   поддерживающим   типом руководителя команды. Стиль руководства командой Председателя - принимать вносимые вклады в деятельность команды и оценивать их в соответствии с целями команды. ')
         my_file.write('Председатель')
     if test_exit == 2:
         bot.send_message(m.chat.id,'Формирователь (Ф) \n Это   другой,   более   умело   управляющий,   честолюбивый,   оппортунистический, предпринимательский  тип  руководителя  команды.  Он  формирует  усилия  команды  через установление  целей  и  приоритетов.  Формирователь  присоединяется  к  точке  зрения,  что победителей  не  судят. Стиль  руководства  Формирователя -оспаривать,  мотивировать, достигать. Он склонен к провокациям, раздражению и нетерпению')
         my_file.write('Формирователь')
     if test_exit == 3:
         bot.send_message(m.chat.id,'Мыслитель (Генератор идей) (М) \n Это  интровертный  (сосредоточенный  на  своем  внутреннем  мире),  умный,  склонный  к нововведениям  член  команды.  Мыслитель  представляет н овые  идеи,  пытается  их развивать,  разрабатывает  стратегию.  Он  интересуется,  в  основном,  более  широкими вопросами, которые могут дать результат, при недостаточном внимании к деталям. Стиль Мыслителя - привносить  инновационные  идеи  в  работу  команды  и  ее  цели.  Он  склонен витать в облаках и игнорировать детали или протокол')
         my_file.write('Мыслитель')
     if test_exit == 4:
         bot.send_message(m.chat.id,'Разведчик (Исследователь ресурсов) (Р) \n Это  экстравертивный  (ориентированный  на  внешний  мир),  собирающий  ресурсы  тип генератора  идей.  Разведчик  исследует  и  докладывает  об  идеях,  ресурсах и  новых усовершенствованиях,  которые  имеются  вне  команды.  Он  естествен  в  общественных отношениях  и  создает  полезные  внешние  контакты  для  команды.  Он  обычно  знает,  как примирить  интересы  людей  с  общественными  интересами.  Разведчик  обычно  знает,  кто может помочь решить проблемы. Стиль Исследователя ресурсов - создать сеть и собирать полезные  ресурсы  для  команды.  Разведчики  могут  терять  интерес,  стоит  только  пройти первоначальному увлечению.')
         my_file.write('Разведчик')
     if test_exit == 5:
         bot.send_message(m.chat.id,'Оценщик (О) Оценщик  объективен  при  анализировании  проблем  и  оценке  идей.  Редко  охваченный энтузиазмом, он защищает команду от принятия импульсивных, отчаянных решений. Стиль построения команды Оценщика-объективно анализировать и оценивать идеи и решения команды. Им может не хватать вдохновения или способности мотивировать других.')
         my_file.write('Оценщик')
     if test_exit == 6:
         bot.send_message(m.chat.id,'Коллективист (К) Коллективист играет ориентированную на отношения, поддерживающую роль. Этот чрезвычайно популярный тип нередок среди высших менеджеров. Коллективист благоприятно  действует  на  дух  команды,  улучшает  межличностное  общение,  сводит  к минимуму конфликты в команде. Стиль построения команды Коллективиста-поддерживать отношения внутри команды. Он может быть нерешителен в момент кризиса.')
         my_file.write('Коллективист')
     if test_exit == 7:
         bot.send_message(m.chat.id,'Доводчик (Завершающий работу) (Д) Доводчик  продвигается  вперед  и  настаивает  на  данном  плане,  проекте  или  предложении,  когда возбуждение  и  энтузиазм  других  членов  команды  исчерпаны.  Доводчик хорошо  планирует, выполняет и доводит до конца задачи команды. Он раздражается, если работа команды отстает от графика, и теряет удовлетворение от работы, когда работа не завершена. Стиль построения команды Доводчика-настаивать ради продвижения вперед, выдерживать сроки.')
         my_file.write('Доводчик')
     my_file.close()


#######################################################обработчики для первого блока#####################################################################

def name(m):
     global j
     global data1
     print(m.text)
     print(j)
     print(neme_data)
     try:
       data1[0] = int(m.text)
       j = j-int(m.text)
       if j<0:
           bot.send_message(m.chat.id,'Сумма баллов превышает 10, возврат к первому вопросу')
           input(m)
       else:
           if j==0:
              q2_1(m)
           else:
              q2(m)
     except ValueError:
       input(m)

def name2(m):
     global j
     global data1
     print(m.text)
     print(neme_data)
     print(j)
     try:
       data1[1] = int(m.text)
       j = j-int(m.text)
       if j<0:
           bot.send_message(m.chat.id,'Сумма баллов превышает 10, возврат к первому вопросу')
           input(m)
       else:
           if j==0:
              q2_1(m)
           else:
              q3(m)
     except ValueError:
       q2(m)

def name3(m):
     global j
     global data1
     print(neme_data)
     print(m.text)
     print(j)
     try:
       data1[2] = int(m.text)
       j = j-int(m.text)
       if j<0:
           bot.send_message(m.chat.id,'Сумма баллов превышает 10, возврат к первому вопросу')
           input(m)
       else:
           if j==0:
              q2_1(m)
           else:
              q4(m)
     except ValueError:
       q3(m)

def name4(m):
     global j
     global data1
     print(m.text)
     print(j)
     try:
       data1[3] = int(m.text)
       j = j-int(m.text)
       if j<0:
           bot.send_message(m.chat.id,'Сумма баллов превышает 10, возврат к первому вопросу')
           input(m)
       else:
           if j==0:
              q2_1(m)
           else:
              q5(m)
     except ValueError:
       q4(m)

def name5(m):
     global j
     global data1
     print(m.text)
     print(j)
     try:
       data1[4] = int(m.text)
       j = j-int(m.text)
       if j<0:
           bot.send_message(m.chat.id,'Сумма баллов превышает 10, возврат к первому вопросу')
           input(m)
       else:
           if j==0:
              q2_1(m)
           else:
              q6(m)
     except ValueError:
       q5(m)

def name6(m):
     global j
     global data1
     print(m.text)
     print(j)
     try:
       data1[5] = int(m.text)
       j = j-int(m.text)
       if j<0:
           bot.send_message(m.chat.id,'Сумма баллов превышает 10, возврат к первому вопросу')
           input(m)
       else:
           if j==0:
              q2_1(m)
           else:
              q7(m)
     except ValueError:
       q6(m)

def name7(m):
     global j
     global data1
     print(m.text)
     print(j)
     try:
       data1[6] = int(m.text)
       j = j-int(m.text)
       if j<0:
           bot.send_message(m.chat.id,'Сумма баллов превышает 10, возврат к первому вопросу')
           input(m)
       else:
           if j==0:
              q2_1(m)
           else:
              q8(m)
     except ValueError:
       q7(m)

def name8(m):
     global j
     global data1
     print(m.text)
     print(j)
     try:
       data1[7] = int(m.text)
       j = j-int(m.text)
       if j != 0:
          bot.send_message(m.chat.id,'Сумма баллов превышает 10, возврат к первому вопросу')
          input(m)
       else:
          q2_1(m)
     except ValueError:
       q8(m)
#########################################################################################################################################################


#######################################################обработчики для второго блока#####################################################################
def name2_1(m):
     global j
     global data1
     print(m.text)
     print(j)
     try:
       data2[0] = int(m.text)
       j = j-int(m.text)
       if j<0:
           bot.send_message(m.chat.id,'Сумма баллов превышает 10, возврат к первому вопросу')
           q2_1(m)
       else:
           if j==0:
              q3_1(m)
           else:
              q2_2(m)
     except ValueError:
       q2_1(m)

def name2_2(m):
     global j
     global data1
     print(m.text)
     print(j)
     try:
       data2[1] = int(m.text)
       j = j-int(m.text)
       if j<0:
           bot.send_message(m.chat.id,'Сумма баллов превышает 10, возврат к первому вопросу')
           q2_1(m)
       else:
           if j==0:
              q3_1(m)
           else:
              q2_3(m)
     except ValueError:
       q2_2(m)

def name2_3(m):
     global j
     global data1
     print(m.text)
     print(j)
     try:
       data2[2] = int(m.text)
       j = j-int(m.text)
       if j<0:
           bot.send_message(m.chat.id,'Сумма баллов превышает 10, возврат к первому вопросу')
           q2_1(m)
       else:
           if j==0:
              q3_1(m)
           else:
              q2_4(m)
     except ValueError:
       q2_3(m)

def name2_4(m):
     global j
     global data1
     print(m.text)
     print(j)
     try:
       data2[3] = int(m.text)
       j = j-int(m.text)
       if j<0:
           bot.send_message(m.chat.id,'Сумма баллов превышает 10, возврат к первому вопросу')
           q2_1(m)
       else:
           if j==0:
              q3_1(m)
           else:
              q2_5(m)
     except ValueError:
       q2_4(m)

def name2_5(m):
     global j
     global data1
     print(m.text)
     print(j)
     try:
       data2[4] = int(m.text)
       j = j-int(m.text)
       if j<0:
           bot.send_message(m.chat.id,'Сумма баллов превышает 10, возврат к первому вопросу')
           q2_1(m)
       else:
           if j==0:
              q3_1(m)
           else:
              q2_6(m)
     except ValueError:
       q2_5(m)

def name2_6(m):
     global j
     global data1
     print(m.text)
     print(j)
     try:
       data2[5] = int(m.text)
       j = j-int(m.text)
       if j<0:
           bot.send_message(m.chat.id,'Сумма баллов превышает 10, возврат к первому вопросу')
           q2_1(m)
       else:
           if j==0:
              q3_1(m)
           else:
              q2_7(m)
     except ValueError:
       q2_6(m)

def name2_7(m):
     global j
     global data1
     print(m.text)
     print(j)
     try:
       data2[6] = int(m.text)
       j = j-int(m.text)
       if j<0:
           bot.send_message(m.chat.id,'Сумма баллов превышает 10, возврат к первому вопросу')
           q2_1(m)
       else:
           if j==0:
              q3_1(m)
           else:
              q2_8(m)
     except ValueError:
       q2_7(m)

def name2_8(m):
     global j
     global data1
     print(m.text)
     print(j)
     try:
       data2[7] = int(m.text)
       j = j-int(m.text)
       if j != 0:
          bot.send_message(m.chat.id,'Сумма баллов превышает 10, возврат к первому вопросу')
          q2_1(m)
       else:
          q3_1(m)
     except ValueError:
       q2_8(m)
#########################################################################################################################################################


#######################################################обработчики для третьего блока#####################################################################
def name3_1(m):
     global j
     global data1
     print(m.text)
     print(j)
     try:
       data3[0] = int(m.text)
       j = j-int(m.text)
       if j<0:
           bot.send_message(m.chat.id,'Сумма баллов превышает 10, возврат к первому вопросу')
           q3_1(m)
       else:
           if j==0:
              q4_1(m)
           else:
              q3_2(m)
     except ValueError:
       q3_1(m)

def name3_2(m):
     global j
     global data1
     print(m.text)
     print(j)
     try:
       data3[1] = int(m.text)
       j = j-int(m.text)
       if j<0:
           bot.send_message(m.chat.id,'Сумма баллов превышает 10, возврат к первому вопросу')
           q3_1(m)
       else:
           if j==0:
              q4_1(m)
           else:
              q3_3(m)
     except ValueError:
       q3_2(m)

def name3_3(m):
     global j
     global data1
     print(m.text)
     print(j)
     try:
       data3[2] = int(m.text)
       j = j-int(m.text)
       if j<0:
           bot.send_message(m.chat.id,'Сумма баллов превышает 10, возврат к первому вопросу')
           q3_1(m)
       else:
           if j==0:
              q4_1(m)
           else:
              q3_4(m)
     except ValueError:
       q3_3(m)

def name3_4(m):
     global j
     global data1
     print(m.text)
     print(j)
     try:
       data3[3] = int(m.text)
       j = j-int(m.text)
       if j<0:
           bot.send_message(m.chat.id,'Сумма баллов превышает 10, возврат к первому вопросу')
           q3_1(m)
       else:
           if j==0:
              q4_1(m)
           else:
              q3_5(m)
     except ValueError:
       q3_4(m)

def name3_5(m):
     global j
     global data1
     print(m.text)
     print(j)
     try:
       data3[4] = int(m.text)
       j = j-int(m.text)
       if j<0:
           bot.send_message(m.chat.id,'Сумма баллов превышает 10, возврат к первому вопросу')
           q3_1(m)
       else:
           if j==0:
              q4_1(m)
           else:
              q3_6(m)
     except ValueError:
       q3_5(m)


def name3_6(m):
     global j
     global data1
     print(m.text)
     print(j)
     try:
       data3[5] = int(m.text)
       j = j-int(m.text)
       if j<0:
           bot.send_message(m.chat.id,'Сумма баллов превышает 10, возврат к первому вопросу')
           q3_1(m)
       else:
           if j==0:
              q4_1(m)
           else:
              q3_7(m)
     except ValueError:
       q3_6(m)

def name3_7(m):
     global j
     global data1
     print(m.text)
     print(j)
     try:
       data3[6] = int(m.text)
       j = j-int(m.text)
       if j<0:
           bot.send_message(m.chat.id,'Сумма баллов превышает 10, возврат к первому вопросу')
           q3_1(m)
       else:
           if j==0:
              q4_1(m)
           else:
              q3_8(m)
     except ValueError:
       q3_7(m)

def name3_8(m):
     global j
     global data1
     print(m.text)
     print(j)
     try:
       data3[7] = int(m.text)
       j = j-int(m.text)
       if j != 0:
          bot.send_message(m.chat.id,'Сумма баллов не равна 10, возврат к началу части.')
          q3_1(m)
       else:
          q4_1(m)
     except ValueError:
       q3_8(m)

#########################################################################################################################################################

#######################################################обработчики для четвертого блока#####################################################################
def name4_1(m):
     global j
     global data1
     print(m.text)
     print(j)
     try:
       data4[0] = int(m.text)
       j = j-int(m.text)
       if j<0:
           bot.send_message(m.chat.id,'Сумма баллов превышает 10, возврат к первому вопросу')
           q4_1(m)
       else:
           if j==0:
              q5_1(m)
           else:
              q4_2(m)
     except ValueError:
       q4_1(m)

def name4_2(m):
     global j
     global data1
     print(m.text)
     print(j)
     try:
       data4[1] = int(m.text)
       j = j-int(m.text)
       if j<0:
           bot.send_message(m.chat.id,'Сумма баллов превышает 10, возврат к первому вопросу')
           q4_1(m)
       else:
           if j==0:
              q5_1(m)
           else:
              q4_3(m)
     except ValueError:
       q4_2(m)

def name4_3(m):
     global j
     global data1
     print(m.text)
     print(j)
     try:
       data4[2] = int(m.text)
       j = j-int(m.text)
       if j<0:
           bot.send_message(m.chat.id,'Сумма баллов превышает 10, возврат к первому вопросу')
           q4_1(m)
       else:
           if j==0:
              q5_1(m)
           else:
              q4_4(m)
     except ValueError:
       q4_3(m)

def name4_4(m):
     global j
     global data1
     print(m.text)
     print(j)
     try:
       data4[3] = int(m.text)
       j = j-int(m.text)
       if j<0:
           bot.send_message(m.chat.id,'Сумма баллов превышает 10, возврат к первому вопросу')
           q4_1(m)
       else:
           if j==0:
              q5_1(m)
           else:
              q4_5(m)
     except ValueError:
       q4_4(m)

def name4_5(m):
     global j
     global data1
     print(m.text)
     print(j)
     try:
       data4[4] = int(m.text)
       j = j-int(m.text)
       if j<0:
           bot.send_message(m.chat.id,'Сумма баллов превышает 10, возврат к первому вопросу')
           q4_1(m)
       else:
           if j==0:
              q5_1(m)
           else:
              q4_6(m)
     except ValueError:
       q4_5(m)

def name4_6(m):
     global j
     global data1
     print(m.text)
     print(j)
     try:
       data4[5] = int(m.text)
       j = j-int(m.text)
       if j<0:
           bot.send_message(m.chat.id,'Сумма баллов превышает 10, возврат к первому вопросу')
           q4_1(m)
       else:
           if j==0:
              q5_1(m)
           else:
              q4_7(m)
     except ValueError:
       q4_6(m)

def name4_7(m):
     global j
     global data1
     print(m.text)
     print(j)
     try:
       data4[6] = int(m.text)
       j = j-int(m.text)
       if j<0:
           bot.send_message(m.chat.id,'Сумма баллов превышает 10, возврат к первому вопросу')
           q4_1(m)
       else:
           if j==0:
              q5_1(m)
           else:
              q4_8(m)
     except ValueError:
       q4_7(m)

def name4_8(m):
     global j
     global data1
     print(m.text)
     print(j)
     try:
       data4[7] = int(m.text)
       j = j-int(m.text)
       if j != 0:
          bot.send_message(m.chat.id,'Сумма баллов не равна 10, возврат к началу части.')
          q4_1(m)
       else:
          q5_1(m)
     except ValueError:
       q4_8(m)

#########################################################################################################################################################


#######################################################обработчики для пятого блока#####################################################################
def name5_1(m):
     global j
     global data1
     print(m.text)
     print(j)
     try:
       data5[0] = int(m.text)
       j = j-int(m.text)
       if j<0:
           bot.send_message(m.chat.id,'Сумма баллов превышает 10, возврат к первому вопросу')
           q5_1(m)
       else:
           if j==0:
              q6_1(m)
           else:
              q5_2(m)
     except ValueError:
       q5_1(m)

def name5_2(m):
     global j
     global data1
     print(m.text)
     print(j)
     try:
       data5[1] = int(m.text)
       j = j-int(m.text)
       if j<0:
           bot.send_message(m.chat.id,'Сумма баллов превышает 10, возврат к первому вопросу')
           q5_1(m)
       else:
           if j==0:
              q6_1(m)
           else:
              q5_3(m)
     except ValueError:
       q5_2(m)

def name5_3(m):
     global j
     global data1
     print(m.text)
     print(j)
     try:
       data5[2] = int(m.text)
       j = j-int(m.text)
       if j<0:
           bot.send_message(m.chat.id,'Сумма баллов превышает 10, возврат к первому вопросу')
           q5_1(m)
       else:
           if j==0:
              q6_1(m)
           else:
              q5_4(m)
     except ValueError:
       q5_3(m)

def name5_4(m):
     global j
     global data1
     print(m.text)
     print(j)
     try:
       data5[3] = int(m.text)
       j = j-int(m.text)
       if j<0:
           bot.send_message(m.chat.id,'Сумма баллов превышает 10, возврат к первому вопросу')
           q5_1(m)
       else:
           if j==0:
              q6_1(m)
           else:
              q5_5(m)
     except ValueError:
       q5_4(m)

def name5_5(m):
     global j
     global data1
     print(m.text)
     print(j)
     try:
       data5[4] = int(m.text)
       j = j-int(m.text)
       if j<0:
           bot.send_message(m.chat.id,'Сумма баллов превышает 10, возврат к первому вопросу')
           q5_1(m)
       else:
           if j==0:
              q6_1(m)
           else:
              q5_6(m)
     except ValueError:
       q5_5(m)

def name5_6(m):
     global j
     global data1
     print(m.text)
     print(j)
     try:
       data5[5] = int(m.text)
       j = j-int(m.text)
       if j<0:
           bot.send_message(m.chat.id,'Сумма баллов превышает 10, возврат к первому вопросу')
           q5_1(m)
       else:
           if j==0:
              q6_1(m)
           else:
              q5_7(m)
     except ValueError:
       q5_6(m)

def name5_7(m):
     global j
     global data1
     print(m.text)
     print(j)
     try:
       data5[6] = int(m.text)
       j = j-int(m.text)
       if j<0:
           bot.send_message(m.chat.id,'Сумма баллов превышает 10, возврат к первому вопросу')
           q5_1(m)
       else:
           if j==0:
              q6_1(m)
           else:
              q5_8(m)
     except ValueError:
       q5_7(m)

def name5_8(m):
     global j
     global data1
     print(m.text)
     print(j)
     try:
       data5[7] = int(m.text)
       j = j-int(m.text)
       if j != 0:
          bot.send_message(m.chat.id,'Сумма баллов не равна 10, возврат к началу части.')
          q5_1(m)
       else:
          q6_1(m)
     except ValueError:
       q5_8(m)

#########################################################################################################################################################



#######################################################обработчики для шестого блока#####################################################################
def name6_1(m):
     global j
     global data1
     print(m.text)
     print(j)
     try:
       data6[0] = int(m.text)
       j = j-int(m.text)
       if j<0:
           bot.send_message(m.chat.id,'Сумма баллов превышает 10, возврат к первому вопросу')
           q6_1(m)
       else:
           if j==0:
              q7_1(m)
           else:
              q6_2(m)
     except ValueError:
       q6_1(m)
  
def name6_2(m):
     global j
     global data1
     print(m.text)
     print(j)
     try:
       data6[1] = int(m.text)
       j = j-int(m.text)
       if j<0:
           bot.send_message(m.chat.id,'Сумма баллов превышает 10, возврат к первому вопросу')
           q6_1(m)
       else:
           if j==0:
              q7_1(m)
           else:
              q6_3(m)
     except ValueError:
       q6_2(m)

def name6_3(m):
     global j
     global data1
     print(m.text)
     print(j)
     try:
       data6[2] = int(m.text)
       j = j-int(m.text)
       if j<0:
           bot.send_message(m.chat.id,'Сумма баллов превышает 10, возврат к первому вопросу')
           q6_1(m)
       else:
           if j==0:
              q7_1(m)
           else:
              q6_4(m)
     except ValueError:
       q6_3(m)

def name6_4(m):
     global j
     global data1
     print(m.text)
     print(j)
     try:
       data6[3] = int(m.text)
       j = j-int(m.text)
       if j<0:
           bot.send_message(m.chat.id,'Сумма баллов превышает 10, возврат к первому вопросу')
           q6_1(m)
       else:
           if j==0:
              q7_1(m)
           else:
              q6_5(m)
     except ValueError:
       q6_4(m)

def name6_5(m):
     global j
     global data1
     print(m.text)
     print(j)
     try:
       data6[4] = int(m.text)
       j = j-int(m.text)
       if j<0:
           bot.send_message(m.chat.id,'Сумма баллов превышает 10, возврат к первому вопросу')
           q6_1(m)
       else:
           if j==0:
              q7_1(m)
           else:
              q6_6(m)
     except ValueError:
       q6_5(m)

def name6_6(m):
     global j
     global data1
     print(m.text)
     print(j)
     try:
       data5[5] = int(m.text)
       j = j-int(m.text)
       if j<0:
           bot.send_message(m.chat.id,'Сумма баллов превышает 10, возврат к первому вопросу')
           q6_1(m)
       else:
           if j==0:
              q7_1(m)
           else:
              q6_7(m)
     except ValueError:
       q6_6(m)

def name6_7(m):
     global j
     global data1
     print(m.text)
     print(j)
     try:
       data6[6] = int(m.text)
       j = j-int(m.text)
       if j<0:
           bot.send_message(m.chat.id,'Сумма баллов превышает 10, возврат к первому вопросу')
           q6_1(m)
       else:
           if j==0:
              q7_1(m)
           else:
              q6_8(m)
     except ValueError:
       q6_7(m)

def name6_8(m):
     global j
     global data1
     print(m.text)
     print(j)
     try:
       data6[7] = int(m.text)
       j = j-int(m.text)
       if j != 0:
          bot.send_message(m.chat.id,'Сумма баллов не равна 10, возврат к началу части.')
          q6_1(m)
       else:
          q7_1(m)
     except ValueError:
       q6_8(m)


#########################################################################################################################################################



#######################################################обработчики для седьмого блока#####################################################################
def name7_1(m):
     global j
     global data1
     print(m.text)
     print(j)
     try:
       data7[0] = int(m.text)
       j = j-int(m.text)
       if j<0:
           bot.send_message(m.chat.id,'Сумма баллов превышает 10, возврат к первому вопросу')
           q7_1(m)
       else:
           if j==0:
              out(m)
           else:
              q7_2(m)
     except ValueError:
       q7_1(m)

def name7_2(m):
     global j
     global data1
     print(m.text)
     print(j)
     try:
       data7[1] = int(m.text)
       j = j-int(m.text)
       if j<0:
           bot.send_message(m.chat.id,'Сумма баллов превышает 10, возврат к первому вопросу')
           q7_1(m)
       else:
           if j==0:
              out(m)
           else:
              q7_3(m)
     except ValueError:
       q7_2(m)

def name7_3(m):
     global j
     global data1
     print(m.text)
     print(j)
     try:
       data7[2] = int(m.text)
       j = j-int(m.text)
       if j<0:
           bot.send_message(m.chat.id,'Сумма баллов превышает 10, возврат к первому вопросу')
           q7_1(m)
       else:
           if j==0:
              out(m)
           else:
              q7_4(m)
     except ValueError:
       q7_3(m)

def name7_4(m):
     global j
     global data1
     print(m.text)
     print(j)
     try:
       data7[3] = int(m.text)
       j = j-int(m.text)
       if j<0:
           bot.send_message(m.chat.id,'Сумма баллов превышает 10, возврат к первому вопросу')
           q7_1(m)
       else:
           if j==0:
              out(m)
           else:
              q7_5(m)
     except ValueError:
       q7_4(m)

def name7_5(m):
     global j
     global data1
     print(m.text)
     print(j)
     try:
       data7[4] = int(m.text)
       j = j-int(m.text)
       if j<0:
           bot.send_message(m.chat.id,'Сумма баллов превышает 10, возврат к первому вопросу')
           q7_1(m)
       else:
           if j==0:
              out(m)
           else:
              q7_6(m)
     except ValueError:
       q7_5(m)

def name7_6(m):
     global j
     global data1
     print(m.text)
     print(j)
     try:
       data7[5] = int(m.text)
       j = j-int(m.text)
       if j<0:
           bot.send_message(m.chat.id,'Сумма баллов превышает 10, возврат к первому вопросу')
           q7_1(m)
       else:
           if j==0:
              out(m)
           else:
              q7_7(m)
     except ValueError:
       q7_6(m)

def name7_7(m):
     global j
     global data1
     print(m.text)
     print(j)
     try:
       data7[6] = int(m.text)
       j = j-int(m.text)
       if j<0:
           bot.send_message(m.chat.id,'Сумма баллов превышает 10, возврат к первому вопросу')
           q7_1(m)
       else:
           if j==0:
              out(m)
           else:
              q7_8(m)
     except ValueError:
       q7_7(m)

def name7_8(m):
     global j
     global data1
     print('name_data')
     print(neme_data)
     print(m.text)
     print(j)
     try:
       data7[7] = int(m.text)
       j = j-int(m.text)
       if j != 0:
          bot.send_message(m.chat.id,'Сумма баллов не равна 10, возврат к началу части.')
          q7_1(m)
          print('test')
       else:
          out(m)
     except ValueError:
       q7_8(m)
#########################################################################################################################################################

while True:
    try:
        bot.polling(none_stop=True)

    except Exception as e:
        print('timeout_err')  # или просто print(e) если у вас логгера нет,
        # или import traceback; traceback.print_exc() для печати полной инфы
        time.sleep(15)
