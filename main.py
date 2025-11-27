import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Токен беремо з змінної середовища TELEGRAM_BOT_TOKEN (на Railway задаєш у Variables)
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not TOKEN:
    raise RuntimeError("TELEGRAM_BOT_TOKEN is not set. Please add it in Railway → Variables.")

def start(update, context):
    text = (
        "Привіт! Я рахую спред і прибуток по крипті.\n\n"
        "Пиши мені повідомлення в такому форматі:\n"
        "% price1 price2 amount\n\n"
        "де:\n"
        "price1 – ціна на першій біржі (де купуєш)\n"
        "price2 – ціна на другій біржі (де продаєш)\n"
        "amount – кількість токенів\n\n"
        "Приклад:\n"
        "% 0.03198 0.0283 85200"
    )
    update.message.reply_text(text)

def calc_spread_and_profit(price1, price2, amount):
    # спред у відсотках
    spread_percent = (price2 - price1) / price1 * 100.0
    # прибуток у валюті ціни
    profit = (price2 - price1) * amount
    return spread_percent, profit

def handle_message(update, context):
    text = update.message.text.strip()

    # Працюємо тільки з повідомленнями, що починаються на "%"
    if not text.startswith("%"):
        return

    # Вирізаємо "%", замінюємо кому на крапку і ділимо рядок
    parts = text[1:].strip().replace(",", ".").split()

    if len(parts) != 3:
        update.message.reply_text(
            "Формат має бути:\n"
            "% price1 price2 amount\n"
            "Наприклад:\n"
            "% 0.03198 0.0283 85200"
        )
        return

    try:
        price1 = float(parts[0])
        price2 = float(parts[1])
        amount = float(parts[2])
    except ValueError:
        update.message.reply_text("Після % потрібно ввести три числа: price1 price2 amount.")
        return

    spread_percent, profit = calc_spread_and_profit(price1, price2, amount)

    msg = (
        f"{spread_percent:.2f}% – (спред)\n"
        f"{profit:.2f}$ – (прибуток)"
    )
    update.message.reply_text(msg)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # long polling – підходить для Railway[web:95]
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
