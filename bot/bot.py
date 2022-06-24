import discord
import os
import logging
from dotenv import load_dotenv
from discord.ext import commands

#Logging (ERROR,WARNING,DEBUG)
logger = logging.getLogger('discord')
logger.setLevel(logging.WARNING)
handler = logging.FileHandler(filename='discord_bot.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

prfx = '!'
bot = commands.Bot(command_prefix = prfx)

@bot.command()
async def load(ctx, rotation):
    bot.load_extension(f'cogs.{rotation}')

@bot.command()
async def unload(ctx, rotation):
    bot.unload_extension(f'cogs.{rotation}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

#get the bot token from .env ...so secret
load_dotenv()
token = os.getenv('TOKEN')
client = discord.Client()
client.run(token)