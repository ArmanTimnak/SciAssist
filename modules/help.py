from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Help!")

__handlers__ = [
    [
        CommandHandler(
            "help",
            help
        )
    ]
]