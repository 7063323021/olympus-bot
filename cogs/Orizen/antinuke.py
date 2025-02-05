import discord
from discord.ext import commands

class Antinuke(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Antinuke commands"""

    def help_custom(self):
        emoji = '🛡️'
        label = "Security Commands"
        description = ""
        return emoji, label, description

    @commands.group(name="antinuke", invoke_without_command=True)
    async def antinuke(self, ctx: commands.Context):
        """Displays antinuke commands information"""
        await ctx.send(
            "`antinuke`, `antinuke enable`, `antinuke disable`, `whitelist`, `whitelist @user`, `unwhitelist`, "
            "`whitelisted`, `whitelist reset`, `extraowner`, `extraowner set`, `extraowner view`, `extraowner reset`, "
            "`nightmode`, `nightmode enable`, `nightmode disable`\n\n__**Emergency Situation**__\n`emergency`, `emergency enable`, "
            "`emergency disable`, `emergency role`, `emergency role add`, `emergency role remove`, `emergency role list`, "
            "`emergency authorise`, `emergency authorise add`, `emergency authorise remove`, `emergency authorise list`, "
            "`emergency-situation (emgs)`"
        )

    # Add subcommands here for antinuke enable/disable, whitelist, etc.

def setup(bot):
    bot.add_cog(Antinuke(bot))
