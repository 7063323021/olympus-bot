import discord
from discord.ext import commands


class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Utility commands"""

    def help_custom(self):
        emoji = '🛠️'
        label = "Utility Commands"
        description = "Commands for utility and information retrieval."
        return emoji, label, description

    @commands.group(name="utility", invoke_without_command=True)
    async def utility(self, ctx: commands.Context):
        """Utility commands: botinfo, stats, invite, serverinfo, userinfo, roleinfo, boostcount, unbanall, joined-at, ping, github, vcinfo, channelinfo, badges, banner user, banner server, reminder start, reminder clear, permissions, timer\n\nMedia Commands: media, media setup, media remove, media config, media bypass, media bypass add, media bypass remove, media bypass show"""
        await ctx.send(
            "`botinfo`, `stats`, `invite`, `serverinfo`, `userinfo`, `roleinfo`, `boostcount`, `unbanall`, `joined-at`, `ping`, `github`, "
            "`vcinfo`, `channelinfo`, `badges`, `banner user`, `banner server`, `reminder start`, `reminder clear`, `permissions`, `timer`\n\n"
            "__**Media Commands**__\n"
            "`media`, `media setup`, `media remove`, `media config`, `media bypass`, `media bypass add`, `media bypass remove`, `media bypass show`"
        )

    # Add additional subcommands here for each utility function, for example:

    @utility.command(name="ping")
    async def ping(self, ctx: commands.Context):
        """Check bot's latency"""
        await ctx.send(f"Pong! {round(self.bot.latency * 1000)}ms")


def setup(bot):
    bot.add_cog(Utility(bot))
