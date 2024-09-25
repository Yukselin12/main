import discord
from bot_logic import gen_pass
from discord.ext import commands
# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
bot = commands.Bot(command_prefix = "$", intents=intents)
@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')


@bot.command()
async def hello(ctx):
    await ctx.send("Hi!")

@bot.command()
async def bye(ctx):
    await ctx.send("😔")

@bot.command()
async def password(ctx):
    await ctx.send(gen_pass(10))

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def add1(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left * right)

@bot.command()
async def add2(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left / right)
@bot.command()
async def add3(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left - right)
@bot.command()
async def ayuda(ctx):
    await ctx.send("Ayuda. para ejecutar commandos siempre utilice al inicio $ ejemplo: $hello, Comandos: add add1 add2 add3 descripcion (Suma multiplica divide resta) hello y bye tambien son comandos")
@bot.command()
async def Help(ctx):
    await ctx.send("Help. to execute commands always use $ at the beginning example: $hello, Commands: add add1 add2 add3 description (Add multiply divide subtract) hello and bye are also commands")

bot.run("¡SU TOKEN DEBERIA ESTAR AQUI (robado)!")

