
import telebot

# =========================
# BOT SETTINGS
# =========================
BOT_TOKEN = "8881095610:AAEms6MCdKAHLEcNnJc5_HIjDuGBMJ4k3fg"

bot = telebot.TeleBot(BOT_TOKEN)


# =========================
# COMMANDS AND LINKS
# নতুন কমান্ড যোগ করতে এই অংশে লিখবে
# =========================
COMMANDS = {
    "69blu": {
        "link": ""
    },
    "96rad": {
        "link": "https://t.me/blugay69"
    },
    "fb7yt": {
        "link": "https://t.me/hotandgoot"
    },
    "fb7fc": {
        "link": ""
    },
    "ffuid": {
        "link": "6645547609"
    },
    "Pubguid": {
        "link": ""
    },
    "fb7tg": {
        "link": "https://t.me/fv7channel"
    },
    "lovelo": {
        "link": "https://t.me/lovelo888"
    },
    "ew": {
        "link": ""
    }
}


# =========================
# START COMMAND
# =========================
@bot.message_handler(commands=["start"])
def start_command(message):
    bot.reply_to(
        message,
        "WELCOME TO THE TUTU DRESS WORLD"
    )


# =========================
# OTHER COMMANDS
# =========================
@bot.message_handler(
    func=lambda message: message.text is not None
    and message.text.startswith("/")
)
def handle_commands(message):
    command = message.text.split()[0]
    command = command.split("@")[0][1:].lower()

    # Match command names without case sensitivity
    matched_command = next(
        (name for name in COMMANDS if name.lower() == command),
        None
    )

    if matched_command is None:
        return

    link = COMMANDS[matched_command]["link"]

    if not link:
        bot.reply_to(
            message,
            "This link has not been added yet."
        )
        return

    bot.reply_to(
        message,
        f"{link}\n\nThank You!"
    )


# =========================
# RUN BOT
# =========================
if __name__ == "__main__":
    print("TUTU DRESS BOT IS RUNNING...")
    bot.infinity_polling()
