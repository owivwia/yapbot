import random
import settings
import discord
from discord.ext import commands

logger = settings.logging.getLogger("bot")

class Booper(commands.Converter):
    async def convert(self, ctx, argument):
        if argument.startswith("<@") and argument.endswith(">"):
            user_id = argument[2:-1].replace("!", "")
            member = await commands.MemberConverter().convert(ctx, user_id)
            return f"Boop! {ctx.author.mention} booped {member.mention}! owo"
        else: 
            return f"{ctx.author.mention} booped the air! uwu"

def run():
    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix="yap ", intents=intents)

    @bot.event
    async def on_ready():
        logger.info(f"User: {bot.user} (ID: {bot.user.id})") 

    @bot.command(
            # aliases = ["p"],
            # help = "This is help",
            # description = "This is description",
            # brief = "This is brief"
    )
    async def ping(ctx):
        """Answers the lonely user with a pong!"""
        await ctx.send("yap pong!")
    
    @bot.command()
    async def bing(ctx):
        """Answers the lonely user with a bong!"""
        await ctx.send("yap bong!")

    @bot.command()
    async def wat(ctx, wat = "wat owo?"):
        """YapBot is curious~!"""
        await ctx.send(wat)

    @bot.command()
    async def say(ctx, *what):
        """YapBot will say what you want!"""
        await ctx.send(" ".join(what))

    @bot.command(name='random')
    async def random_number(ctx, start : int, end : int):
        """YapBot will choose a random number between the two numbers you provide!"""
        await ctx.send(random.randint(start, end))

    @bot.command()
    async def add(ctx, one : int, two : int):
        """YapBot will help you do some quick mafs (+)!"""
        await ctx.send(one + two)

    @bot.command()
    async def subtract(ctx, one : int, two : int):
        """YapBot will help you do some quick mafs (-)!"""
        await ctx.send(one - two)

    @bot.command()
    async def boop(ctx, person : Booper ):
        await ctx.send(person)

    @boop.error
    async def add_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("You booped nothing!")


    bot.run(settings.DISCORD_API_SECRET, root_logger=True)

if __name__ == "__main__":
    run()