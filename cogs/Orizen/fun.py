import discord
from discord.ext import commands


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Fun commands"""

    def help_custom(self):
        emoji = '🎭'
        label = "Fun Commands"
        description = "Commands for fun and interaction."
        return emoji, label, description

    @commands.group(name="fun", invoke_without_command=True)
    async def fun(self, ctx: commands.Context):
        """Fun commands: imagine, ship, mydog, chat, translate, howgay, lesbian, cute, intelligence, chutiya, horny, tharki, gif, iplookup, weather, hug, kiss, pat, cuddle, slap, tickle, spank, ngif, 8ball, truth, dare"""
        await ctx.send(
            "`/imagine`, `ship`, `mydog`, `chat`, `translate`, `howgay`, `lesbian`, `cute`, `intelligence`, `chutiya`, `horny`, `tharki`, `gif`, "
            "`iplookup`, `weather`, `hug`, `kiss`, `pat`, `cuddle`, `slap`, `tickle`, `spank`, `ngif`, `8ball`, `truth`, `dare`"
        )

    # Add additional subcommands here for each fun command, for example:

    @fun.command(name="imagine")
    async def imagine(self, ctx: commands.Context):
        """Imagine something fun"""
        await ctx.send("Imagine something awesome!")

    @fun.command(name="ship")
    async def ship(self, ctx: commands.Context):
        """Ship two people together"""
        await ctx.send("Let's ship two people!")

    # Add other commands like mydog, chat, etc.


def setup(bot):
    bot.add_cog(Fun(bot))
