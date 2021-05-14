from Cogs.variables import discord, datetime, commands, prefix, githuburl, ranks, supportinvite, owneremojiurl, emojiurl, botinvite, ownercolor, commandcolor

# ------------------------ COGS ------------------------ #
class HelpCog(commands.Cog, name="HelpCog"):
	def __init__(self, bot):
		self.bot = bot

# ------------------------ HELP COMMAND ------------------------ #
	@commands.command(name='commands', usage="(commandName)", description="Display the help message.", aliases=["cmds", "h"])
	@commands.guild_only()
	async def commands(self, ctx):
		if str(ctx.author.id) in ranks:
			embed = discord.Embed(
				title=f"Command List: \n",
				description=f"{prefix}cmds => Shows this Message\n"
							f"{prefix}announce => Sending a Announcement though all Servers (Botowner only)\n"
							f"{prefix}addglobal => Setup Globalchat in a Channel\n"
							f"{prefix}removeglobal => Removes GlobalChat from a channel\n"
							f"{prefix}serverlist => Shows Servernames where im in\n"
							f"{prefix}joke => Generating a random joke using a API\n"
							f"\n\n[Support-Server]({supportinvite}) | [Bot-Invite]({botinvite}) | [GitHub]({githuburl})", color=ownercolor)

			embed.set_author(name=f"[Bot Developer] {ctx.author.name}", icon_url=f"{owneremojiurl}")
			embed.set_thumbnail(url=f'{ctx.author.avatar_url}')
			embed.set_footer(text=f"User ID: {ctx.author.id} | Sent from: {ctx.guild.name}", icon_url=f"{ctx.author.avatar_url}")
			embed.timestamp = datetime.utcnow()
			await ctx.send(embed=embed)
			await ctx.message.delete()

		else:
			if not str(ctx.author.id) in ranks:
				embed = discord.Embed(
					title=f"Command List: \n",
					description=f"{prefix}cmds => Shows this Message\n"
								f"{prefix}announce => Sending a Announcement though all Servers (Botowner only)\n"
								f"{prefix}addglobal => Setup Globalchat in a Channel\n"
								f"{prefix}removeglobal => Removes GlobalChat from a channel\n"
								f"{prefix}serverlist => Shows Servernames where im in\n"
								f"{prefix}joke => Generating a random joke using a API\n"
								f"\n\n[Support-Server]({supportinvite}) | [Bot-Invite]({botinvite}) | [GitHub]({githuburl})", color=commandcolor)

				embed.set_author(name=f"Unranked Normie | {ctx.author.name}", icon_url=f"{emojiurl}")
				embed.set_thumbnail(url=f"{ctx.author.avatar_url}")
				embed.set_footer(text=f"User ID: {ctx.author.id} | Sent from: {ctx.guild.name}", icon_url=f"{ctx.author.avatar_url}")
				embed.timestamp = datetime.utcnow()
				await ctx.channel.send(embed=embed)
				await ctx.message.delete()

# ------------------------ END OF COG ------------------------ #  
def setup(bot):
	bot.remove_command("help")
	bot.add_cog(HelpCog(bot))
