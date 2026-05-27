import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

TOKEN = "8890338622:AAE2DhsEq6lkc86tFEca76YP22pCfoPkiAQ"
bot = telebot.TeleBot(TOKEN)

# --- ১০টি মেইন বাটন এবং প্রতিটিতে ১৫টি করে সাব-বাটন ---
# এখানে আমি ফরম্যাটটা একদম ক্লিয়ার করে দিলাম যাতে আপনার এডিট করতে সুবিধা হয়
MAIN_MENU_STRUCTURE = {
    "Category 1": [("App 1", "https://link.com"), ("App 2", "https://link.com"), ("App 3", "https://link.com"), ("App 4", "https://link.com"), ("App 5", "https://link.com"), ("App 6", "https://link.com"), ("App 7", "https://link.com"), ("App 8", "https://link.com"), ("App 9", "https://link.com"), ("App 10", "https://link.com"), ("App 11", "https://link.com"), ("App 12", "https://link.com"), ("App 13", "https://link.com"), ("App 14", "https://link.com"), ("App 15", "https://link.com")],
    "Category 2": [("App 1", "https://link.com"), ("App 2", "https://link.com"), ("App 3", "https://link.com"), ("App 4", "https://link.com"), ("App 5", "https://link.com"), ("App 6", "https://link.com"), ("App 7", "https://link.com"), ("App 8", "https://link.com"), ("App 9", "https://link.com"), ("App 10", "https://link.com"), ("App 11", "https://link.com"), ("App 12", "https://link.com"), ("App 13", "https://link.com"), ("App 14", "https://link.com"), ("App 15", "https://link.com")],
    "Category 3": [("App 1", "https://link.com"), ("App 2", "https://link.com"), ("App 3", "https://link.com"), ("App 4", "https://link.com"), ("App 5", "https://link.com"), ("App 6", "https://link.com"), ("App 7", "https://link.com"), ("App 8", "https://link.com"), ("App 9", "https://link.com"), ("App 10", "https://link.com"), ("App 11", "https://link.com"), ("App 12", "https://link.com"), ("App 13", "https://link.com"), ("App 14", "https://link.com"), ("App 15", "https://link.com")],
    "Category 4": [("App 1", "https://link.com"), ("App 2", "https://link.com"), ("App 3", "https://link.com"), ("App 4", "https://link.com"), ("App 5", "https://link.com"), ("App 6", "https://link.com"), ("App 7", "https://link.com"), ("App 8", "https://link.com"), ("App 9", "https://link.com"), ("App 10", "https://link.com"), ("App 11", "https://link.com"), ("App 12", "https://link.com"), ("App 13", "https://link.com"), ("App 14", "https://link.com"), ("App 15", "https://link.com")],
    "Category 5": [("App 1", "https://link.com"), ("App 2", "https://link.com"), ("App 3", "https://link.com"), ("App 4", "https://link.com"), ("App 5", "https://link.com"), ("App 6", "https://link.com"), ("App 7", "https://link.com"), ("App 8", "https://link.com"), ("App 9", "https://link.com"), ("App 10", "https://link.com"), ("App 11", "https://link.com"), ("App 12", "https://link.com"), ("App 13", "https://link.com"), ("App 14", "https://link.com"), ("App 15", "https://link.com")],
    "Category 6": [("App 1", "https://link.com"), ("App 2", "https://link.com"), ("App 3", "https://link.com"), ("App 4", "https://link.com"), ("App 5", "https://link.com"), ("App 6", "https://link.com"), ("App 7", "https://link.com"), ("App 8", "https://link.com"), ("App 9", "https://link.com"), ("App 10", "https://link.com"), ("App 11", "https://link.com"), ("App 12", "https://link.com"), ("App 13", "https://link.com"), ("App 14", "https://link.com"), ("App 15", "https://link.com")],
    "Category 7": [("App 1", "https://link.com"), ("App 2", "https://link.com"), ("App 3", "https://link.com"), ("App 4", "https://link.com"), ("App 5", "https://link.com"), ("App 6", "https://link.com"), ("App 7", "https://link.com"), ("App 8", "https://link.com"), ("App 9", "https://link.com"), ("App 10", "https://link.com"), ("App 11", "https://link.com"), ("App 12", "https://link.com"), ("App 13", "https://link.com"), ("App 14", "https://link.com"), ("App 15", "https://link.com")],
    "Category 8": [("App 1", "https://link.com"), ("App 2", "https://link.com"), ("App 3", "https://link.com"), ("App 4", "https://link.com"), ("App 5", "https://link.com"), ("App 6", "https://link.com"), ("App 7", "https://link.com"), ("App 8", "https://link.com"), ("App 9", "https://link.com"), ("App 10", "https://link.com"), ("App 11", "https://link.com"), ("App 12", "https://link.com"), ("App 13", "https://link.com"), ("App 14", "https://link.com"), ("App 15", "https://link.com")],
    "Category 9": [("App 1", "https://link.com"), ("App 2", "https://link.com"), ("App 3", "https://link.com"), ("App 4", "https://link.com"), ("App 5", "https://link.com"), ("App 6", "https://link.com"), ("App 7", "https://link.com"), ("App 8", "https://link.com"), ("App 9", "https://link.com"), ("App 10", "https://link.com"), ("App 11", "https://link.com"), ("App 12", "https://link.com"), ("App 13", "https://link.com"), ("App 14", "https://link.com"), ("App 15", "https://link.com")],
    "Category 10": [("App 1", "https://link.com"), ("App 2", "https://link.com"), ("App 3", "https://link.com"), ("App 4", "https://link.com"), ("App 5", "https://link.com"), ("App 6", "https://link.com"), ("App 7", "https://link.com"), ("App 8", "https://link.com"), ("App 9", "https://link.com"), ("App 10", "https://link.com"), ("App 11", "https://link.com"), ("App 12", "https://link.com"), ("App 13", "https://link.com"), ("App 14", "https://link.com"), ("App 15", "https://link.com")]
}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = InlineKeyboardMarkup(row_width=2)
    buttons = [InlineKeyboardButton(cat, callback_data=f"cat_{cat}") for cat in MAIN_MENU_STRUCTURE.keys()]
    markup.add(*buttons)
    bot.send_message(message.chat.id, "🤖 মেনু সিলেক্ট করুন:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data.startswith("cat_"):
        category = call.data.split("_", 1)[1]
        markup = InlineKeyboardMarkup(row_width=2)
        buttons = [InlineKeyboardButton(name, web_app=WebAppInfo(url=url)) for name, url in MAIN_MENU_STRUCTURE[category]]
        markup.add(*buttons)
        markup.add(InlineKeyboardButton("« Back to Menu", callback_data="back_main"))
        bot.edit_message_text(f"📱 {category} এর অ্যাপস:", call.message.chat.id, call.message.message_id, reply_markup=markup)
    
    elif call.data == "back_main":
        markup = InlineKeyboardMarkup(row_width=2)
        buttons = [InlineKeyboardButton(cat, callback_data=f"cat_{cat}") for cat in MAIN_MENU_STRUCTURE.keys()]
        markup.add(*buttons)
        bot.edit_message_text("🤖 মেনু সিলেক্ট করুন:", call.message.chat.id, call.message.message_id, reply_markup=markup)

if __name__ == "__main__":
    bot.infinity_polling()
