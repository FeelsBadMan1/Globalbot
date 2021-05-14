import json
import discord
import traceback
import sys
import aiohttp
import time
import asyncio
import re
import numpy as np
import random
import string
import Augmentor
import os
import shutil
import asyncio


from discord.ext import commands
from random import randint
from datetime import datetime
from discord.ext.commands import has_permissions
from colorama import Fore
from nude import Nude
from io import BytesIO
from profanity_check import predict
from discord.utils import get
from PIL import ImageFont, ImageDraw, Image
from Tools.logMessage import sendLogMessage
from discord import Guild, TextChannel

with open('configuration.json') as f:
    config = json.load(f)

developer = config.get("Developer")
prefix = config.get("Prefix")
token = config.get("Token")
clientid = config.get("ClientID")
blacklist = config.get("Blacklist")
githuburl = config.get("Githuburl")
ranks = config.get("OwnerID")
supportinvite = config.get("Supportserver")
owneremojiurl = config.get("Owneremojiurl")
emojiurl = config.get("Emojiurl")
twitchurl = config.get("Twitchurl")
botinvite = f"https://discord.com/oauth2/authorize?client_id={clientid}&scope=bot&permissions=-8"

ownercolor = 0x8000ff
usercolor = 0x03989b
announcecolor = 0xe1ff00
commandcolor = 0x08c42e
bot = commands.Bot(command_prefix=prefix, intents=discord.Intents.all(), case_insensitive=True, help_command=None)
botinvite = f"https://discord.com/oauth2/authorize?client_id={clientid}&scope=bot&permissions=-8"
bot.remove_command("help")
# ------------------------ COGS ------------------------ #

class VariablesCog(commands.Cog, name="VariablesCog"):
    def __init__(self, bot):
        self.bot = bot

def setup(bot):
    bot.add_cog(VariablesCog(bot))