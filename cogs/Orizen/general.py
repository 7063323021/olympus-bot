import discord
from discord.ext import commands


class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """General commands"""

    def help_custom(self):
        emoji = '🪩'
        label = "General Commands"
        description = "Commands for general server management and information."
        return emoji, label, description

    @commands.group(name="general", invoke_without_command=True)
    async def general(self, ctx: commands.Context):
        """General commands: status, afk, avatar, banner, servericon, membercount, poll, hack, token, users, wizz, urban, rickroll, hash, snipe, list boosters, list inrole, list emojis, list bots, list admins, list invoice, list mods, list early, list activedeveloper, list createpos, list roles"""
        await ctx.send(
            "`status`, `afk`, `avatar`, `banner`, `servericon`, `membercount`, `poll`, `hack`, `token`, `users`, `wizz`, `urban`, `rickroll`, `hash`, `snipe`, "
            "`list boosters`, `list inrole`, `list emojis`, `list bots`, `list admins`, `list invoice`, `list mods`, `list early`, `list activedeveloper`, `list createpos`, `list roles`"
        )

    # Example of some general commands

    @general.command(name="status")
    async def status(self, ctx: commands.Context):
        """Get bot status"""
        await ctx.send("Bot is online and running!")

    @general.command(name="avatar")
    async def avatar(self, ctx: commands.Context, user: discord.User = None):
        """Get the avatar of a user"""
        user = user or ctx.author
        await ctx.send(f"{user}'s avatar: {user.avatar.url}")

    @general.command(name="membercount")
    async def membercount(self, ctx: commands.Context):
        """Show the server's member count"""
        await ctx.send(f"Member count: {ctx.guild.member_count}")

    # You can add other commands (poll, hack, users, etc.) in a similar fashion


def setup(bot):
    bot.add_cog(General(bot))
