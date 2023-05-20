# подключение библиотек
# В google colab добавить: !pip install pyTelegramBotAPI

from telebot import TeleBot, types


bot = TeleBot(token='токен', parse_mode='html') # создание бота


# обработчик команды '/start'
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Лицо😊")
    btn2 = types.KeyboardButton("Глаза👀")
    btn3 = types.KeyboardButton("Брови🥸")
    btn4 = types.KeyboardButton("Губы👄")
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Выбери категорию😉".format(message.from_user), reply_markup=markup)
    bot.send_video(message.chat.id, 'https://media.tenor.com/1HJQoy-7NYgAAAAC/lipstick-cat-warner.gif', None, 'Text')

# обработчик всех остальных сообщений    
@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "Лицо😊"):
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
     btn1 = types.KeyboardButton("База под макияж/Праймер")
     btn2 = types.KeyboardButton("Тональная основа")
     btn3 = types.KeyboardButton("Консилер")
     btn4 = types.KeyboardButton("Пудра")
     btn5 = types.KeyboardButton("Скульптор")
     btn6 = types.KeyboardButton("Румяна")
     btn7 = types.KeyboardButton("Хайлайтер")
     btn8 = types.KeyboardButton("Фиксатор макияжа")
     btn9 = types.KeyboardButton("Выбрать другую категорию")
     markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9)
     bot.send_message(message.chat.id,text="Выбери продукт, который тебя интересует, и узнай о нем больше😉", reply_markup=markup)

    elif(message.text == "База под макияж/Праймер"):
      bot.send_message(message.chat.id,"Праймер – это база под тональное средство. Содержащиеся в его составе компоненты помогают значительно продлить стойкость макияжа. Средство выравнивает рельеф кожи, делая ее более гладкой, а также зачастую помогает скрыть мелкие недостатки – например, расширенные поры. Благодаря этому тональная основа распределяется более ровным слоем.")

    elif(message.text == "Тональная основа"):
      bot.send_message(message.chat.id,"Тональная основа — это крем с содержанием тонирующих пигментов, который обычно служит для получения оптического эффекта: маскирует покраснения и несовершенства, выравнивает тон и рельеф кожи. При этом средство может содержать различные ухаживающие компоненты.")
    
    elif(message.text == "Консилер"):
      bot.send_message(message.chat.id,"Консилер – это средство для маскировки локальных несовершенств кожи.")

    elif(message.text == "Пудра"):
      bot.send_message(message.chat.id,"Пудра - это декоративное косметическое средство в виде мелкого порошка, используемое для закрепления макияжа, а также как самостоятельный продукт для выравнивания цвета и, в том числе, рельефа кожи.")

    elif(message.text == "Скульптор"):
      bot.send_message(message.chat.id,"Скульптор преображает лицо и делает его черты более аккуратными, помогает скрыть щечки и прорисовывает все естественные теневые зоны на лице. Цвет скульптора должен напоминать цвет естественной тени, поэтому самый подходящий оттенок скульптора – это холодный, приглушенный коричневый с примесями серого и зеленого.")

    elif(message.text == "Румяна"):
      bot.send_message(message.chat.id,"Румяна — косметическое средство для наведения румянца на щеках. Его наносят в виде пудры или крема. Используется для придания более свежего и молодого вида и/или чтобы подчеркнуть скулы.")

    elif(message.text == "Хайлайтер"):
      bot.send_message(message.chat.id,"Хайлайтер – косметическое средство, главная цель которого – «привлекать» световые лучи и отражать их, создавая иллюзию кожи, подсвеченной изнутри.")

    elif(message.text == "Фиксатор макияжа"):
      bot.send_message(message.chat.id,"Фиксатор – это спрей, который наносится на лицо для того, чтобы макияж держался долго: не смазался и не потёк.")

    elif(message.text == "Глаза👀"):
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
     btn1 = types.KeyboardButton("База под тушь")
     btn2 = types.KeyboardButton("База под тени")
     btn3 = types.KeyboardButton("Тушь")
     btn4 = types.KeyboardButton("Тени")
     btn5 = types.KeyboardButton("Карандаш для глаз/Кайал")
     btn6 = types.KeyboardButton("Подводка для глаз")
     btn7 = types.KeyboardButton("Выбрать другую категорию")
     markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
     bot.send_message(message.chat.id,text="Выбери продукт, который тебя интересует, и узнай о нем больше😉", reply_markup=markup)

    elif(message.text == "База под тушь"):
      bot.send_message(message.chat.id,"База под тушь – косметическое средство, которое подготавливает ресницы к нанесению туши. База под тушь, она же праймер, основа, бывает белой или прозрачной. Основа обволакивает, разделяет, удлиняет ресницы, придает им упругость, объем, плавный изгиб.")

    elif(message.text == "База под тени"):
      bot.send_message(message.chat.id,"База под тени (другое название – праймер или основа под тени) – средство для макияжа глаз, подготавливающее кожу для нанесения теней и увеличивающее их стойкость.")
    
    elif(message.text == "Тушь"):
      bot.send_message(message.chat.id,"Тушь для ресниц — декоративная косметика, предназначенная для подчёркивания, выделения и изменения естественного цвета ресниц. Тушь производится в различных формах: жидкая, кремообразная и сухая.")

    elif(message.text == "Тени"):
      bot.send_message(message.chat.id,"Тени для век – средство декоративной косметики, которое используют для макияжа глаз. Бывают разной консистенции: сухие, кремовые, жидкие, тени-карандаш, компактные, минеральные. Самые распространенные – сухие тени, они легче всего наносятся и растушевываются. Тени бывают разных видов: матовые, атласные, с шиммером.")

    elif(message.text == "Карандаш для глаз/Кайал"):
      bot.send_message(message.chat.id,"Кайал — контурный мягкий косметический карандаш для подводки глаз, в традиционный состав которого входят натуральная сажа или измельчённые минералы и антисептические вещества растительного происхождения.")

    elif(message.text == "Подводка для глаз"):
      bot.send_message(message.chat.id,"Это косметическое средство делает взгляд выразительным, позволяет создать яркий и притягательный образ.")


    elif(message.text == "Брови🥸"):
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
     btn1 = types.KeyboardButton("Карандаш для бровей")
     btn2 = types.KeyboardButton("Маркер для бровей")
     btn3 = types.KeyboardButton("Помада для бровей")
     btn4 = types.KeyboardButton("Тинт для бровей")
     btn5 = types.KeyboardButton("Тушь для бровей")
     btn6 = types.KeyboardButton("Гель для бровей")
     btn7 = types.KeyboardButton("Мыло для бровей")
     btn8 = types.KeyboardButton("Выбрать другую категорию")
     markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
     bot.send_message(message.chat.id,text="Выбери продукт, который тебя интересует, и узнай о нем больше😉", reply_markup=markup)

    elif(message.text == "Карандаш для бровей"):
      bot.send_message(message.chat.id,"Карандаш для бровей – самый простой и универсальный способ придать бровям необходимую форму. Максимально естественный эффект получается за счет прорисовки отдельных волосков на участках, где есть пустоты, пробелы. С помощью карандаша можно скорректировать бесцветные или редкие брови.")

    elif(message.text == "Маркер для бровей"):
      bot.send_message(message.chat.id,"По сути, маркер — это подводка для бровей; часто его называют «ручка» (brow pen). Он бывает с фетровым наконечником или кисточкой. Жидкая текстура сначала кажется непривычной, зато быстро высыхает и не растекается: маркеры обычно стойкие и иногда смываются только средством демакияжа.")
    
    elif(message.text == "Помада для бровей"):
      bot.send_message(message.chat.id,"Помада для бровей — это средство с кремовой, достаточной плотной текстурой, предназначенное для макияжа бровей. Как правило, помады выпускают в небольших круглых баночках, по виду скорее напоминает монотени для век.")

    elif(message.text == "Тинт для бровей"):
      bot.send_message(message.chat.id,"Тинт для бровей (от англ. tint – оттенок) – это домашняя альтернатива салонному окрашиванию и перманентному макияжу бровей.")

    elif(message.text == "Тушь для бровей"):
      bot.send_message(message.chat.id,"Тушь для бровей – это специальный гель, предназначенный для укладки или тонирования бровей. Как и в случае с ресницами, тушь для бровей придает волоскам объем и делает брови более выразительными. Это особенно важно для девушек с тонкими и редкими волосками.")

    elif(message.text == "Гель для бровей"):
      bot.send_message(message.chat.id,"Гель для бровей – это жидкое средство для укладки бровей. Он фиксирует волоски и придает им объем, делая брови аккуратными и четкими. Как правило, гели для бровей выпускают во флаконе с аппликатором или щеточкой (почти как у туши для ресниц).")

    elif(message.text == "Мыло для бровей"):
      bot.send_message(message.chat.id,"Мыло для бровей - это инновационный продукт для стайлинга бровей. Отличие мыла от геля в том, что с мылом можно уложить брови от корня до кончика с достаточно сильной фиксацией. Это может заменить процедуру долговременной укладки бровей до следующего умывания.")

    elif(message.text == "Губы👄"):
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
     btn1 = types.KeyboardButton("Карандаш для губ")
     btn2 = types.KeyboardButton("Помада")
     btn3 = types.KeyboardButton("Тинт для губ")
     btn4 = types.KeyboardButton("Блеск для губ")
     btn5 = types.KeyboardButton("Бальзам для губ")
     btn6 = types.KeyboardButton("Масло для губ")
     btn7 = types.KeyboardButton("Скраб для губ")
     btn8 = types.KeyboardButton("Маска для губ")
     btn9 = types.KeyboardButton("Выбрать другую категорию")
     markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9)
     bot.send_message(message.chat.id,text="Выбери продукт, который тебя интересует, и узнай о нем больше😉", reply_markup=markup)

    elif(message.text == "Карандаш для губ"):
      bot.send_message(message.chat.id,"Карандаш для губ — это косметическое средство, которое используется для подчеркивания контура губ и помогает губной помаде оставаться на месте.")

    elif(message.text == "Помада"):
      bot.send_message(message.chat.id,"Губная помада — косметический продукт для яркой окраски, защиты и/или увлажнения губ. Состоит из красок, воска, спермацета, вазелинового масла, масла-какао, ароматических и других веществ.")
    
    elif(message.text == "Тинт для губ"):
      bot.send_message(message.chat.id,"Тинт — это стойкий цветной пигмент, растворенный в жидкой или кремообразной основе. После нанесения эта основа впитывается или испаряется, а цвет остается на коже, словно бы «впечатываясь» в нее. Благодаря этому покрытие буквально сливается с губами и практически не ощущается на коже.")

    elif(message.text == "Блеск для губ"):
      bot.send_message(message.chat.id,"Блеск для губ - косметический продукт, придающий губам блеск и едва различимый цвет.")

    elif(message.text == "Бальзам для губ"):
      bot.send_message(message.chat.id,"Бальзам для губ (гигиеническая помада) — косметическое средство, которое используют для ухода за губами.")

    elif(message.text == "Масло для губ"):
      bot.send_message(message.chat.id,"Масла для губ — это бальзам и блеск в одном флаконе. Консистенция жидкая, текучая. Чаще всего представлены с аппликатором. Они питают и увлажняют губы и придают им легкий блеск — при этом совершенно не липкий.")

    elif(message.text == "Скраб для губ"):
      bot.send_message(message.chat.id,"Скраб для губ – это косметическое средство, призванное удалять с них омертвевшие частички, убирать шероховатость и шелушение.")

    elif(message.text == "Маска для губ"):
      bot.send_message(message.chat.id,"Маски для губ — популярное косметическое средство, которое обеспечивает дополнительный интенсивный уход за нежной кожей.")

    
    
    elif (message.text == "Выбрать другую категорию"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Лицо😊")
        btn2 = types.KeyboardButton("Глаза👀")
        btn3 = types.KeyboardButton("Брови🥸")
        btn4 = types.KeyboardButton("Губы👄")
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню😉", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="Не понимаю тебя😟")


# главная функция программы
def main():
    # запускаем нашего бота
    bot.infinity_polling()


if __name__ == '__main__':
    main()