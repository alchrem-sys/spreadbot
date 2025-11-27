{\rtf1\ansi\ansicpg1251\cocoartf2867
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;\f1\fnil\fcharset0 LucidaGrande;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww28020\viewh17000\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import os\
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters\
\
# \uc0\u1058 \u1086 \u1082 \u1077 \u1085  \u1073 \u1077 \u1088 \u1077 \u1084 \u1086  \u1079  \u1079 \u1084 \u1110 \u1085 \u1085 \u1086 \u1111  \u1089 \u1077 \u1088 \u1077 \u1076 \u1086 \u1074 \u1080 \u1097 \u1072  TELEGRAM_BOT_TOKEN (\u1085 \u1072  Railway \u1079 \u1072 \u1076 \u1072 \u1108 \u1096  \u1091  Variables)\
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")\
\
if not TOKEN:\
    raise RuntimeError("TELEGRAM_BOT_TOKEN is not set. Please add it in Railway 
\f1 \uc0\u8594 
\f0  Variables.")\
\
def start(update, context):\
    text = (\
        "\uc0\u1055 \u1088 \u1080 \u1074 \u1110 \u1090 ! \u1071  \u1088 \u1072 \u1093 \u1091 \u1102  \u1087 \u1088 \u1080 \u1073 \u1091 \u1090 \u1086 \u1082  \u1110 \u1079  \u1089 \u1077 \u1088 \u1077 \u1076 \u1072 .\\n\\n\'bb\
        "\uc0\u1055 \u1080 \u1096 \u1080  \u1084 \u1077 \u1085 \u1110  \u1087 \u1086 \u1074 \u1110 \u1076 \u1086 \u1084 \u1083 \u1077 \u1085 \u1085 \u1103  \u1074  \u1090 \u1072 \u1082 \u1086 \u1084 \u1091  \u1092 \u1086 \u1088 \u1084 \u1072 \u1090 \u1110 :\\n"\
        "% price1 price2 amount\\n\\n"\
        "\uc0\u1076 \u1077 :\\n"\
        "price1 \'96 \uc0\u1094 \u1110 \u1085 \u1072  \u1085 \u1072  \u1087 \u1077 \u1088 \u1096 \u1110 \u1081  \u1073 \u1110 \u1088 \u1078 \u1110  (\u1076 \u1077  \u1082 \u1091 \u1087 \u1091 \u1108 \u1096 )\\n"\
        "price2 \'96 \uc0\u1094 \u1110 \u1085 \u1072  \u1085 \u1072  \u1076 \u1088 \u1091 \u1075 \u1110 \u1081  \u1073 \u1110 \u1088 \u1078 \u1110  (\u1076 \u1077  \u1087 \u1088 \u1086 \u1076 \u1072 \u1108 \u1096 )\\n"\
        "amount \'96 \uc0\u1082 \u1110 \u1083 \u1100 \u1082 \u1110 \u1089 \u1090 \u1100  \u1090 \u1086 \u1082 \u1077 \u1085 \u1110 \u1074 \\n\\n"\
        "\uc0\u1055 \u1088 \u1080 \u1082 \u1083 \u1072 \u1076 :\\n"\
        "% 0.03198 0.0283 85200"\
    )\
    update.message.reply_text(text)\
\
def calc_spread_and_profit(price1, price2, amount):\
    # \uc0\u1089 \u1087 \u1088 \u1077 \u1076  \u1091  \u1074 \u1110 \u1076 \u1089 \u1086 \u1090 \u1082 \u1072 \u1093 \
    spread_percent = (price2 - price1) / price1 * 100.0\
    # \uc0\u1087 \u1088 \u1080 \u1073 \u1091 \u1090 \u1086 \u1082  \u1091  \u1074 \u1072 \u1083 \u1102 \u1090 \u1110  \u1094 \u1110 \u1085 \u1080 \
    profit = (price2 - price1) * amount\
    return spread_percent, profit\
\
def handle_message(update, context):\
    text = update.message.text.strip()\
\
    # \uc0\u1055 \u1088 \u1072 \u1094 \u1102 \u1108 \u1084 \u1086  \u1090 \u1110 \u1083 \u1100 \u1082 \u1080  \u1079  \u1087 \u1086 \u1074 \u1110 \u1076 \u1086 \u1084 \u1083 \u1077 \u1085 \u1085 \u1103 \u1084 \u1080 , \u1097 \u1086  \u1087 \u1086 \u1095 \u1080 \u1085 \u1072 \u1102 \u1090 \u1100 \u1089 \u1103  \u1085 \u1072  "%"\
    if not text.startswith("%"):\
        return\
\
    # \uc0\u1042 \u1080 \u1088 \u1110 \u1079 \u1072 \u1108 \u1084 \u1086  "%", \u1079 \u1072 \u1084 \u1110 \u1085 \u1102 \u1108 \u1084 \u1086  \u1082 \u1086 \u1084 \u1091  \u1085 \u1072  \u1082 \u1088 \u1072 \u1087 \u1082 \u1091  \u1110  \u1076 \u1110 \u1083 \u1080 \u1084 \u1086  \u1088 \u1103 \u1076 \u1086 \u1082 \
    parts = text[1:].strip().replace(",", ".").split()\
\
    if len(parts) != 3:\
        update.message.reply_text(\
            "\uc0\u1060 \u1086 \u1088 \u1084 \u1072 \u1090  \u1084 \u1072 \u1108  \u1073 \u1091 \u1090 \u1080 :\\n"\
            "% price1 price2 amount\\n"\
            "\uc0\u1053 \u1072 \u1087 \u1088 \u1080 \u1082 \u1083 \u1072 \u1076 :\\n"\
            "% 0.03198 0.0283 85200"\
        )\
        return\
\
    try:\
        price1 = float(parts[0])\
        price2 = float(parts[1])\
        amount = float(parts[2])\
    except ValueError:\
        update.message.reply_text("\uc0\u1055 \u1110 \u1089 \u1083 \u1103  % \u1087 \u1086 \u1090 \u1088 \u1110 \u1073 \u1085 \u1086  \u1074 \u1074 \u1077 \u1089 \u1090 \u1080  \u1090 \u1088 \u1080  \u1095 \u1080 \u1089 \u1083 \u1072 : price1 price2 amount.")\
        return\
\
    spread_percent, profit = calc_spread_and_profit(price1, price2, amount)\
\
    msg = (\
        f"\{spread_percent:.2f\}% \'96 (\uc0\u1089 \u1087 \u1088 \u1077 \u1076 )\\n"\
        f"\{profit:.2f\}$ \'96 (\uc0\u1087 \u1088 \u1080 \u1073 \u1091 \u1090 \u1086 \u1082 )"\
    )\
    update.message.reply_text(msg)\
\
def main():\
    updater = Updater(TOKEN, use_context=True)\
    dp = updater.dispatcher\
\
    dp.add_handler(CommandHandler("start", start))\
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))\
\
    # long polling \'96 \uc0\u1087 \u1110 \u1076 \u1093 \u1086 \u1076 \u1080 \u1090 \u1100  \u1076 \u1083 \u1103  Railway[web:95]\
    updater.start_polling()\
    updater.idle()\
\
if __name__ == "__main__":\
    main()\
}