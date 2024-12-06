import requests
from bs4 import BeautifulSoup
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from datetime import datetime, timezone







# Вставьте ваш токен и Telegram API ID/Hash
BOT_TOKEN = "7552772723:AAFRE4eP7wD9zXDpJ7vRZqAzXX60pab4imI"
DOTA_PROFILE_URL = "https://ru.dotabuff.com/players/853246304"  # URL вашего профиля Dotabuff

async def fetch_last_game_time():
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

async def update_status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Команда для обновления статуса."""
    try:
        last_game_time = await fetch_last_game_time()
        if not last_game_time:
            await update.message.reply_text("Не удалось получить информацию с Dotabuff.")
            return
        time_since_last_game = await calculate_time_difference(last_game_time)
        status_text = f"Вова последний раз играл в доту {time_since_last_game}"
        await update.message.reply_text(status_text)

        # Обновление статуса в Telegram
        #await update_telegram_status(status_text)

    except Exception as e:
        await update.message.reply_text(f"Произошла ошибка: {e}")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Приветственное сообщение."""
    await update.message.reply_text("Привет! Используйте /update, чтобы узнать когда Вова в последний раз играть в доту")

def main():
    """Запуск бота."""
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("update", update_status))

    application.run_polling()

if __name__ == "__main__":
    main()
