import discord
from discord.ext import commands

class Automod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Automod commands"""

    def help_custom(self):
        emoji = '🚨'
        label = "Automod Commands"
        description = ""
        return emoji, label, description

    @commands.group(name="automod", invoke_without_command=True)
    async def automod(self, ctx: commands.Context):
        """Automod command group, shows available automod commands"""
        await ctx.send(
            "`automod`, `automod enable`, `automod disable`, `automod punishment`, `automod config`, `automod logging`, "
            "`automod ignore`, `automod ignore channel`, `automod ignore role`, `automod ignore show`, `automod ignore reset`, "
            "`automod unignore`, `automod unignore channel`, `automod unignore role`\n\n"
            "__**Blacklistword Commands**__\n"
            "`blacklistword`, `blacklistword add <word>`, `blacklistword remove <word>`, `blacklistword reset`, `blacklistword config`, "
            "`blacklistword bypass add <user/role>`, `blacklistword bypass remove <user/role>`, `blacklistword bypass show`"
        )

    # Add subcommands here for automod enable/disable, blacklistword, etc.

def setup(bot):
    bot.add_cog(Automod(bot))
