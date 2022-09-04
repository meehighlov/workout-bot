from telegram.ext import ApplicationBuilder

from bot.config import cfg


app = ApplicationBuilder().token(cfg.WORKOUT_BOT_TOKEN).build()
