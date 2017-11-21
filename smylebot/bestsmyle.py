# -*- coding: utf-8 -*-

import telebot
import time
import smtplib
from telebot import types
from email.mime.text import MIMEText
from email.header import Header

bot = telebot.TeleBot("491102670:AAHSRmXLg8Iuwg5THJyfgp2eaXv13vhMUwI",threaded=False)
# задаю векторы для накопления данных опроса

nam = '-1'
tel = '-1'
dat = '-1'
commen = '-1'
prom = '-1'

@bot.message_handler(commands=['start'])
def start(m):
   m.text = 'НАЧАТЬ↩️'
   nachat(m)

def nachat(m):
    if m.text == 'НАЧАТЬ↩️':
         print('nachat')                                    
         keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 2)
         keyboard.add(*[types.KeyboardButton(name) for name in ['ℹ️ О нас', '📧 Контакты', '💸 Услуги', '💠 Акции', '📆 Записаться на бесплатную консультацию']])
         msg = bot.send_message(m.chat.id,'Вы в главном меню', reply_markup=keyboard)
         bot.register_next_step_handler(msg,step2)

def step2(m):
    if m.text == 'ℹ️ О нас':
         print('о нас')                                    
         keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 2)
         keyboard.add(*[types.KeyboardButton(name) for name in ['ℹ️ О нас', '📧 Контакты', '💸 Услуги', '💠 Акции', '📆 Записаться на бесплатную консультацию']])
         msg = bot.send_message(m.chat.id,'***Солодкий Богдан Сергеевич***, врач-стоматолог. Опыт работы более 10 лет. \n***Специализация*** \nТерапевтическая стоматология: профессиональная гигиена полости рта, отбеливание, реставрация зубов;Ортопедическая стоматология: протезирование металлокерамическими коронками, коронками на основе диоксида циркония, протезирование на имплантах. Лечение проводится на современном оборудовании, только качественными материалами, с соблюдением всех норм стерилизации и дезинфекции.', reply_markup=keyboard, parse_mode="Markdown")
         bot.register_next_step_handler(msg,step2)
    if m.text == '📧 Контакты':
         print('контакты')                                    
         keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 2)
         keyboard.add(*[types.KeyboardButton(name) for name in ['ℹ️ О нас', '📧 Контакты', '💸 Услуги', '💠 Акции', '📆 Записаться на бесплатную консультацию']])
         msg = bot.send_message(m.chat.id,'Вы всегда можете с нами связаться с помощью: \n***Телефон регистрации:*** +7(925)091-19-13 \n***Телефон консультации:*** +7(968)096-81-06 \n***сайт:*** cool-smile.ru \n***e-mail:*** (дам позже) \n***социальные сети:*** \n***Instagram:*** bogdansolodkiy \n***FB*** – Богдан Солодский', reply_markup=keyboard, parse_mode="Markdown")
         bot.register_next_step_handler(msg,step2)
    if m.text == '💸 Услуги':
         print('Услуги')                                    
         keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 2)
         keyboard.add(*[types.KeyboardButton(name) for name in ['➡️Чистка и отбеливание', '➡️Лечение', '➡️Протезирование', '➡️Хирургия и Имплантация']])
         msg = bot.send_message(m.chat.id,'Раздел "Услуги"', reply_markup=keyboard)
         bot.register_next_step_handler(msg,uslugi)
    if m.text == '💠 Акции':
         print('Акции')                                    
         keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 1)
         keyboard.add(*[types.KeyboardButton(name) for name in ['➡️ЗАПИСАТЬСЯ ПО АКЦИИ', '➡️У МЕНЯ ЕСТЬ ПРОМОКОД', '🔙Главное меню']])
         msg = bot.send_message(m.chat.id,'***Профессиональная гигиена полости рта, весь комплекс всего за 4 000 рублей!*** \nВходит: ультразвуковая чистка, чистка Air Flow, финишная полировка пастой \n\nОТБЕЛИВАНИЕ ЗУБОВ ХОЛОДНЫМ СВЕТОМ ЛИБО ЛАЗЕРНОЕ ВСЕГО 10000 рублей!"', reply_markup=keyboard, parse_mode="Markdown")
         bot.register_next_step_handler(msg,actions_out)
    if m.text == '📆 Записаться на бесплатную консультацию':
         print('запись')                                    
         zapis(m)

def uslugi(m):
    if m.text == '➡️Чистка и отбеливание':
         print('Чистка и отбеливание')                                    
         keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 1)
         keyboard.add(*[types.KeyboardButton(name) for name in ['📆Запись на Чистку или Отбеливание. Либо на бесплатную консультацию', '🔙Главное меню',]])
         msg = bot.send_message(m.chat.id,'***Чистка и Отбеливание \nКомплексная гигиена полости рта (Чистка) 4000 руб.***  \nПоказание: \nНаличие твердых (зубной камень) и мягких зубных отложений; \nНаличие налета курильщика, а также от пищевых красителей (кофе, чай и т.д.); \nЗаболевание десен, их кровоточивость; \nТак же плановая профилактика гигиены полости рта. \n\n***Отбеливание 10000 руб.*** \nПоказания: \nЭстетические показания; \nДисколорит зубов (наличие желтого, серого или тусклого оттенка', reply_markup=keyboard, parse_mode="Markdown")
         bot.register_next_step_handler(msg,uslugi_out)

    if m.text == '➡️Лечение':
         print('Лечение')                                    
         keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 1)
         keyboard.add(*[types.KeyboardButton(name) for name in ['📆Запись на Лечение или бесплатную консультацию', '🔙Главное меню',]])
         msg = bot.send_message(m.chat.id,'***Реставрация зуба от 3000 руб.*** \nПоказания: \nНаличие кариеса, повреждение зубной эмали; \nЭстетические показания \n\n***Лечение каналов зуба от 3000 руб.*** \nПоказания: \nПроводится при пульпите (воспаление нерва зуба); \nПереодонтите (воспаление на корнезуба)', reply_markup=keyboard, parse_mode="Markdown")
         bot.register_next_step_handler(msg,uslugi_out)

    if m.text == '➡️Протезирование':
         print('Протезирование')                                    
         keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 1)
         keyboard.add(*[types.KeyboardButton(name) for name in ['📆 Запись на Протезирование или бесплатную консультацию', '🔙Главное меню',]])
         msg = bot.send_message(m.chat.id,'***Коронка от 8000 руб.*** \n Показания: \n Коронка ставится при разрушении зуба более 50%, дефектах формы и цвета зуба \n \n ***Виниры от 17000 руб.*** \n Показания: \n Коррекция положения зубов, выраженные дисколориты, не поддающиеся отбеливанию.', reply_markup=keyboard, parse_mode="Markdown")
         bot.register_next_step_handler(msg,uslugi_out)
   
    if m.text == '➡️Хирургия и Имплантация':
         print('Хирургия и Имплантация')                                    
         keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 1)
         keyboard.add(*[types.KeyboardButton(name) for name in ['📆 Запись на Хирургия или Имплантация. Либо на бесплатную консультацию', '🔙Главное меню',]])
         msg = bot.send_message(m.chat.id,'***Удаление от 3000 руб.*** \nПоказания: \nПри сильной разрушенности зуба; \nОтсутствие возможности лечения каналов; \nНеправильность роста и положения зубов мудрости \n\n***Имплантация от 15000 руб.*** \nПоказания: \nПроводится при отсутствии одного или нескольких зубов; \nАльтернатива съемному протезирован', reply_markup=keyboard, parse_mode="Markdown")
         bot.register_next_step_handler(msg,uslugi_out)

def uslugi_out(m):
          if m.text == '📆Запись на Чистку или Отбеливание. Либо на бесплатную консультацию':
            print('запись')                                    
            zapis(m)
          if m.text == '📆Запись на Лечение или бесплатную консультацию':
            print('запись')                                    
            zapis(m)
          if m.text == '📆 Запись на Протезирование или бесплатную консультацию':
            print('запись')                                    
            zapis(m)
          if m.text == '📆 Запись на Хирургия или Имплантация. Либо на бесплатную консультацию':
            print('запись')                                    
            zapis(m)
          if m.text == '🔙Главное меню':
            print('Главное меню')        
            m.text = 'НАЧАТЬ↩️'                 
            nachat(m)

def actions_out(m):
    if m.text == '➡️ЗАПИСАТЬСЯ ПО АКЦИИ':
         print('запись по акции')                                    
         zapis_actions(m)
    if m.text == '➡️У МЕНЯ ЕСТЬ ПРОМОКОД':
         print('запись по акции')                                    
         zapis_promo(m)
    if m.text == '🔙Главное меню':
         print('Главное меню')        
         m.text = 'НАЧАТЬ↩️'                            
         nachat(m)

####################################################обработка результата#################################################################################
def name(m):
     global nem
     nem = m.text
     msg = bot.send_message(m.chat.id,'Напишите удобную дату и время приёма')
     bot.register_next_step_handler(msg,data)
def data(m):
     global dat
     dat = m.text
     msg = bot.send_message(m.chat.id,'Напишите контактный телефон')
     bot.register_next_step_handler(msg,tele)
def promo(m):
     global prom
     prom = m.text
     msg = bot.send_message(m.chat.id,'Напишите свое имя')
     bot.register_next_step_handler(msg,name)
def tele(m):
     global tel
     tel = m.text
     bot.send_message(m.chat.id,'Вы записаны на приём 📌, если хотите продолжить общение с ботом то нажмите /start')
     zapis_out(m)
def zapis(m):
     # логирование в файлик.
     keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 1)
     keyboard.add(*[types.KeyboardButton(name) for name in ['Пропустить']])
    # msg = bot.send_message(m.chat.id,'Напишите своё имя')
     msg = bot.send_message(m.chat.id,'Напишите своё имя', reply_markup=keyboard)
     bot.register_next_step_handler(msg,name)
def zapis_out(m):
     tomail = str(m.chat.id)+';  '+prom+';  '+nem+';  '+dat+';  '+tel
     msgout = MIMEText(tomail,'plain','utf-8')
     smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
     smtpObj.starttls()
     smtpObj.login('coolsmilebot@gmail.com','qhgiaohgohgo5g78yg')
     smtpObj.sendmail("coolsmilebot@gmail.com","valer-g2005@yandex.ru",msgout.as_string())
     smtpObj.quit()
def zapis_promo(m):
     keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 1)
     keyboard.add(*[types.KeyboardButton(name) for name in ['Пропустить']])
     msg = bot.send_message(m.chat.id,'Напишите промокод', reply_markup=keyboard)
     bot.register_next_step_handler(msg,zapis)
def zapis_actions(m):
     # логирование в файлик.
     keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 1)
     keyboard.add(*[types.KeyboardButton(name) for name in ['Пропустить']])
     msg = bot.send_message(m.chat.id,'Напишите какая акция', reply_markup=keyboard)
     bot.register_next_step_handler(msg,promo)
bot.polling(none_stop=True)


