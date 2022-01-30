from pyrogram import filters, Client
from spam import bot

spammessage = '''
Hi, Welcome {}

Press >>
/vanitasalert 
/sibylalert
'''


@bot.on_message(filters.command(["start"], ['/', ".", "?"]))
async def start(client, message):
    await message.reply_text(spammessage.format(message.from_user.first_name))
