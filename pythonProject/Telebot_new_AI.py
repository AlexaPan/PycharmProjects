import os
from dotenv import load_dotenv

import telebot
from openai import OpenAI

load_dotenv()

api_key_env = os.environ.get("api_key")
TOKEN = os.environ.get("TOKEN")
print(TOKEN)

# Инициализация клиента OpenAI
client = OpenAI(
    api_key=api_key_env,
    base_url="https://api.proxyapi.ru/openai/v1",
)

# Инициализация бота
bot = telebot.TeleBot(TOKEN)

# Словарь для хранения сообщений чата для каждого пользователя
user_messages = {}

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот, который отвечает на ваши"
                          " вопросы с помощью нейросети. Просто напишите свой вопрос!")

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
    user_messages[user_id].append({"role": "system", "content": "отвечай остроумно в юмористическом стиле"})

if __name__ == "__main__":
    bot.polling(none_stop=True)