import os, asyncio, logging
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.types import FSInputFile
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import Command  # Новый импорт!
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

dp = Dispatcher(storage=MemoryStorage())
bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)

# ===== HANDLERS =====
@dp.message(Command("start"))
async def start(message: types.Message):
    text = (
        "🎶 Привет!\n"
        "Я превращаю ваши стихи в песню за 24 ч или делаю клип за 7 дней.\n"
        "Нажмите:\n"
        "• /song — заказать трек\n"
        "• /clip — заказать клип"
    )
    await message.answer(text)

@dp.message(Command("song"))
async def order_song(message: types.Message):
    await message.answer(
        "Отправьте текст песни + пожелания (жанр, настроение).\n"
        "Я пришлю минутный демо-фрагмент бесплатно!"
    )

@dp.message(Command("clip"))
async def order_clip(message: types.Message):
    await message.answer(
        "Пришлите готовый трек или ссылку, расскажите идею клипа.\n"
        "Через сутки получите 20-сек. превью!"
    )

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())