import telebot
from telebot import types
import random

bot = telebot.TeleBot("token")


a = 0 # баланс
c = 1 # добыча монет за клик
da = 5 # цена за доп клик
da2 = 2 # цена за доп здоровье
Click_Number = 0 # Число кликов
health = 10 # Здоровье
na4 = 150 # Здоровье босса
kon = 200 # Здоровье босса
uron1 = 20 # урон босса
uron2 = 30 # Урон босса рандомен
boss = int(random.uniform(1, 1))
rov = 0 #так как в магазине у нас там два

@bot.message_handler(commands=['start'])
def send_welcome(message):
	
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	btn1 = types.KeyboardButton("Клик")
	btn2 = types.KeyboardButton("Магазин")
	btn3 = types.KeyboardButton("Профиль")
	btn4 = types.KeyboardButton("Сражение с боссом")
	markup.add(btn1)
	markup.add(btn2, btn3)
	markup.add(btn4)
	bot.send_message(message.chat.id, "Загрузка..." , reply_markup=markup)
	



	#ОБРАБОТЧИК СОБЫТИИ
@bot.message_handler(func=lambda message: True)
def echo_all(message):
	global a
	global c
	global da
	global da2
	global Click_Number
	global health
	global na4
	global kon
	global uron1
	global uron2
	global boss
	global rov
	
	# KEYBOARDS MENU
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
	btn1 = types.KeyboardButton("Клик")
	btn2 = types.KeyboardButton("Магазин")
	btn3 = types.KeyboardButton("Профиль")
	btn4 = types.KeyboardButton("Cражение с боссом")
	markup.add(btn1)
	markup.add(btn2, btn3)
	markup.add(btn4)

	#KEYBOARDS SHOP
	shop = types.ReplyKeyboardMarkup(resize_keyboard=True)
	shp1 = types.KeyboardButton("Улучшить клик") 
	shp2 = types.KeyboardButton("Улучшить здоровье")
	shp3 = types.KeyboardButton("Назад")
	shop.add(shp1, shp2)
	shop.add(shp3)

	#KEYBOARDS BOSS
	bss = types.ReplyKeyboardMarkup(resize_keyboard=True)
	bs1 = types.KeyboardButton("Клик") 
	bs2 = types.KeyboardButton("Cбежать")
	bss = types.ReplyKeyboardMarkup(resize_keyboard=True)
	bss.add(bs1)
	bss.add(bs2)

	#KEYBOARDS SHOP CONFIRMATION
	shopc = types.ReplyKeyboardMarkup(resize_keyboard=True)
	shc1=types.KeyboardButton("Купить")
	shc2=types.KeyboardButton("Отменить")
	shopc.add(shc1, shc2)

	if message.text == "Клик" and boss >= 2: 
		boss -= c 
		bot.send_message(message.chat.id, f"Здоровье босса: {boss}hp \nВы нанесли {c} урона", reply_markup=bss)
		dod = int(random.uniform(uron1, uron2)) 
		health -= dod
		bot.send_message(message.chat.id, f"Ваше здоровье: {health}hp \nВы потеряли {dod} здоровья ", reply_markup=bss)
	elif message.text == "Клик":
		a+=c
		Click_Number += 1
		bot.send_message(message.chat.id, f"Ваш баланс: {a} монет \nВы прибавили: +{c}", reply_markup=markup)


	if message.text == "Магазин":
		bot.send_message(message.chat.id, "Магазин открыт", reply_markup=shop)


	if message.text == "Улучшить клик":
		rov = 1 # клик
		bot.send_message(message.chat.id, f" Ваш баланс: {a} монет \nЦена: {da} монет", reply_markup=shopc)
	if message.text == "Купить" and a >= da and rov ==1:
		a -= da # баланс минус цена за доп клик
		c += 1 # +1 к клику
		da *= 2 # price for click
		bot.send_message(message.chat.id, f"Вы улучшили свой клик: +1\nКлик: +{c}", reply_markup=shopc)
	if message.text == "Купить" and a < da and rov ==1:
			bot.send_message(message.chat.id,"У вас недостаточно: " + str(da - a) + " монет", reply_markup=shopc)
	if message.text == "Отменить":
		rov = 0
		bot.send_message(message.chat.id, "Сделка отменена", reply_markup=shop)



	if message.text == "Улучшить здоровье":
		rov = 2 # жизнь
		bot.send_message(message.chat.id,f"Ваш баланс: {a} монет \nЦена: {da2} монет", reply_markup=shopc)
	if message.text == "Купить" and a >= da2 and rov == 2:
		a -= da2
		health += 10
		da2 *= 2 # price for health
		bot.send_message(message.chat.id, f"Вы улучшили своё здоровье: +10hp \nЗдоровье: {health}", reply_markup=shopc)
	if message.text == "Купить" and a < da2 and rov == 2:  
		bot.send_message(message.chat.id,"У вас недостаточно: " + str(da2 - a) + " монет",reply_markup=shopc)

	if message.text == "Назад":
		bot.send_message(message.chat.id, "Меню", reply_markup=markup)

	if message.text == "Cражение с боссом":
		boss = int(random.uniform(na4, kon))
		bot.send_message(message.chat.id,f"Здоровье босса: {boss}hp\nУрон босса: 20-30 едениц",reply_markup=bss)
	if boss <= 0:
		bot.send_message(message.chat.id,f"Вы полностью прошли игру!\nНаграда: +10 к клику",reply_markup=markup)
		boss=1
		c+=10
	if message.text == "Cбежать":
		poter = int(random.uniform(20, 80))
		a-=poter
		bot.send_message(message.chat.id, f"Вы успешно сбежали, поджав хвост\nПотеряв по дороге {poter} монет",reply_markup=markup)
		boss = 1
	if health <= 0:
		bot.send_message(message.chat.id,"Вас убили... \nВесь ваш прогресс сброшен",reply_markup=markup)
		a = 0 # баланс
		c = 1 # добыча монет за клик
		da = 5 # цена за доп клик
		da2 = 4 # цена за доп здоровье
		Click_Number = 0 # Число кликов
		health = 10 # Здоровье
		na4 = 150 # hp of boss
		kon = 200
		uron1 = 20
		uron2 = 30
		boss = int(random.uniform(1, 1))
	if message.text == "чде":

		a =+ 18118
		health =+ 140
		c=+ 12000
		Click_Number = 0 


	if message.text == "Профиль":
   		bot.send_message(message.chat.id, f"Баланс: {a} монет\nЗдоровье: {health}hp \nДобыча за клик: {c} \nКоличество кликов: {Click_Number}", reply_markup=markup)
	# elif message.text == "улучшить клик":
	# 	rov = 1 
	# 	bot.send_message(message.chat.id, f" Ваш баланс: {a} монет \nЦена: {da} монет", reply_markup=shopc)

bot.infinity_polling() 
