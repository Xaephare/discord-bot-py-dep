import discord
from discord.ext import commands, tasks
from scraper import scraper


current = scraper()

class Rotation(commands.Cog):

    def __init__(self, client):
        self.client = client

    #Events
    @commands.Cog.listener()
    async def on_ready(self):
        self.scraperLoop.start()
        print('Bot is online.')

    #Loops
    @tasks.loop(minutes=1)
    async def scraperLoop(self):
        global current
        current = scraper()

    @tasks.loop(minutes=1)
    async def artisanPing(self): #i will make this modular in future but for now just need it working
        if current[0][1] == "World's Edge" and current[1][0] == " 5 mins":
            channel = self.client.get_channel(994396674363506728)
            await channel.send("<@!429917352579039232> Guess what's on in 5 minutes.")

    #Commands
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f' {round(self.client.latency * 1000)}ms')

    @commands.command(name='Rotation', aliases=['r', 'rotation', 'R'])
    async def rotation(self, ctx):
        global current
        await ctx.send(f'*On now:*\n`{current[0][0]}`\n*Upcoming:*\n`{current[0][1]}` in `{current[1][0]}`\n`{current[0][2]}` in `{current[1][1]}` ')

    @commands.command()
    async def loop(self, ctx):
        try:
            self.artisanPing.start() # start the loop if it isn't currently running
            await ctx.send("Started pinging <@!429917352579039232>")
        except: # happens if the loop is already running
            self.artisanPing.cancel() # if so, cancel the loop
            await ctx.send("Stopped pinging <@!429917352579039232>")

def setup(client):
    client.add_cog(Rotation(client))