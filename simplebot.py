import logging
import ephem
import datetime

logging.basicConfig(format='%(name)s-%(levelname)s-%(message)s',
	level=logging.INFO,
	filename='bot.log')

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def start_bot(bot, update):
#    print(update)
    mytext = "Привет! как дела?"
    update.message.reply_text(mytext)
    print("start")

def find_planet(bot, update):
    update.message.reply_text('Введите название планеты?')

# def talk_to_me(bot, update):
#    user_text = update.message.text
#    print(user_text)
#    update.message.reply_text(user_text)

# planet_dict = {'Venus' : ephem.Venus, 'Mars' : ephem.Mars}

def get_answer(bot, update):
    
    user_text = str(update.message.text)
    
    # sym_index = 0
    # for sym in user_text:
    #     sym_index = sym_index + 1
    #     if sym == "+":
    #         sign_pos = sym_index
    #         print(sign_pos)

    # user_text = str(update.message.text)
    # print(user_text)
        
    # number_of_spaces = 0
    # sym_index = 0
    # for sym in user_text:
    #     sym_index = sym_index + 1
    #     if sym is ' ':
    #         if sym_index != 1 or len(user_text):
    #             number_of_spaces = number_of_spaces + 1

    # print(number_of_spaces)        

    # number_of_words = number_of_spaces + 1
    # update.message.reply_text(number_of_words)

    # planet_selection = planet_dict.get(user_text)
    
    # if planet_selection is None:
    #     update.message.reply_text('Введите правильное название на английском языке!')
    
    # planet_pos = planet_selection(datetime.date.today())
    # reply_to_user = ephem.constellation(planet_pos)
    # update.message.reply_text(reply_to_user)

# def count_words(user_text):
#     for word_spacing in user_text:
#         if word_spacing == ' ':
#             number_of_spaces += 1

def word_counter(bot, update):
    update.message.reply_text('Введите фразу')

def main():
    updater = Updater("406676275:AAFxpdNjU3c7LdmauuNyGiUx5u4BY-8g1_s")

    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler("start",start_bot))
    dp.add_handler(CommandHandler("planet",find_planet))
    dp.add_handler(CommandHandler("wordcount",word_counter))
    # dp.add_handler(CommandHandler("calc",calculator))
    dp.add_handler(MessageHandler(Filters.text,get_answer))

    updater.start_polling()
    updater.idle()
    



if __name__ == "__main__":
    main()