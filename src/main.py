import os
from discord.ext import commands
from discord import Intents
import random

from dotenv import dotenv_values

token = dotenv_values(".env")["TOKEN"]


bot = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    case_insensitive=True,  # Commands aren't case-sensitive
    intents=Intents.all()
)

bot.author_id = 369134955932155906 

@bot.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier

@bot.command()
async def pong(ctx):
    await ctx.send('pong')

@bot.command() # Sends back name of the caller.
async def name(ctx) :
    await ctx.send(ctx.author)

@bot.command()
async def count(ctx) :
    await ctx.send("**+++Online Members+++**")
    for member in ctx.guild.members :
        if (member.raw_status == "online") :
            await ctx.send(member.name)
    await ctx.send("**+++Offline Members+++**")
    for member in ctx.guild.members :
        if (member.raw_status == "offline") :
            await ctx.send(member.name)
    await ctx.send("**+++Idle Members+++**")
    for member in ctx.guild.members :
        if (member.raw_status == "idle") :
            await ctx.send(member.name)
    await ctx.send("**+++Do not disturb Members+++**")
    for member in ctx.guild.members :
        if (member.raw_status == "dnd") :
            await ctx.send(member.name)

@bot.command() # TODO
async def admin(ctx, message) :
    #if (not(ctx.guild.get_member(message))) :
    #    await ctx.send("Please give a valid username/mention.")
    #else :
    #    await ctx.send("Reussite")
    if (ctx.message.raw_mentions) :
        await ctx.send("Pipou")
    #Check nombre d'arg.Récupérer user. Verifier s'il existe. Creer role. Assigner role admin.

@bot.command()
async def xkcd(ctx) :
    url = "https://xkcd.com/" + str(random.randint(1,2521))
    await ctx.send(url)

@bot.command()
async def ban(ctx, message) :
    id = ctx.message.raw_mentions[0]
    await ctx.guild.ban(ctx.guild.get_member(id), reason="Bonne nuit mon petit !")


bot.run(token)  # Starts the bot