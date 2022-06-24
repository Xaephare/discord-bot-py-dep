import discord
from discord.ext import commands

class Rotation(commands.Cog):

    def __init__(self, client):
        self.client = client

    #Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is online.')

    #Commands
    @commands.Command()
    async def ping(self, ctx):
        await ctx.send()

def setup(client):
    client.add_cog(Rotation(client))