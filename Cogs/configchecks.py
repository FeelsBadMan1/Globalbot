#!/usr/bin/env python3

# ------------------------ MODULE IMPORTS ------------------------ #

from Cogs.variables import time, Fore, commands, prefix, token, clientid, githuburl, ranks, supportinvite, owneremojiurl, emojiurl, twitchurl, bot
bot.remove_command("help")

# ------------------------ COGS ------------------------ #
class ConfigChecks(commands.Cog, name="Config Checks"):
    def __init__(self, bot):
        self.bot = bot

# ------------------------ CONFIG CHECK ------------------------ #
def exitbot():
    print("\n")
    print(f"{Fore.RED}Shutdown the Bot...")
    time.sleep(1)
    exit(0)

    if prefix == "":
        print(f"No{Fore.CYAN} Prefix {Fore.RESET}in {Fore.CYAN} configuration.json {Fore.RESET} is set. Please Edit the config!")
        exitbot()

    if token == "":
        print(f"No{Fore.CYAN} Bottoken {Fore.RESET}in {Fore.CYAN} configuration.json {Fore.RESET} is set. Please Edit the config!")
        exitbot()

    if clientid == "":
        print(f"No{Fore.CYAN} ClientID {Fore.RESET}in {Fore.CYAN} configuration.json {Fore.RESET} is set. Please Edit the config!")
        exitbot()

    if githuburl == "":
        print(f"No{Fore.CYAN} GithubURL {Fore.RESET}in {Fore.CYAN} configuration.json {Fore.RESET} is set. Please Edit the config!")
        exitbot()

    if ranks == "":
        print(f"No{Fore.CYAN} OwnerID {Fore.RESET}in {Fore.CYAN} configuration.json {Fore.RESET} is set. Please Edit the config!")
        exitbot()

    if supportinvite == "":
        print(f"No{Fore.CYAN} Serverinvite {Fore.RESET}in {Fore.CYAN} configuration.json {Fore.RESET} is set. Please Edit the config!")
        exitbot()

    if owneremojiurl == "":
        print(f"No{Fore.CYAN} OwnerEmojiURL {Fore.RESET}in {Fore.CYAN} configuration.json {Fore.RESET} is set. Please Edit the config!")
        exitbot()

    if emojiurl == "":
        print(f"No{Fore.CYAN} EmojiURL {Fore.RESET}in {Fore.CYAN} configuration.json {Fore.RESET} is set. Please Edit the config!")
        exitbot()

    if twitchurl == "":
        print(f"No{Fore.CYAN} TwitchURL {Fore.RESET}in {Fore.CYAN} configuration.json {Fore.RESET} is set. Please Edit the config!")
        exitbot()
# ------------------------ COGS END ------------------------ #
def setup(bot):
    bot.add_cog(ConfigChecks(bot))