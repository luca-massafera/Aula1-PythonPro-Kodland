import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Estamos logados como {bot.user}')

@bot.command()
async def poluicao(ctx):
    await ctx.send("Digite a primeira palavra desses comandos e descubra mais sobre: " \
    "Redução de desperdício, " \
    "Consumo consciente, " \
    "Alimentação sustentável, " \
    "Lixo na praia, " \
    "Os três R")

@bot.command()
async def Reducao(ctx):
    await ctx.send("Reduzir o desperdício é uma das maneiras mais eficazes de combater a poluição. Isso pode ser feito através da redução do consumo de produtos descartáveis, como sacolas plásticas e utensílios de plástico, e da escolha de produtos duráveis e reutilizáveis.")

@bot.command()
async def Consumo(ctx):
    await ctx.send("O consumo consciente é uma abordagem que incentiva as pessoas a fazerem escolhas de consumo mais responsáveis e sustentáveis. Isso inclui a escolha de produtos com menor impacto ambiental, a redução do desperdício e o apoio a empresas que adotam práticas sustentáveis.")

@bot.command()
async def Alimentacao(ctx):
    await ctx.send("A alimentação sustentável é uma abordagem que busca reduzir o impacto ambiental da produção e do consumo de alimentos. Isso inclui a escolha de alimentos produzidos de forma sustentável, a redução do desperdício de alimentos e a promoção de dietas mais saudáveis e equilibradas.")

@bot.command()
async def Lixo(ctx):
    await ctx.send("O lixo na praia é um problema ambiental significativo afetando a vida marinha e a saúde humana. A poluição por lixo na praia pode ser causada pelo descarte inadequado de resíduos, e pode ter efeitos negativos na fauna e flora marinha, bem como na qualidade da água e do ar.")

@bot.command()
async def TresR(ctx):
    await ctx.send("Os três R's referem-se a Reduzir, Reutilizar e Reciclar. Essa abordagem incentiva a redução do consumo de recursos naturais, a reutilização de produtos e materiais sempre que possível, e a reciclagem de materiais para reduzir o impacto ambiental e promover a sustentabilidade.")

bot.run('')
