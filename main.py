#!/usr/bin/env python3

# ------------------------ MODULE IMPORTS ------------------------ #
from discord import Permissions

from Cogs.variables import json, traceback, sys, discord, os, Guild, TextChannel, commands, datetime, Fore, asyncio
from Cogs.variables import prefix, blacklist, githuburl, ranks, supportinvite, emojiurl, bot, botinvite, ownercolor, \
    usercolor, announcecolor, commandcolor, twitchurl

# ------------------------ GLOBALBOT SETUPCODE ------------------------ #
if os.path.isfile("servers.json"):
    with open("servers.json", encoding="utf-8") as file:
        servers = json.load(file)

else:
    servers = {"servers": []}
    with open("servers.json", "w") as file:
        json.dump(servers, file, indent=4)


def guild_exists(guildid):
    for server in servers["servers"]:
        if int(server["guildid"]) == int(guildid):
            return True
    return False


def get_globalchat(guildid, channelid):
    globalchat = None
    for server in servers["servers"]:
        if int(server["guildid"]) == int(guildid):
            if channelid:
                if int(server["channelid"]) == int(channelid):
                    globalchat = server

            else:
                globalchat = server
    return globalchat


def get_globalchat_id(guildid):
    globalchat = -1
    i = 0
    for server in servers["servers"]:
        if int(server["guildid"]) == int(guildid):
            globalchat = i
        i += 1
    return globalchat


# ------------------------ COMMANDS ------------------------ #
@bot.command(name="announce", aliases=["important"])
@commands.guild_only()
async def announce(ctx, *, text):
    if str(ctx.author.id) not in ranks:
        embed = discord.Embed(
            title="Globalbot Errormessage: \n",
            description="You are missing Botowner permission(s) to run this command.\n"
                        f"\n\n[Support-Server]({supportinvite}) | [Bot-Invite]({botinvite}) | [GitHub]({githuburl})",
            color=commandcolor)

        embed.set_author(name=f"{ctx.author.name}", icon_url=f"{emojiurl}")
        embed.set_thumbnail(url=f"{ctx.author.avatar_url}")
        embed.set_footer(text=f"User ID: {ctx.author.id} | Sent from: {ctx.guild.name}",
                         icon_url=f"{ctx.author.avatar_url}")
        embed.timestamp = datetime.utcnow()
        await ctx.send(embed=embed)
        await ctx.message.delete()


    elif str(ctx.author.id) in ranks:
        embed = discord.Embed(
            title="➜ Important Announcement!",
            description=f"{text} \n\n[Support-Server]({supportinvite}) | [Bot-Invite]({botinvite}) | [GitHub]({githuburl})",
            color=announcecolor
        )
        embed.set_thumbnail(url=f"{ctx.author.avatar_url}")
        embed.set_footer(text=f"User ID: {ctx.author.id} | Sent from: {ctx.guild.name}",
                         icon_url=f"{ctx.author.avatar_url}")
        embed.timestamp = datetime.utcnow()

        for server in servers["servers"]:
            guild: Guild = bot.get_guild(int(server["guildid"]))
            if guild:
                channel: TextChannel = guild.get_channel(int(server["channelid"]))
                if channel:
                    await channel.send(embed=embed)
        await ctx.message.delete()


def convert(time):
    pos = ['s', 'm', 'h', 'd']

    time_dict = {'s': 1, 'm': 60, 'h': 3600, 'd': 3600 * 24}

    unit = time[-1]

    if unit not in pos:
        return -1
    try:
        val = int(time[:-1])
    except:
        return -2

    return val * time_dict[unit]


@bot.command()
@commands.guild_only()
@commands.has_permissions(administrator=True)
async def addglobal(ctx):
    if not guild_exists(ctx.guild.id):
        server = {
            "guildid": ctx.guild.id,
            "guild_name": ctx.guild.name,
            "channelid": ctx.channel.id,
            "invite": f'{(await ctx.channel.create_invite()).url}'
        }

        servers["servers"].append(server)
        with open('servers.json', 'w') as f:
            json.dump(servers, f, indent=4)

        if not str(ctx.author.id) in ranks or str(ctx.author.id) in ranks:
            await ctx.message.delete()
            embed = discord.Embed(title='New Globalchat Added!',
                                  description=f'The Server: `{ctx.guild.name}` with a total of `{len(ctx.guild.members)} Members` is now in the Globalgang!',
                                  color=0x1abc9c)

            embed.set_thumbnail(url=f"{ctx.author.avatar_url}")
            embed.set_footer(text='Sent from Server {}'.format(ctx.guild.name), icon_url=f"{ctx.guild.icon_url}")

            links = f"[Support-Server]({supportinvite}) | [Bot Invite]({botinvite}) | [GitHub]({githuburl})"

            embed.add_field(name='⠀', value='⠀', inline=False)
            embed.add_field(name='Links & Help', value=links, inline=False)

            for server in servers["servers"]:
                guild: Guild = bot.get_guild(int(server["guildid"]))
                if guild:
                    if guild.id is ctx.guild.id:
                        continue
                    channel: TextChannel = guild.get_channel(int(server["channelid"]))
                    if channel:
                        perms: Permissions = channel.permissions_for(guild.get_member(bot.user.id))
                        if perms.send_messages:
                            if perms.embed_links and perms.attach_files and perms.external_emojis:
                                await channel.send(embed=embed)
                            else:
                                await channel.send('I not have enough Permissions. I need following:'
                                                   '`Send Messages` `Embed Links` `Attach Files`'
                                                   '`Use External Emojis`')


@bot.command()
@commands.guild_only()
@commands.has_permissions(administrator=True)
async def removeglobal(ctx):
    if guild_exists(ctx.guild.id):
        globalid = get_globalchat_id(ctx.guild.id)
        if globalid != -1:
            servers["servers"].pop(globalid)
            with open('servers.json', 'w') as f:
                json.dump(servers, f, indent=4)

        embed = discord.Embed(
            description=f"Sucessfully removed Globalchat from Channel: {ctx.channel.mention}.",
            color=0xc0392b
        )

        await ctx.send(embed=embed)
        await ctx.message.delete()


# ------------------------ EVENTS ------------------------ #
@bot.event
async def on_message(message):
    if not message.guild or message.author.bot:
        return

    if not message.content.startswith(prefix):
        if get_globalchat(message.guild.id, message.channel.id):
            await sendAll(message, message.author)
    await bot.process_commands(message)


async def sendAll(message, member):
    global word
    bad_words = ["Hurensohn", "ficke", "Ficker", "Wichser", "bitch"]
    bad_word_detection = []

    for word in message.content.split():
        if word not in bad_words:
            bad_word_detection.append(False)
        else:
            bad_word_detection.append(True)

    if True in bad_word_detection:
        embed = discord.Embed(
            title="Blacklisted Word Detected! \n",
            description=f"I have detected that you used {word} what is blacklisted. Please stop doing that!\n"
                        f"Words on Blacklist:\n {bad_words}"
                        f"\n\n[Support-Server]({supportinvite}) | [Bot-Invite]({botinvite}) | [GitHub]({githuburl})",
            color=commandcolor)

        embed.set_author(name=f"{message.author.name}", icon_url=f"{emojiurl}")
        embed.set_thumbnail(url=f"{message.author.avatar_url}")
        embed.set_footer(text=f"User ID: {message.author.id} | Sent from: {message.guild.name}",
                         icon_url=f"{message.author.avatar_url}")
        embed.timestamp = datetime.utcnow()
        await message.channel.send(embed=embed)
        await message.delete()

    else:

        # If user is Blacklised:
        if str(message.author.id) in blacklist:
            await message.channel.send(
                f"{message.author.mention} You are not allowed to use the Bot during your Blacklist!")
            return

        # Wenn UserID  nicht in ranks variable: #
        if not str(message.author.id) in ranks:
            embed = discord.Embed(
                title="",
                description=f"{message.content} \n\n[Support-Server]({supportinvite}) | [Bot-Invite]({botinvite}) | [GitHub]({githuburl})",
                color=usercolor
            )

            embed.set_author(name=f"{member.name}",
                             icon_url=f"{emojiurl}")
            embed.set_thumbnail(url=f"{message.author.avatar_url}")
            embed.set_footer(text=f"User ID: {message.author.id} | Sent from: {message.guild.name}",
                             icon_url=f"{message.author.avatar_url}")
            embed.timestamp = datetime.utcnow()

            for server in servers["servers"]:
                guild: Guild = bot.get_guild(int(server["guildid"]))
                if guild:
                    channel: TextChannel = guild.get_channel(int(server["channelid"]))
                    if channel:
                        await channel.send(embed=embed)
            await message.delete()

        # Wenn UserID in ranks variable: #
        if str(message.author.id) in ranks:
            embed = discord.Embed(
                title="",
                description=f"{message.content} \n\n[Support-Server]({supportinvite}) | [Bot-Invite]({botinvite}) | [GitHub]({githuburl})",
                color=ownercolor
            )

            embed.set_author(name=f"{member.name} [Bot Developer]",
                             icon_url=f"{emojiurl}")
            embed.set_thumbnail(url=f"{message.author.avatar_url}")
            embed.set_footer(text=f"User ID: {message.author.id} | Sent from: {message.guild.name}",
                             icon_url=f"{message.author.avatar_url}")
            embed.timestamp = datetime.utcnow()

            for server in servers["servers"]:
                guild: Guild = bot.get_guild(int(server["guildid"]))
                if guild:
                    channel: TextChannel = guild.get_channel(int(server["channelid"]))
                    if channel:
                        await channel.send(embed=embed)
            await message.delete()


# ------------------------ BOT OUTPUT IF READY ------------------------ #
@bot.event
async def on_ready():
    print(f"{Fore.CYAN}")
    print("Logged in as: {0.user}".format(bot))
    print(f"{Fore.MAGENTA}")
    print("Running on servers: ")
    for s in bot.guilds:
        print(f"{Fore.RED} - %s (%s)" % (s.name, s.id))
    await bot.change_presence(status=discord.Status.idle)
    print(f"{Fore.LIGHTBLUE_EX}")
    print(f"Invite your Bot with this url: \n{botinvite}")
    print(f"{Fore.RESET}")

    while True:
        try:
            serverlist = [server.name for server in bot.guilds]
            await bot.change_presence(
                activity=discord.Streaming(
                    name=f"Managing {len(serverlist)} Guilds",
                    url=twitchurl))

            await asyncio.sleep(5.0)
            await bot.change_presence(
                activity=discord.Streaming(
                    name=f"{prefix}cmds / {prefix}commands",
                    url=twitchurl))
        except:
            print("Something went wrong")


# ------------------------ LOAD COGS ------------------------ #
if __name__ == '__main__':
    for filename in os.listdir("Cogs"):
        if filename.endswith(".py"):
            try:
                bot.load_extension(f"Cogs.{filename[:-3]}")
                print(f"{Fore.RED}[>] {Fore.GREEN}Cogs.{filename[:-3]} loaded")
            except Exception as e:
                print(f'Failed to load extension {filename}', file=sys.stderr)
                traceback.print_exc()

# ------------------------ RUN ------------------------ #
with open("configuration.json", "r") as f:
    data = json.load(f)
    token = data["Token"]
    bot.run(token)
data.close()
servers.close()
