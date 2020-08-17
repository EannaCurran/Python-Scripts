"""
    Python Discord Bot by Éanna Curran
    Program which runs a Discord bot that sends images and messages of Jeeves
"""


from discord.ext import commands
import random


# Settings for bot
TOKEN = "Private"
bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print("Working")
    print(bot.user.name)


# Command to sent image of Jeeves
@bot.command(pass_context=True)
async def jeeves_pic(ctx):
    number = random.randint(1, 21)
    await bot.send_file(ctx.message.channel, "JeevesBot/Images/%d.png" % number)


# Command to send quote from Jeeves
@bot.command(pass_context=True)
async def jeeves_quote(ctx):
    f = open("jeevesBot/Quotes.txt", "r")
    number = random.randint(0, 8)
    quote = f.readlines()[number]
    await bot.send_message(ctx.message.channel, quote)


bot.run(TOKEN)
