import discord
from discord.ext import commands, tasks
from scraper import scraper


current = scraper()

class Rotation(commands.Cog):

    def __init__(self, client):
        self.client = client

    #Events **********************************************************************************************************************
    @commands.Cog.listener()
    async def on_ready(self):
        self.scraperLoop.start()
        print('Bot is online.')

    #Loops **********************************************************************************************************************
    @tasks.loop(minutes=1)
    async def scraperLoop(self):
        global current
        if current != scraper():
            current = scraper()
        else:
            print('No change in rotation, scraper may be down.')

    #Commands **********************************************************************************************************************
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f' {round(self.client.latency * 1000)}ms')

    @commands.command(name='Rotation', aliases=['r', 'rotation', 'R'])
    async def rotation(self, ctx):
        global current
        await ctx.send(f'*On now:*\n`{current[0][0]}`\n*Upcoming:*\n`{current[0][1]}` in `{current[1][0]}`\n`{current[0][2]}` in `{current[1][1]}` ')


def setup(client):
    client.add_cog(Rotation(client))