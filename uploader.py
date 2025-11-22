import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

TOKEN = 'YOUR_ID_TOKEN' #замени на свой токен

SAVE_DIR = 'YOUR PATH TO THE DIRECTORY' # путь куда будет сохраняться файл

if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

TOKEN = 'YOUR_ID_TOKEN'  # замени на свой токен
SAVE_DIR = r'YOUR PATH TO THE DIRECTORY'  # путь куда будет сохраняться файл

if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Готов к команде')

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', start))

    app.run_polling()

async def save_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message

    # Обрабатываем документы
    if message.document:
        file = await message.document.get_file()
        filename = message.document.file_name
        filepath = os.path.join(SAVE_DIR, filename)
        await file.download_to_drive(custom_path=filepath)
        await message.reply_text(f'Файл сохранён: {filename}')
    elif message.photo:
        file = await message.photo[-1].get_file()
        filename = f'photo_{message.photo[-1].file_unique_id}.jpg'
        filepath = os.path.join(SAVE_DIR, filename)
        await file.download_to_drive(custom_path=filepath)
        await message.reply_text(f'Фото сохранено: {filename}')
    else:
        await message.reply_text('Пожалуйста, пришлите файл или фото.')

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.ALL & (~filters.StatusUpdate.ALL), save_file))
    app.run_polling()

if __name__ == '__main__':
    main()
