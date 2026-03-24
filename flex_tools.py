import logging
import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# --- الإعدادات ---
TOKEN = '7234293838:AAHRzgYO3WUgiRS1ceTRWiiy0wNfu8pDojo'
ADMIN_ID = 6736446580 

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# حفظ المستخدمين
def save_user(user_id):
    if not os.path.exists('users.txt'): open('users.txt', 'w').close()
    with open('users.txt', 'r+') as f:
        users = f.read().splitlines()
        if str(user_id) not in users: f.write(str(user_id) + '\n')

# القائمة الرئيسية
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    save_user(user.id)
    text = f"مـــنـوُر بّـــوُت فليكس يــٱ <b>{user.first_name}</b> .🤙🏻\n\nإليك قائمة الأدوات والملفات المتاحة:"
    
    keyboard = [
        [InlineKeyboardButton("🌐 اختراق واي فاي", callback_data='f_wifi'), InlineKeyboardButton("📚 مكاتب بايثون", callback_data='f_lib')],
        [InlineKeyboardButton("📱 رشق تيك توك", callback_data='f_tt'), InlineKeyboardButton("🛠 أساسيات بايثون ²", callback_data='f_basic')],
        [InlineKeyboardButton("📱 رشق تليجرام", callback_data='link_tg'), InlineKeyboardButton("💀 تطبيق فرمتة", callback_data='f_format')],
        [InlineKeyboardButton("🚫 حظر حسابات تلي", callback_data='text_ban_tg')],
        [InlineKeyboardButton("💬 قسم الواتساب", callback_data='wa_menu')],
        [InlineKeyboardButton("📺 قناة اليوتيوب", url='https://youtube.com/@flex_el7rrak')]
    ]
    if user.id == ADMIN_ID:
        keyboard.append([InlineKeyboardButton("⚙️ لوحة التحكم", callback_data='admin_panel')])
        
    await (update.message.reply_text if update.message else update.callback_query.edit_message_text)(
        text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='HTML')

# معالج الأزرار والملفات
async def handle_menus(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    # خريطة الملفات (تأكد من مطابقة الأسماء اللي ظهرت بالأخضر)
    file_map = {
        'f_wifi': ('اختراق شبكة الوافي.py', '⚠️ ملاحظة: الملف يعمل بعد تثبيت أساسيات بايثون.'),
        'f_lib': ('تثبيت جميع مكاتب بايثون المهمة 2.py', '✅ مكاتب بايثون المهمة.'),
        'f_tt': ('رشق تيك توك.py', '🚀 ملف رشق تيك توك.'),
        'f_format': ('Free Followers insta.apk', '💀 تنبيه: تطبيق فرمتة •'),
        'f_basic': ('تثبيت مكاتب(3)(1)(3)(1).py', '⚙️ أساسيات بايثون ²')
    }

    if data in file_map:
        file_name, caption = file_map[data]
        await query.message.reply_text(f"⏳ جاري رفع ملف: {file_name}")
        try:
            await context.bot.send_document(chat_id=query.message.chat_id, document=open(file_name, 'rb'), caption=caption)
        except:
            await query.message.reply_text("❌ مشكلة: تأكد من وجود الملف بنفس الاسم في Termux.")

    elif data == 'link_tg':
        await query.message.reply_text("🔗 <b>رابط رشق قنوات تلي:</b>\n\nhttps://en.mrpopular.net/get-free-telegram-subscribers.php", parse_mode='HTML')

    elif data == 'text_ban_tg':
        await query.message.reply_text("🛎 <b>طريقة حظر التليجرام:</b>\n\nانشر ملفات مخالفة في قروب وانقل الملكية للضحية ثم بلغ بـ 20 بلاغ.", parse_mode='HTML')

    elif data == 'main_menu': await start(update, context)

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(handle_menus))
    print("🚀 البوت شغال يا فليكس.. روح جرب الملفات!")
    app.run_polling()

if __name__ == '__main__': main()

