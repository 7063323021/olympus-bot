import discord
from discord.ext import commands


class sonu11111111111111111(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Giveaway commands"""
  
    def help_custom(self):
		      emoji = '<:olympus_giveaways:1222784568290185246>'
		      label = "Giveaway Commands"
		      description = ""
		      return emoji, label, description

    @commands.group()
    async def __Giveaway__(self, ctx: commands.Context):
        """`gstart`, `gend`, `greroll` , `glist`"""