from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes
import random
CATOKEN = ["eyydybewubjkw", "enjineindin", "sbbs2wbs2u"]
WEBSITE = ["http://site.mtl", "http://site.comomtl"]
TELEGRAM = ["http://tme.mtl", "http://tme.comomtl"]

ca_placeholder = random.choice(CATOKEN)
website_placeholder = random.choice(WEBSITE)
telegram_placeholder = random.choice(TELEGRAM)

async def start(update : Update, context : ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello, im your bot. Type /ca, /website or /telegram for more information.")

async def ca(update : Update, context : ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"{ca_placeholder}")

async def website(update : Update, context : ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"{website_placeholder}")

async def telegram(update : Update, context : ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"{telegram_placeholder}")


app = ApplicationBuilder().token("7816623591:AAF2bCO47mGonxjUyXUJrsbUmhaMnQHHlQI").build()
start_handler = CommandHandler("start",start)
ca_handler= CommandHandler("ca", ca)
website_handler = CommandHandler("website", website)
telegram_handler = CommandHandler("telegram", telegram)

app.add_handler(start_handler)
app.add_handler(ca_handler)
app.add_handler(website_handler)
app.add_handler(telegram_handler)

app.run_polling()