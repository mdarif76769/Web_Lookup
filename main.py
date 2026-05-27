import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

TOKEN = "8890338622:AAE2DhsEq6lkc86tFEca76YP22pCfoPkiAQ"  # আপনার বটের টোকেন দিন
bot = telebot.TeleBot(TOKEN)

# আপনার লাইভ ওয়েব অ্যাপ লিঙ্ক (গিটহাব পেজ লিঙ্ক)
MINI_APP_URL = "https://mdarif76769.github.io/mdarif76769/"

def get_reply_keyboard():
    markup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn_search = KeyboardButton("🔍 Search Apps", web_app=WebAppInfo(url=https://mdarif76769.github.io/mdarif76769/))
    btn_all_app = KeyboardButton("📱 All Apps")
    markup.add(btn_search, btn_all_app)
    return markup

@bot.message_handler(commands=['start', 'menu'])
def send_welcome(message):
    bot.send_message(
        chat_id=message.chat.id, 
        text="🤖 *RS5_Apps_Store Engine Active!*\n\nমেনু কন্ট্রোল করতে নিচের বাটন ব্যবহার করুন।", 
        parse_mode="Markdown", 
        reply_markup=get_reply_keyboard()
    )

if __name__ == "__main__":
    bot.infinity_polling()
