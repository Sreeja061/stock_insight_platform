import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from decouple import config
from core.utils import predict_stock

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Get the bot token from the .env file
TOKEN = config('TELEGRAM_BOT_TOKEN')

# /start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome to Stock Insight Bot!\n"
        "Use /predict <TICKER> to get a stock prediction.\n"
        "Example: /predict TSLA"
    )

# /predict <ticker> command handler
async def predict(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("⚠️ Please provide a stock ticker. Example: /predict TSLA")
        return

    ticker = context.args[0]
    try:
        result = predict_stock(ticker)
        reply = (
            f"📈 *Prediction for {ticker.upper()}*\n\n"
            f"🔮 Predicted Price: ₹{result['predicted_price']}\n"
            f"📊 Metrics:\n"
            f"- MSE: {result['metrics']['mse']}\n"
            f"- RMSE: {result['metrics']['rmse']}\n"
            f"- R²: {result['metrics']['r2']}"
        )
        await update.message.reply_text(reply, parse_mode="Markdown")
    except Exception as e:
        logger.error(e)
        await update.message.reply_text("❌ Failed to fetch prediction. Try again later.")

# Main app function
if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("predict", predict))

    print("🤖 Bot is running... (Press CTRL+C to stop)")
    app.run_polling()
