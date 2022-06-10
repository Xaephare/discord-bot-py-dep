import discord
import os

from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
token = os.getenv('TOKEN')

client = discord.Client()

prefix = "/"

@client.event
async def on_ready():
    print(f"{client.user} is using enlargment pills!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(f'{prefix}greet'):
        await message.channel.send('Hello! I am huge dick bot, my penis? massive.')


client.run(token)