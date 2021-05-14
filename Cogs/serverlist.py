from Cogs.variables import discord, datetime, commandcolor, bot, commands

class ServerlistCog(commands.Cog, name="ServerlistCog"):
	def __init__(self, bot):
		self.bot = bot
# ------------------------ SERVERLIST COMMAND ------------------------ #
	@commands.command()
	@commands.guild_only()
	async def serverlist(self, ctx):
		serverlist = [server.name for server in bot.guilds]

		embed = discord.Embed(
			title=f"All Servers im curretly in: ({len(serverlist)})",
			description=f" \n".join(serverlist),
			color=commandcolor
		)
		embed.set_thumbnail(url=f"{ctx.guild.icon_url}")
		embed.set_footer(text=f"Requested by: {ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")
		embed.timestamp = datetime.utcnow()
		await ctx.message.delete()
		await ctx.send(embed=embed)

# ------------------------ END OF COG ------------------------ #  
def setup(bot):
	bot.add_cog(ServerlistCog(bot))
