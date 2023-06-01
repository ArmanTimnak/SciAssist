import math
from telegram import Update
from telegram.ext import CommandHandler, CallbackContext

def gcf_calc(numbers):
    gcd_result = numbers[0]
    for i in range(1, len(numbers)):
        gcd_result = math.gcd(gcd_result, numbers[i])
    return gcd_result

async def gcf(update: Update, context: CallbackContext) -> None:
    input_mex = update.message.text
    input_args = input_mex.split('/gcd ')[1]
    input_args = list(input_args.split(" ")) 
    input_args = list(filter(str.strip, input_args))
    input_args = list(map(int, input_args))
    await update.message.reply_text(f"The gcd of the numbers provided is: {gcf_calc(input_args)}")

__handlers__ = [
    [
        CommandHandler(
            "gcf",
            gcf
        )
    ]
]