from telegram import Update
from telegram.ext import CommandHandler, CallbackContext

def mixs(num):
    try:
        ele = int(num)
        return (0, ele, '')
    except ValueError:
        return (1, num, '')

async def sort(update: Update, context: CallbackContext) -> None:
    input_mex = update.message.text
    input_args = input_mex.split('/sort ')[1]
    input_args = list(input_args.split(" ")) 
    input_args = list(filter(str.strip, input_args))
    foo = []
    for i in input_args:
        try:
            foo.append(int(i) if float(i).is_integer() else float(i))
        except ValueError:
            foo.append(i)
    foo.sort(key = mixs)
    await update.message.reply_text(f"The sorted version of the numbers provided is: {foo}")

__handlers__ = [
    [
        CommandHandler(
            "sort",
            sort
        )
    ]
]