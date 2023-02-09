
    
import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
tkn = "deleteOTM4MzY0MDAwNzEyOTMzMzc3.GjhlMO.sFBRvvJNg59wE-xR0BRd4kWsLnP1hoNSYfhVkkdelete"
#getting token from txt file
with open("token.txt", "r") as f:
    token = f.read()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
        
#join vice channel        
@client.event
async def on_voice_state_update(member, before, after):
    if before.channel is None and after.channel is not None:
        # User just joined a voice channel
        voice_channel = after.channel
        print(f"{member} joined {voice_channel}")
        await voice_channel.connect()      

client.run(token)
