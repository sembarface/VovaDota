import requests
from bs4 import BeautifulSoup
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from datetime import datetime, timezone

# Вставьте ваш токен и Telegram API ID/Hash
BOT_TOKEN = "7552772723:AAFRE4eP7wD9zXDpJ7vRZqAzXX60pab4imI"

# Заданные URL для разных пользователей
DOTA_PROFILE_URLS = {
    "vova": "https://ru.dotabuff.com/players/853246304",  
    "denis": "https://ru.dotabuff.com/players/120268281", 
    "robert": "https://ru.dotabuff.com/players/223768611",
    "gena": "https://ru.dotabuff.com/players/248595717",
    "anya":"https://ru.dotabuff.com/players/431947539",
    "yarik":"https://ru.dotabuff.com/players/462089642",



    "вова": "https://ru.dotabuff.com/players/853246304", 
    "денис": "https://ru.dotabuff.com/players/120268281", 
    "роберт": "https://ru.dotabuff.com/players/223768611",
    "гена": "https://ru.dotabuff.com/players/248595717",
    "аня":"https://ru.dotabuff.com/players/431947539",
    "ярик":"https://ru.dotabuff.com/players/462089642",


    "miracle":"https://ru.dotabuff.com/esports/players/105248644-miracle",
    "topson":"https://ru.dotabuff.com/esports/players/94054712-topson",
    "sumail":"https://ru.dotabuff.com/esports/players/111620041-aster-suma1l",
    "ATF": "https://ru.dotabuff.com/esports/players/183719386-ammar_the_f",
    "daxak":"https://ru.dotabuff.com/esports/players/177411785-daxak",
    "ramzes666":"https://ru.dotabuff.com/esports/players/132851371-9pandas-ramzes666",
    "skiter":"https://ru.dotabuff.com/esports/players/100058342-skiter",
    "iltw":"https://ru.dotabuff.com/players/113995822",
    "andreyimersion":"https://ru.dotabuff.com/players/86853590"

}

async def fetch_last_game_time(DOTA_PROFILE_URL):
    """Получает дату последней игры с Dotabuff."""
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(DOTA_PROFILE_URL, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    time_tag = soup.find('time')
    if time_tag:
        return time_tag['datetime']
    return None


async def calculate_time_difference(last_game_time):
    """Рассчитывает разницу времени от последней игры."""
    now = datetime.now(timezone.utc)  # Установим UTC для "сейчас"
    last_game = datetime.fromisoformat(last_game_time).astimezone(timezone.utc)  # Переведём в UTC
    diff = now - last_game
    if diff.days > 0:
        return f"{diff.days} дней назад"
    hours = diff.seconds // 3600
    if hours > 0:
        return f"{hours} часов назад"
    minutes = (diff.seconds % 3600) // 60
    return f"{minutes} минут назад"


async def update_status_vova(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Команда для получения статуса Вовы."""
    try:
        DOTA_PROFILE_URL = DOTA_PROFILE_URLS["vova"]
        
        # Получаем дату последней игры
        last_game_time = await fetch_last_game_time(DOTA_PROFILE_URL)
        if not last_game_time:
            await update.message.reply_text("Не удалось получить информацию с Dotabuff.")
            return
        
        # Рассчитываем разницу времени
        time_since_last_game = await calculate_time_difference(last_game_time)
        
        # Отправляем статус
        status_text = f"Вова последний раз играл в доту {time_since_last_game}"
        await update.message.reply_text(status_text)

    except Exception as e:
        await update.message.reply_text(f"Произошла ошибка: {e}")

async def update_status_robert(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        DOTA_PROFILE_URL = DOTA_PROFILE_URLS["robert"]
        
        # Получаем дату последней игры
        last_game_time = await fetch_last_game_time(DOTA_PROFILE_URL)
        if not last_game_time:
            await update.message.reply_text("Не удалось получить информацию с Dotabuff.")
            return
        
        # Рассчитываем разницу времени
        time_since_last_game = await calculate_time_difference(last_game_time)
        
        # Отправляем статус
        status_text = f"Роберт последний раз играл в доту {time_since_last_game}"
        await update.message.reply_text(status_text)

    except Exception as e:
        await update.message.reply_text(f"Произошла ошибка: {e}")

async def update_status_denis(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Команда для получения статуса Дениса."""
    try:
        DOTA_PROFILE_URL = DOTA_PROFILE_URLS["denis"]
        
        # Получаем дату последней игры
        last_game_time = await fetch_last_game_time(DOTA_PROFILE_URL)
        if not last_game_time:
            await update.message.reply_text("Не удалось получить информацию с Dotabuff.")
            return
        
        # Рассчитываем разницу времени
        time_since_last_game = await calculate_time_difference(last_game_time)
        
        # Отправляем статус
        status_text = f"Денис последний раз играл в доту {time_since_last_game}"
        await update.message.reply_text(status_text)

    except Exception as e:
        await update.message.reply_text(f"Произошла ошибка: {e}")


async def update_status_gena(update: Update, context: ContextTypes.DEFAULT_TYPE):

    try:
        DOTA_PROFILE_URL = DOTA_PROFILE_URLS["gena"]
        
        # Получаем дату последней игры
        last_game_time = await fetch_last_game_time(DOTA_PROFILE_URL)
        if not last_game_time:
            await update.message.reply_text("Не удалось получить информацию с Dotabuff.")
            return
        
        # Рассчитываем разницу времени
        time_since_last_game = await calculate_time_difference(last_game_time)
        
        # Отправляем статус
        status_text = f"Гена последний раз играл в доту {time_since_last_game}"
        await update.message.reply_text(status_text)

    except Exception as e:
        await update.message.reply_text(f"Произошла ошибка: {e}")



async def update_status_anya(update: Update, context: ContextTypes.DEFAULT_TYPE):

    try:
        DOTA_PROFILE_URL = DOTA_PROFILE_URLS["anya"]
        
        # Получаем дату последней игры
        last_game_time = await fetch_last_game_time(DOTA_PROFILE_URL)
        if not last_game_time:
            await update.message.reply_text("Не удалось получить информацию с Dotabuff.")
            return
        
        # Рассчитываем разницу времени
        time_since_last_game = await calculate_time_difference(last_game_time)
        
        # Отправляем статус
        status_text = f"Аня последний раз играла в доту {time_since_last_game}"
        await update.message.reply_text(status_text)

    except Exception as e:
        await update.message.reply_text(f"Произошла ошибка: {e}")

async def update_status_yarik(update: Update, context: ContextTypes.DEFAULT_TYPE):

    try:
        DOTA_PROFILE_URL = DOTA_PROFILE_URLS["yarik"]
        
        # Получаем дату последней игры
        last_game_time = await fetch_last_game_time(DOTA_PROFILE_URL)
        if not last_game_time:
            await update.message.reply_text("Не удалось получить информацию с Dotabuff.")
            return
        
        # Рассчитываем разницу времени
        time_since_last_game = await calculate_time_difference(last_game_time)
        
        # Отправляем статус
        status_text = f"Ярик последний раз играл в доту {time_since_last_game}"
        await update.message.reply_text(status_text)

    except Exception as e:
        await update.message.reply_text(f"Произошла ошибка: {e}")


async def update_status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Команда для обновления статуса, принимает URL профиля как параметр."""
    try:
        # Получаем аргумент (имя пользователя), переданный в команду
        profile_key = context.args[0].lower() if context.args else None

        if not profile_key or profile_key not in DOTA_PROFILE_URLS:
            await update.message.reply_text("Не указан правильный пользователь или URL профиля.")
            return

        # Получаем URL профиля по ключу
        DOTA_PROFILE_URL = DOTA_PROFILE_URLS[profile_key]

        # Получаем дату последней игры
        last_game_time = await fetch_last_game_time(DOTA_PROFILE_URL)
        if not last_game_time:
            await update.message.reply_text("Не удалось получить информацию с Dotabuff.")
            return
        
        # Рассчитываем разницу времени
        time_since_last_game = await calculate_time_difference(last_game_time)
        
        # Отправляем статус
        status_text = f"{profile_key.capitalize()} последний раз играл в доту {time_since_last_game}"
        await update.message.reply_text(status_text)

    except Exception as e:
        await update.message.reply_text(f"Произошла ошибка: {e}")



async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Приветственное сообщение."""
    await update.message.reply_text(
        "Привет! Используйте /updateName чтобы узнать когда Вова и его друзья последний раз играли в доту"
    )


def main():
    """Запуск бота."""
    application = Application.builder().token(BOT_TOKEN).build()

    # Обработчики команд для различных пользователей
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("updatevova", update_status_vova))
    application.add_handler(CommandHandler("updatedenis", update_status_denis))
    application.add_handler(CommandHandler("updaterobert", update_status_robert))
    application.add_handler(CommandHandler("updategena", update_status_gena))
    application.add_handler(CommandHandler("updateanya", update_status_anya))
    application.add_handler(CommandHandler("updateyarik", update_status_yarik))
    application.add_handler(CommandHandler("update", update_status))
    
    # application.add_handler(CommandHandler("updateOther", update_status_other))

    application.run_polling()


if __name__ == "__main__":
    main()
