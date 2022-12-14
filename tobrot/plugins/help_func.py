#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) 5MysterySD | Anasty17 [MLTB]
#
# Copyright 2022 - TeamTele-LeechX
# 
# This is Part of < https://github.com/5MysterySD/Tele-LeechX >
# All Right Reserved

import logging
import pyrogram
import os

from tobrot import *
from tobrot.helper_funcs.display_progress import humanbytes, TimeFormatter
from time import time
from subprocess import check_output
from psutil import disk_usage, cpu_percent, swap_memory, cpu_count, virtual_memory, net_io_counters, boot_time
from pyrogram import enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

async def new_join_f(client, message):
    chat_type = message.chat.type
    if chat_type != enums.ChatType.PRIVATE:
        await message.reply_text(
            f"""<b>šš»āāļø Hello dear!\n\n This Is A Leech Bot .This Chat Is Not Supposed To Use Me</b>\n\n<b>Current CHAT ID: <code>{message.chat.id}</code>""",
            parse_mode=enums.ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('Channel', url='https://t.me/FuZionXTorrentQuater')
                    ]
                ]
               )
            )
        # leave chat
        await client.leave_chat(chat_id=message.chat.id, delete=True)
    # delete all other messages, except for AUTH_CHANNEL
    #await message.delete(revoke=True)


async def stats(client, message):
    stats = 'āāāāā š šš¼š š¦šš®šš š āāāāāā»\n'
    if os.path.exists('.git'):
        last_commit = check_output(["git log -1 --date=format:'%I:%M:%S %p %d %B, %Y' --pretty=format:'%cr ( %cd )'"], shell=True).decode()
    else:
        LOGGER.info("Stats : No UPSTREAM_REPO")
        last_commit = ''
    if last_commit:
        stats += f'ā£ š <b>Commit Date:</b> {last_commit}\nā\n'
    currentTime = TimeFormatter((time() - BOT_START_TIME)*1000)
    osUptime = TimeFormatter((time() - boot_time())*1000)
    total, used, free, disk= disk_usage('/')
    total = humanbytes(total)
    used = humanbytes(used)
    free = humanbytes(free)
    sent = humanbytes(net_io_counters().bytes_sent)
    recv = humanbytes(net_io_counters().bytes_recv)
    cpuUsage = cpu_percent(interval=0.5)
    p_core = cpu_count(logical=False)
    t_core = cpu_count(logical=True)
    swap = swap_memory()
    swap_p = swap.percent
    swap_t = humanbytes(swap.total)
    memory = virtual_memory()
    mem_p = memory.percent
    mem_t = humanbytes(memory.total)
    mem_a = humanbytes(memory.available)
    mem_u = humanbytes(memory.used)
    stats +=f'ā£ š¤ <b>Bot Uptime:</b> {currentTime}\n'\
            f'ā£ š¶ <b>OS Uptime:</b> {osUptime}\nā\n'\
            f'ā£ š <b>Total Disk Space:</b> {total}\n'\
            f'ā£ š <b>Used:</b> {used} | š <b>Free:</b> {free}\nā\n'\
            f'ā£ š¤ <b>Upload:</b> {sent}\n'\
            f'ā£ š„ <b>Download:</b> {recv}\nā\n'\
            f'ā£ š¦ <b>CPU:</b> {cpuUsage}%\n'\
            f'ā£ š§¬ <b>RAM:</b> {mem_p}%\n'\
            f'ā£ š <b>DISK:</b> {disk}%\nā\n'\
            f'ā£ š <b>Physical Cores:</b> {p_core}\n'\
            f'ā£ š <b>Total Cores:</b> {t_core}\nā\n'\
            f'ā£ š <b>SWAP:</b> {swap_t} | š <b>Used:</b> {swap_p}%\n'\
            f'ā£ š« <b>Memory Total:</b> {mem_t}\n'\
            f'ā£ š­ <b>Memory Free:</b> {mem_a}\n'\
            f'ā£ š¬ <b>Memory Used:</b> {mem_u}\nā\n'\
            f'āāā¦ļøāš šØšš£šš š¹šŖ {UPDATES_CHANNEL}ā¦ļøāā¹'
    await message.reply_text(text = stats,
        parse_mode = enums.ParseMode.HTML,
        disable_web_page_preview=True
    )


async def help_message_f(client, message):

    reply_markup = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("šļø Open Help šļø", callback_data = "openHelp_pg1")
            ]
        ]
    )
    await message.reply_text(
        text = f"""āā š <b>HELP MODULE</b> š āāāā»
ā
āā¢ <i>Open Help to Get Tips and Help</i>
āā¢ <i>Use the Bot Like a Pro User</i>
āā¢ <i>Access Every Feature That Bot Offers in Better Way </i>
āā¢ <i>Go through Commands to Get Help</i>
ā
āāā¦ļøāš šØšš£šš š¹šŖ {UPDATES_CHANNEL}ā¦ļøāā¹""",
        reply_markup = reply_markup,
        parse_mode = enums.ParseMode.HTML,
        disable_web_page_preview=True
    )

