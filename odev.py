import discord
from config import token

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('+hello'):
        await message.channel.send('Hello!')
    if message.content.startswith('+how are you'):
        await message.channel.send('Not fine or happy becouse ı am a artifical inteligence ı dont know what means happy or sad')

client.run(token)
