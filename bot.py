import logging, html, json, traceback, datetime, os
from telegram import ForceReply, Update
from telegram.constants import ParseMode
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters, CallbackContext
from dotenv import load_dotenv
from modules import all_handlers
load_dotenv()

token = os.environ.get('BOT_TOKEN')
chat_id = os.environ.get('DEVELOPER_CHAT_ID')

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    chat_id = update.effective_chat.id
    await update.message.reply_html(
        rf"Hi {user.mention_html()}! I'm here to help with your calculations. Just send me the numbers and operators, and I'll do the math for you. Need assistance? Just click /help.",
        reply_markup=ForceReply(selective=True),
    )
    await context.bot.send_message(
        chat_id=chat_id, text= f"✅ A person has started the bot!\n\n🪪 Name: {user.mention_html()}\n🆔 ChatID: {chat_id}\n📅 Date&Time: {datetime.datetime.now()}", parse_mode=ParseMode.HTML
    )

async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.error("Exception while handling an update:", exc_info=context.error)

    tb_list = traceback.format_exception(None, context.error, context.error.__traceback__)
    tb_string = "".join(tb_list)

    update_str = update.to_dict() if isinstance(update, Update) else str(update)
    message = (
        f"An exception was raised while handling an update\n"
        f"<pre>update = {html.escape(json.dumps(update_str, indent=2, ensure_ascii=False))}"
        "</pre>\n\n"
        f"<pre>context.chat_data = {html.escape(str(context.chat_data))}</pre>\n\n"
        f"<pre>context.user_data = {html.escape(str(context.user_data))}</pre>\n\n"
        f"<pre>{html.escape(tb_string)}</pre>"
    )

    await context.bot.send_message(
        chat_id=chat_id, text=message, parse_mode=ParseMode.HTML
    )

def main() -> None:
    application = Application.builder().token(token).build()

    for handler in all_handlers:
        if len(handler) == 2:
            application.add_handler(
                handler[0],
                handler[1]
            )
        else:
            application.add_handler(
                handler[0]
            )

    application.add_handler(CommandHandler("start", start))
    application.add_error_handler(error_handler)
    application.run_polling()


if __name__ == "__main__":
    main()