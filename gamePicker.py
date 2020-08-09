# gamePicker.py
import os
import random
import discord
from dotenv import load_dotenv

wake = "!gamePicker"

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

#this event will inform the user the bot
#has connected via the command prompt
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

#this event will listen for messages in chat
#and reply to the user if appropriate
@client.event
async def on_message(message):
    if message.author == client.user:
        return	
    if message.content.startswith(wake) == True:
        input = message.content[:]
        splitVal = input.split(" ")
        response = random.choice(splitVal)
        await message.channel.send(response)

client.run(TOKEN)