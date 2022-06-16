import discord
import os
import logging
from dotenv import load_dotenv
from discord.ext import commands


logger = logging.getLogger('discord')
logger.setLevel(logging.WARNING)
handler = logging.FileHandler(filename='discord_bot.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)



load_dotenv()
token = os.getenv('TOKEN')

client = discord.Client()

prfx = "/"

@client.event
async def on_ready():
    print(f"{client.user} is using enlargment pills!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(f'{prfx}greet'):
        await message.channel.send('Hello! I am huge dick bot, my penis? massive.')


client.run(token)