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

prfx = '!'
bot = commands.Bot(command_prefix=prfx)

load_dotenv()
token = os.getenv('TOKEN')
client = discord.Client()
client.run(token)