#!/usr/bin/env python3

# ------------------------ MODULE IMPORTS ------------------------ #
from Cogs.variables import discord, datetime, commands, githuburl, supportinvite, emojiurl, botinvite, commandcolor

# ------------------------ COGS ------------------------ #
class EventsCog(commands.Cog, name="EventsCog"):
    def __init__(self, bot):
        self.bot = bot

# ------------------------------------------------------- #



# ------------------------ BOT ------------------------ #

def setup(bot):
    bot.add_cog(EventsCog(bot))
