import discord
from discord.ext import commands


class sonuIgnore(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Ignore commands"""

    def help_custom(self):
              emoji = '<:olympus_ignore:1254106939693203467>'
              label = "Ignore Commands"
              description = ""
              return emoji, label, description

    @commands.group()
    async def __Ignore__(self, ctx: commands.Context):
        """`ignore` , `ignore command add` , `ignore command remove` , `ignore command show` , `ignore channel add` , `ignore channel remove` , `ignore channel show` , `ignore user add` , `ignore user remove` , `ignore user show` , `ignore bypass add` , `ignore bypass show` , `ignore bypass remove`"""