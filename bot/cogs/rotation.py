import discord
from discord.ext import commands
from scraper import scraper


class Rotation(commands.Cog):

    def __init__(self, client):
        self.client = client

    #Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is online.')

    #Commands
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f' {round(self.client.latency * 1000)}ms')

    @commands.command()
    async def rotation(self, ctx):
        current = scraper()
        await ctx.send(f'*On now:*\n`{current[0][0]}`\n*Upcoming:*\n `{current[0][1]}` in `{current[1][0]}`\n`{current[0][2]}` in `{current[1][1]}` ')

        

def setup(client):
    client.add_cog(Rotation(client))