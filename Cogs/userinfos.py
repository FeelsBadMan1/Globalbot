from Cogs.variables import discord, commands, randint, re, developer, datetime
# ------------------------ COGS ------------------------ #  

class UserInfosCog(commands.Cog, name="user infos command"):
    def __init__(self, bot):
        self.bot = bot

# ------------------------------------------------------ #  

    # @commands.command(name = 'userinfos', aliases=["ui", "userinfo", "info", "infos"],usage="<@user/ID>",description="Displays data from user.")
    # async def userinfos (self, ctx, member):

    #     # Get member
    #     member = re.findall(r'\d+', member) # Get only numbers from member
    #     member = self.bot.get_user(int(member[0]))

    #     if member is not None:
    #         embed = discord.Embed(title=f"__**{member.name} informations :**__", description="", color=randint(0, 0xffffff))
    #         embed.set_thumbnail(url=f'{member.avatar_url}')
    #         embed.add_field(name="**Member ID :**", value=f"{member.id}", inline=True)
    #         embed.add_field(name="**Account creation :**", value=f"{member.created_at.year}-{member.created_at.month}-{member.created_at.day} {member.created_at.hour}:{member.created_at.minute}:{member.created_at.second}", inline=True)
    #         for guildMember in ctx.guild.members:
    #             if guildMember == member:
    #                 embed.add_field(name="**Joined at :**", value=f"{guildMember.joined_at.year}-{guildMember.joined_at.month}-{guildMember.joined_at.day} {guildMember.joined_at.hour}:{guildMember.joined_at.minute}:{guildMember.joined_at.second}", inline=True)
    #         embed.set_footer(text=f"Bot Created by {developer}")
    #         await ctx.channel.send(embed=embed)
    #     else:
    #         await ctx.channel.send("Member not found!")

    @commands.command(name='userinfo', aliases=["ui", "userinfos", "info", "infos"],usage="<@user/ID>",description="Displays data from user.")
    async def userinfo(self, ctx, member: discord.Member = None):

        if member is not None:
            # de = pytz.timezone('Europe/Berlin')
            embed = discord.Embed(title=f'> Userinfo for {member.display_name} | {ctx.author.id}', description='', color=0x4cd137) # , timestamp=datetime.now().astimezone(tz=de)

            embed.add_field(name='Name', value=f'```{member.name}#{member.discriminator}```', inline=True)
            embed.add_field(name='Bot', value=f'```{("Look hes a Botuser lol" if member.bot else "Hes a Human imagine that!")}```', inline=True)
            embed.add_field(name='Nickname', value=f'```{(member.nick if member.nick else "No current Servernickname found!")}```', inline=True)
            for guildMember in ctx.guild.members:
                if guildMember == member:
                    embed.add_field(name='Server Joindate', value=f'```{member.joined_at}```', inline=True)
            embed.add_field(name='Account creation', value=f'```{member.created_at}```', inline=True)
            embed.add_field(name='Roles', value=f'```{len(member.roles) -1}```', inline=True)
            embed.add_field(name='Highest Role', value=f'```{member.top_role.name}```', inline=True)
            embed.add_field(name='Color', value=f'```{member.color}```', inline=True)
            embed.add_field(name='Booster', value=f'```{("Yes this guy is a booster :)" if member.premium_since else "No Booster :(")}```', inline=True)
            embed.set_footer(text=f'Developer: {developer}', icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)

        elif member is None:
            await ctx.channel.send("Member not found!")

# ------------------------ BOT ------------------------ #

def setup(bot):
    bot.add_cog(UserInfosCog(bot))
