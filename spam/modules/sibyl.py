from pyrogram import filters
from spam.helper import sibyl, is_alertsibyl
from spam.modules.spam import is_admin, kick_callback, ban_callback, mute_callback, call_back_filter
from spam import bot
from time import time
from pyrogram.types import ChatPermissions
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.types import Message
from spam import db

s = sibyl()


@bot.on_message(
    filters.command("sibylalert", prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def sibylalert(_, message):
    if is_admin(message.chat.id, message.from_user.id):
        return
    if is_sibyl := db.is_sibyl(message.chat.id):
        db.rm_sibyl(message.chat.id)
        await message.reply_text("Sibyl Alert Disable")
    else:
        db.set_sibyl(message.chat.id)
        await message.reply_text("Sibyl Alert Enable")


@bot.on_message(filters.new_chat_members)
def salert(_, m: Message):
    user = m.from_user.id
    is_sibyl = db.is_sibyl(m.chat.id)
    if not is_sibyl:
        return
    if is_alertsibyl(user):
        x = s.get_info(user)
        bot.send_message(
            m.chat.id,
            f"""
#ALERT
**This User Is Blacklisted**
**USER** : [{user}](tg://user?id={user})
**REASON** : {x.result.reason}
**ENFORCER** : [{x.result.banned_by}](tg://user?id={x.result.banned_by})""",
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
