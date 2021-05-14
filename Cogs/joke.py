import discord
import json
import aiohttp

from discord.ext import commands
from datetime import datetime
# ------------------------ VARIABLES ------------------------ #
with open('configuration.json') as f:
	config = json.load(f)

prefix = config.get("Prefix")
ownerid = config.get("OwnerID")
clientid = config.get("ClientID")
ownercolor = 0x8000ff
commandcolor = 0x08c42e
bot = commands.Bot(command_prefix=prefix, intents=discord.Intents.all(), case_insensitive=True, help_command=None)
botinvite = f"https://discord.com/oauth2/authorize?client_id={clientid}&scope=bot&permissions=-8"

# ------------------------ COGS ------------------------ #
class jokeCog(commands.Cog, name="jokeCog"):
	def __init__(self, bot):
		self.bot = bot

# ------------------------ JOKE COMMAND ------------------------ #
	@commands.command()
	@commands.guild_only()
	async def joke(self, ctx):
		if str(ctx.author.id) in ownerid:
			await ctx.message.delete()

			headers = {
				"Accept": "application/json"
			}
			async with aiohttp.ClientSession()as session:
				async with session.get("https://icanhazdadjoke.com", headers=headers) as req:
					r = await req.json()
			embed = discord.Embed(title="Random Generated Dadjoke: ", description=r["joke"], color=ownercolor)
			embed.set_thumbnail(url="https://media.tenor.com/images/99338a98580194539b4ecbcbc1ade726/tenor.gif")
			embed.set_footer(text=f"User ID: {ctx.author.id} | Sent from: {ctx.guild.name}", icon_url=f"{ctx.author.avatar_url}")
			embed.timestamp = datetime.utcnow()
			await ctx.channel.send(embed=embed)

		else:
			if str(ctx.author.id) not in ownerid:
				await ctx.message.delete()
				headers = {
					"Accept": "application/json"
				}
				async with aiohttp.ClientSession()as session:
					async with session.get("https://icanhazdadjoke.com", headers=headers) as req:
						r = await req.json()
				embed = discord.Embed(title="Random Generated Dadjoke: ", description=r["joke"], color=commandcolor)
				embed.set_thumbnail(url="https://media.tenor.com/images/99338a98580194539b4ecbcbc1ade726/tenor.gif")
				embed.set_footer(text=f"User ID: {ctx.author.id} | Sent from: {ctx.guild.name}", icon_url=f"{ctx.author.avatar_url}")
				embed.timestamp = datetime.utcnow()
				await ctx.channel.send(embed=embed)

# ------------------------ END OF COG ------------------------ #  
def setup(bot):
	bot.remove_command("help")
	bot.add_cog(jokeCog(bot))

