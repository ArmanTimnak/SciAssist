from telegram import Update
from telegram.ext import CommandHandler, CallbackContext

def common_factors_calc(numbers):
    numbers.sort()
    if not numbers:
        return []
    
    factors = set()
    for i in range(1, numbers[0] + 1):
        if numbers[0] % i == 0:
            factors.add(i)
    
    for num in numbers[1:]:
        common_factors = set()
        for factor in factors:
            if num % factor == 0:
                common_factors.add(factor)
        factors = list(common_factors)
    factors.sort()
    factors = ", ".join(map(str, factors))
    return factors

async def common_factors(update: Update, context: CallbackContext) -> None:
    input_mex = update.message.text
    input_args = input_mex.split('/common_factors ')[1]
    input_args = list(input_args.split(" ")) 
    input_args = list(filter(str.strip, input_args))
    input_args = list(map(int, input_args))
    await update.message.reply_text(f"The common factors of the numbers provided is: {common_factors_calc(input_args)}")

__handlers__ = [
    [
        CommandHandler(
            "common_factors",
            common_factors
        )
    ]
]