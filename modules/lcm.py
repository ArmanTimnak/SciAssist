import math
from telegram import Update
from telegram.ext import CommandHandler, CallbackContext

def lcm_calc(numbers):
    lcm_result = numbers[0]
    for i in range(1, len(numbers)):
        lcm_result = lcm_result * numbers[i] // math.gcd(lcm_result, numbers[i])
    return lcm_result

async def lcm(update: Update, context: CallbackContext) -> None:
    input_mex = update.message.text
    input_args = input_mex.split('/lcm ')[1]
    input_args = list(input_args.split(" ")) 
    input_args = list(filter(str.strip, input_args))
    input_args = list(map(int, input_args))
    await update.message.reply_text(f"The lcm of the numbers provided is: {lcm_calc(input_args)}")

__handlers__ = [
    [
        CommandHandler(
            "lcm",
            lcm
        )
    ]
]