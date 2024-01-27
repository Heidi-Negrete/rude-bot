import discord
from discord.ext import commands
import config
import foas

intents = discord.Intents.default()
intents.message_content = True
intents.emojis = True
intents.reactions = True

client = discord.Client(intents=intents)

fucks = foas.Foas()


@client.event
async def on_ready():
    print(f'Logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$****off'):
        await message.channel.send(fucks.give_fuck())

    if 'fuck' in message.content.replace(" ", "").lower():
        await message.add_reaction("🖕")


@client.event
async def on_reaction_add(reaction, user):
    if reaction.emoji == "🖕":
        await reaction.message.add_reaction("🖕")

client.run(config.bot_token)
