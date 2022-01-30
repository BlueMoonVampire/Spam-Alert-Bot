from pyrogram import filters
from spam.helper import vanitas, is_alertvanitas
from spam.modules.spam import is_admin, kick_callback, ban_callback, mute_callback, call_back_filter
from spam import bot
from time import time
from pyrogram.types import ChatPermissions
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.types import Message
from spam import db

v = vanitas()


@bot.on_message(
    filters.command("vanitasalert", prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def vanitasalert(_, message):
    if is_admin(message.chat.id, message.from_user.id):
        return
    if is_vanitas := db.is_vanitas(message.chat.id):
        db.rm_vanitas(message.chat.id)
        await message.reply_text("Alert Mode Disable")
    else:
        db.set_vanitas(message.chat.id)
        await message.reply_text("Alert Mode Enable")


@bot.on_message(filters.new_chat_members)
def valert(_, m: Message):
    user = m.from_user.id
    is_vanitas = db.is_vanitas(m.chat.id)
    if not is_vanitas:
        return
    if is_alertvanitas(user):
        x = v.get_info(user)
        bot.send_message(
            m.chat.id,
            f"""
#ALERT
**This User Is Blacklisted**
**USER** : [{user}](tg://user?id={user})
**REASON** : {x.reason}
**ENFORCER** : [{x.enforcer}](tg://user?id={x.enforcer})""",
            reply_markup=InlineKeyboardMarkup([
                [
                    InlineKeyboardButton("Ban",
                                         callback_data=f"ban:ban:{user}"),
                    InlineKeyboardButton("Kick",
                                         callback_data=f"kick:kick:{user}"),
                    InlineKeyboardButton("Mute",
                                         callback_data=f"mute:mute:{user}")
                ],
            ]))
