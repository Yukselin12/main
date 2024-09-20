import discord
from bot_logic import gen_pass
# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.lower().startswith('hola'):
        await message.channel.send("Hola!")
    elif message.content.lower().startswith('adiós'):
        await message.channel.send(":pensive:")

    elif message.content.lower().startswith('contraseña'): 
        await message.channel.send(gen_pass(10))
    elif message.content.lower().startswith('genera una contraseña'): 
        await message.channel.send(gen_pass(10))        
    else:
        await message.channel.send(message.content)

client.run("MTI4NTcxNTQzNDA1Nzg5MTkwMg.GiVzNt.s0Il4QHVsvTZtn2OueMfLJV7Ru1w54ZqAQsO8Q")
