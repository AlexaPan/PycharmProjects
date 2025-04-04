import telebot
import datetime
import random
import time
import threading
from openai import OpenAI
#from google.cloud import speech
import sounddevice as sd
import wave
from gtts import gTTS
import os
from langdetect import detect
from pydub import AudioSegment
import speech_recognition as sr
import logging
from dotenv import load_dotenv

load_dotenv()

#load token
api_key_env = os.environ.get("api_key")
TOKEN = os.environ.get("TOKEN_lang_bot")


#turn on logging
logging.basicConfig(filename='app.log',level=logging.INFO)
logger = logging.getLogger(__name__)
logging.info('Lang_bot started at %s', datetime.datetime.now())


# Инициализация клиента OpenAI
client = OpenAI(
    api_key=api_key_env,
    base_url="https://api.proxyapi.ru/openai/v1",
)

bot = telebot.TeleBot(TOKEN) #Import token


@bot.message_handler(commands=['start']) #Start command
def start_message(message):
    help_message(message)
#    bot.reply_to(message, f"Hello, {message.from_user.first_name}! I'm a bot that answers you with OpenAI. "
#                         f"You can ask me anything!")
    reminder_thread = threading.Thread(target=send_remainders, args=(message.chat.id,)) #Create thread
    reminder_thread.start() #Start thread
#    send_fact(message)  #Send fact message
#    user_language = 'English'  # или получайте язык от пользователя
#    task = generate_daily_task(user_language)
#    bot.send_message(message.chat.id, f'Here is your daily task:\n{task}')

@bot.message_handler(content_types=['voice']) #Voice command create wav-file from voice
def voice_handler(message):
#   bot.reply_to(message, "Thanks for voice message")
    voice_file = bot.get_file(message.voice.file_id)
    voice_data = bot.download_file(voice_file.file_path)

    #save voice data to file
    with open('voice.ogg', 'wb') as new_file:
        new_file.write(voice_data)

    #convert ogg to wav
    audio = AudioSegment.from_ogg('voice.ogg')
    audio.export('voice.wav', format='wav')


#recognize voice
    recognizer = sr.Recognizer()
    with sr.AudioFile('voice.wav') as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data, language='ru-RU')
            bot.reply_to(message, f'Вы сказали: {text}')
            message.text = text
            chat_with_ai(message)
        except sr.UnknownValueError:
            bot.reply_to(message, 'Не удалось распознать речь.')
        except sr.RequestError as e:
            bot.reply_to(message, f'Ошибка сервиса распознавания: {e}')

@bot.message_handler(commands=['help']) #Help command
def help_message(message):
    bot.reply_to(message, f"\nHello, {message.from_user.first_name}!\nI'm a bot that answers you with OpenAI.\n "
                          f"You can ask me anything in English and Russian\n!"
                          f"Also you can use /task command to get daily task for learning English\n"
                          f"And you can use /record command to record audio\n"
                          f"And you can use /fact command to get current time and receive facts about water\n"
                          f"And I will remind you to drink water at 9:00, 14:00 and 21:00\n"
                          f"I voice all messages from AI in English. This will help to learn the correct pronunciation "
                          f"of words, isn't it? You can use this bot to learn English\n"
                 f"\n\n Чтобы общаться с ИИ голосом запиши голосовое сообщение. Еще совет, перед диалогом с ИИ можешь дать ему установку, что он учитель английского"
                          f" и помогает в обучении и исправляет ошибки.")


@bot.message_handler(content_types=['audio'])
def handle_audio(message):
    bot.send_message(message.chat.id, f'Create audio file here')
    file_info = bot.get_file(message.audio.file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    with open("user_audio.wav", "wb") as new_file:
        new_file.write(downloaded_file)
        bot.send_message(message.chat.id, f'File created')

    #transcript = check_pronunciation("user_audio.wav")
    #bot.send_message(message.chat.id, f'You said: {transcript}')


@bot.message_handler(commands=["fact"])
def send_fact(message):
    bot.reply_to(message, f"The current time is {datetime.datetime.now().strftime("%H : %M")}")
    list_water = ["На самом деле, холодная вода почти всегда тяжелее теплой воды. "
                 "Это говорит о том, что если бы лед не плавал, реки и озера замерзли бы "
                 "по всему объему, что серьезно помешало бы рыбакам.",

                 "Молекулы воды прислушиваются к звукам. Они могут изменять свою"
                 " структуру под действием разной музыки!"
                 " Воображение сразу создает картину танцующих молекул в воде под музыку,"
                 " не правда ли?",

                 "Вода способна поглощать запахи очень сильно. Например, даже небольшое"
                 " количество рыбы в ведре с водой начнет заставлять весь дом пахнуть свежей уловом.",

                 "Вода течет и кругом и вверх. Всплеск в ванной - это не просто капельки, это небольшqй фонтанчик!"

                  "Атомы воды, которые вы пьете, могли быть частью динозавров или космических кораблей "
                  "(если верить в теорию о воде, доставленной на Землю метеоритами)."]


    random_choice_list= random.choice(list_water)
    bot.reply_to(message, f"Catch a fact about water: {random_choice_list}")

@bot.message_handler(commands=['record'])
def handle_record_command(message):
    # Запись аудио
    audio_file = "user_audio.wav"
    record_audio(message, audio_file)

    # there I should make a comment to this code
    # Проверка произношения
    # transcript = check_pronunciation(audio_file)
    # bot.send_message(message.chat.id, f'You said: {transcript}')

def send_remainders(chat_id):
    first_rem = "09:00"
    second_rem = "14:00"
    third_rem = "21:00"

    while True:
        if_now = datetime.datetime.now().strftime("%H:%M")
        if if_now == first_rem or if_now == second_rem or if_now == third_rem:
            bot.send_message(chat_id, "Do you remember: you need to drink water")
            time.sleep(61)
        time.sleep(5)


# Словарь для хранения сообщений чата для каждого пользователя
user_messages = {}

@bot.message_handler(func=lambda message: True)
def chat_with_ai(message):
    user_id = message.from_user.id

    # Получаем список сообщений для текущего пользователя или создаем новый
    if user_id not in user_messages:
        user_messages[user_id] = []

    # Добавляем сообщение пользователя в список сообщений
    user_messages[user_id].append({"role": "user", "content": message.text})

    # Отправляем запрос к нейросети
    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo-1106", messages=user_messages[user_id]
    )

    # Получаем ответ от нейросети
    assistant_response = chat_completion.choices[0].message.content

    # Отправляем ответ пользователю
    bot.reply_to(message, assistant_response)

    # Добавляем ответ нейросети в список сообщений
    user_messages[user_id].append({"role": "assistant", "content": assistant_response})
    user_messages[user_id].append({"role": "system", "content": "отвечай остроумно "
                                                                "в юмористическом стиле"})


    language_message = detect(assistant_response)
    # bot.reply_to(message, language_message)
    # if language_message == "en":

        # Преобразуем ответ в голосовое сообщение
    tts = gTTS(text=assistant_response, lang=language_message)  # Используем English
    audio_file = 'response.mp3'

    # Сохраняем аудиофайл
    tts.save(audio_file)

    # Отправляем голосовое сообщение пользователю
    with open(audio_file, 'rb') as audio:
        bot.send_voice(message.chat.id, audio)

    # Удаляем аудиофайл после отправки
    os.remove(audio_file)

def generate_daily_task(language):
    prompt = (f"Generate a daily language learning task for {language} "
              f"that includes vocabulary, grammar exercises, and an audio file suggestion.")

    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

#there I should make a comment to this function
# def check_pronunciation(audio_file):
#     client_speech= speech.SpeechClient()
#
#     with open(audio_file, "rb") as audio_file:
#         content = audio_file.read()
#
#     audio = speech.RecognitionAudio(content=content)
#     config = speech.RecognitionConfig(
#             encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
#             sample_rate_hertz=16000,
#             language_code="en-US",
#          )
#
#     response = client_speech.recognize(config=config, audio=audio)
#
#     for result in response.results:
#         print("Transcript: {}".format(result.alternatives[0].transcript))
#
#     if response.results:
#         return response.results[0].alternatives[0].transcript
#     else:
#         return "No speech detected"



def record_audio(message, filename, duration=5):
    bot.send_message(message.chat.id, f'Record started')
    # Запись аудио с микрофона
    fs = 16000  # Частота дискретизации
    print("Recording...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()  # Ждем завершения записи
    print("Recording finished.")
    bot.send_message(message.chat.id, f'Recording finished.')

    # Сохранение в файл
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)  # 2 байта для int16
        wf.setframerate(fs)
        wf.writeframes(audio.tobytes())



bot.polling(none_stop=True, interval=0)

