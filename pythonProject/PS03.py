import requests
from bs4 import BeautifulSoup
from googletrans import Translator
import asyncio



async def get_english_words():
    url = "http://randomword.com/"
    translator = Translator()

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        english_word = soup.find("div", id = "random_word").text.strip()
        ru_word = await translator.translate(english_word, src = "en", dest = "ru")
        word_definition = soup.find("div", id = "random_word_definition").text.strip()
        ru_definition = await translator.translate(word_definition, src = "en", dest = "ru")
        return {
            "word": english_word,
            "ru_word": ru_word.text,
            "definition": word_definition,
            "ru_definition": ru_definition.text
        }
    except Exception as e:
        print(f"A loading error occurred: {e}")
        return None


async def game_loop():
    print("Welcome to the game! You have got to guess the word using the definition!")

    while True:
        language = input("Which language do you prefer? (en/ru): ").lower()
        if language == "ru":
            definition = "ru_definition"
            word_key = "ru_word"
        else:
            definition = "definition"
            word_key = "word"

        words = await get_english_words()
        if not words:  # Если произошла ошибка, завершаем игру
            print("Failed to fetch word. Exiting the game.")
            break

        print(f"Definition: {words[definition]}")
        guess = input("Your guess word: ")
        if words[word_key].lower() == guess.lower():
            print("Correct!")
        else:
            print("Wrong. Try again.")
        mean = input("Do you want to play again? (y/no): ")
        if mean.lower() != "y":
            break

asyncio.run(game_loop())

