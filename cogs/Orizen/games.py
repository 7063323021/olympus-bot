from random import Random
import discord
from discord.ext import commands

class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Games commands"""

    def help_custom(self):
        emoji = '🎮'
        label = "Games Commands"
        description = "Enjoy a variety of fun games."
        return emoji, label, description

    @commands.group(name="games", invoke_without_command=True)
    async def games(self, ctx: commands.Context):
        """Available games: `blackjack`, `chess`, `tic-tac-toe`, `country-guesser`, `rps`, `lights-out`, `wordle`, `2048`, `memory-game`, `number-slider`, `battleship`, `connect-four`, `slots`"""
        await ctx.send(
            "`blackjack`, `chess`, `tic-tac-toe`, `country-guesser`, `rps`, `lights-out`, `wordle`, `2048`, `memory-game`, `number-slider`, `battleship`, `connect-four`, `slots`"
        )

    # Example Game Command: Rock, Paper, Scissors
    @games.command(name="rps")
    async def rps(self, ctx: commands.Context, choice: str):
        """Play a game of rock, paper, scissors!"""
        valid_choices = ['rock', 'paper', 'scissors']
        if choice.lower() not in valid_choices:
            return await ctx.send(f"Invalid choice! Choose from: {', '.join(valid_choices)}")
        
        bot_choice = Random.choice(valid_choices)
        if bot_choice == choice.lower():
            result = "It's a tie!"
        elif (choice.lower() == "rock" and bot_choice == "scissors") or \
             (choice.lower() == "paper" and bot_choice == "rock") or \
             (choice.lower() == "scissors" and bot_choice == "paper"):
            result = f"You win! Bot chose {bot_choice}."
        else:
            result = f"You lose! Bot chose {bot_choice}."
        
        await ctx.send(result)

    # You can add more game-related commands below, similar to rps (e.g., blackjack, chess, etc.)


def setup(bot):
    bot.add_cog(Games(bot))
