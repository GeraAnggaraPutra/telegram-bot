# from telegram.ext import Updater, CommandHandler, MessageHandler, filters

# def start(update, context):
#     update.message.reply_text("Hello! Welcome to the wakanda bot")
    
# def help(update,context):
#     update.message.reply_text("""
#     The following commands are avilable:
    
#     /start -> Welcome to the wakanda bot : )
#     /help -> This message
#     /content -> This is my telegram bot using python thank you for coming
#     /Weather  -> Check the weather
#     /Laravel -> My big project using laravel
#     /React -> The react movie trailer
#     /Portofolio -> This is my portofolio
#     /contact -> contact information 
#      """)
    
# def content(update, context):
#     update.message.reply_text("i have several project on my github : https://github.com/GeraAnggaraPutra")

# def Weather(update, context):
#     update.message.reply_text("demo link : https://geraanggaraputra.github.io/weather-app/")

# def Laravel(update, context):
#     update.message.reply_text("code link : https://github.com/GeraAnggaraPutra/Rental-Mobil")
    
# def React(update, context):
#     update.message.reply_text("demo link : https://geraanggaraputra.github.io/movie-trailer-app-react/")
    
# def Portofolio(update, context):
#     update.message.reply_text("demo link : https://geraanggaraputra.github.io/my-portofolio/")
    
# def contact(update, context):
#     update.message.reply_text("You can contact me on email anggaragera@gmail.com")

# def handle_message(update, context):
#     update.message.reply_text(f"You said {update.message.text}, use the commands using /")


# Token = "6061616888:AAG7v2Dy5ZoFezreZ9dmWOsYYXhy6WI5ZNc"
# updater = Updater("6061616888:AAG7v2Dy5ZoFezreZ9dmWOsYYXhy6WI5ZNc", use_context=True)
# disp = updater.dispatcher

# disp.add_handler(CommandHandler('start',start))
# disp.add_handler(CommandHandler('help',help))
# disp.add_handler(CommandHandler('content',content))
# disp.add_handler(CommandHandler('Weather',Weather))
# disp.add_handler(CommandHandler('Laravel',Laravel))
# disp.add_handler(CommandHandler('React',React))
# disp.add_handler(CommandHandler('Portofolio',Portofolio))
# disp.add_handler(CommandHandler('contact',contact))
# disp.add_handler(MessageHandler(filters.text, handle_message))
# updater.start_polling()
# updater.idle()

from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

print('Starting up bot...')

TOKEN: Final = '6061616888:AAG7v2Dy5ZoFezreZ9dmWOsYYXhy6WI5ZNc'
BOT_USERNAME: Final = '@Geratech_11_bot'


# Lets us use the /start command
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""Hello there! I\'m a Geratech bot. What\'s up? type /help to see all commads""")


# Lets us use the /help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""The following commands are avilable:
    
     /start -> Welcome to my bot
     /help -> This message
     /content -> This is my project
     /weather  -> Check the weather
     /laravel -> My laravel project
     /movie -> Watch movie trailer
     /portofolio -> This is my portofolio
     /contact -> contact information
     /chatapp -> This is fire chat app""")


# Lets us use the /custom command
async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is a custom command, you can add whatever text you want here.')


def handle_response(text: str) -> str:
    # Create your own response logic
    processed: str = text.lower()

    if 'hello' in processed:
        return 'Hey there!'

    if 'how are you' in processed:
        return 'I\'m good!'

    if 'content' in processed:
        return 'i have several project on my github : https://github.com/GeraAnggaraPutra'
    
    if 'weather' in processed:
        return 'check the weather here : https://geraanggaraputra.github.io/weather-app/'
    
    if 'laravel' in processed:
        return 'my laravel project link : https://github.com/GeraAnggaraPutra/Rental-Mobil'
    
    if 'movie' in processed:
        return 'watch movie trailer : https://geraanggaraputra.github.io/movie-trailer-app-react/'
    
    if 'portofolio' in processed:
        return 'my portofolio : https://geraanggaraputra.github.io/my-portofolio/'
    
    if 'contact' in processed:
        return 'you can contact me on email : anggaragera@gmail.com'
    
    if 'chatapp' in processed:
        return 'you must try this app : https://fire-chat-gera.netlify.app/'

    return 'I don\'t understand'


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Get basic info of the incoming message
    message_type: str = update.message.chat.type
    text: str = update.message.text

    # Print a log for debugging
    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    # React to group messages only if users mention the bot directly
    if message_type == 'group':
        # Replace with your bot username
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return  # We don't want the bot respond if it's not mentioned in the group
    else:
        response: str = handle_response(text)

    # Reply normal if the message is in private
    print('Bot:', response)
    await update.message.reply_text(response)


# Log errors
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


# Run the program
if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Log all errors
    app.add_error_handler(error)

    print('Polling...')
    # Run the bot
    app.run_polling(poll_interval=5)
