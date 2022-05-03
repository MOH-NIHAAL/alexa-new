"""Telegram Ping / Pong Speed
Syntax: .ping"""

import time
from pyrogram import Client, filters
from info import (
    COMMAND_HAND_LER
)
from plugins.helper_functions.cust_p_filters import f_onw_fliter

# -- Constants -- #
ALIVE = "𝘐 𝘭𝘦𝘷 𝘠𝘰𝘶 <a href='https://t.me/vloggerdeven_TG'>𝘥𝘬 </a>."
HELP = "CAACAgUAAxkBAAEEnY9icR7IVu4XCWIu8b5hmdkWqMSHowACSgUAAkHZ6VUXoTLB53NQIiQE"
# -- Constants End -- #


@Client.on_message(
    filters.command(["alive", "start"], COMMAND_HAND_LER) &
    f_onw_fliter
)
async def check_alive(_, message):
    await message.reply_text(ALIVE)


@Client.on_message(filters.command("hi", COMMAND_HAND_LER) & f_onw_fliter)
async def help_me(_, message):
    await message.reply_sticker(HELP)


@Client.on_message(filters.command("ping", COMMAND_HAND_LER) & f_onw_fliter)
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pong!\n{time_taken_s:.3f} ms")
