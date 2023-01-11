import telebot
import os as women
import requests
#from pytube import YouTube
import yt_dlp as youtube_dlp
from PIL import Image


#print('TOKEN:', TOKEN)
api_token = '5455229767:AAFq-tl0UkmbyFkw-lzPTYMQLWoS2MoLmUc'
bot = telebot.TeleBot(api_token)


@bot.message_handler(commands=['video'])
def test(message):
    link=message.text.split(" ")
    print(link[1])
    try:
        ydl_opts = {'outtmpl': 'user_req.%(ext)s'}
        ydl = youtube_dlp.YoutubeDL(ydl_opts)
        with ydl:
                 ydl.download([link[1]])
    except:
        print("An error has occurred")
    print("Download is completed successfully")
    #send video function
    chat_id=message.chat.id
    file_path = "user_req.mp4"
    bot.send_message(chat_id,"Sending videos...")
    bot.send_video(chat_id, video=open(file_path, 'rb'))
    women.remove(file_path)
    
   
@bot.message_handler(func=lambda message: True and message.text=='raja')
def echo_message(message):
    print(message)
    chat_id=message.chat.id
    message_text = message.text
    bot.send_message(chat_id, f"You said: {message_text}")
@bot.message_handler(func=lambda message: True and str(message.text).upper()=='SUBA')
def echo_message(message):
    chat_id=message.chat.id
    message_text = message.text
    bot.send_message(chat_id, "Suba Is Very Gud Girl💕")
@bot.message_handler(commands=['help'])
def test(message):
    req="""HEY do YOu NEED heLp 
    use "/video {link of your video}" To download video

    """
    chat_id=message.chat.id
    bot.send_message(chat_id, req)

@bot.message_handler(content_types=["photo"])
def handle_images(message):
    chat_id=message.chat.id
    file_id = message.photo[-1].file_id
    def download_image(file_id, api_token):
     url = f"https://api.telegram.org/bot{api_token}/getFile?file_id={file_id}"
     response = requests.get(url)
     file_path = response.json()["result"]["file_path"]
     url = f"https://api.telegram.org/file/bot{api_token}/{file_path}"
     response = requests.get(url)
     return response.content
    
    try:
        img_data = download_image(file_id, api_token)
        with open("image.jpg", "wb") as f:
         f.write(img_data)
         image = Image.open("image.jpg")
         image.save("image.pdf", "PDF" ,resolution = 100.0)
         try:
             with open('image.pdf', 'rb') as file:
                input_file = telebot.types.InputFile(file)
                bot.send_document(chat_id, document=input_file, caption='Here You Go!!')
                
                
         except Exception as e:
             print(f"An error ocurred when sending the PDF: {str(e)}")
        
               
        
    except:
     print("An error ocurred when downloading the image")
    women.remove('image.jpg')
    women.remove('image.pdf')
    

            
bot.polling()