import discord 
import asyncio
from discord.ext import commands
import random

#COMANDO PARA CHAMAR O BOT
cliente = discord.Client(); #instanca a conexao com a API e outro serviço do discord
robo = commands.Bot(command_prefix='!'); #instancia o bot e seta um comando para chamar o bot



    
#----------------------------//EVENTOS\\------------------------------------------
@robo.event #FUNCIONA
async def on_ready():
    print("Logged")

@robo.event 
async def on_message(message): #só pode existir um
    if message.author == robo.user:
        return

    if message.content.startswith('oi'):
        await message.channel.send('olá!')

    if message.content == "ping":
        await message.channel.send('pong')


#----------------------------//FIM_EVENTOS\\------------------------------------------


#----------------------------//COMANDOS\\------------------------------------------
@robo.command()
async def D(ctx,num): #TEM QUE VER COMO PEGAR O NUMERO QUE VEM NA MENSAGEM
    await ctx.send(dado(num))

#----------------------------//FIM_COMANDOS\\------------------------------------------


#----------------------------//METODOS\\------------------------------------------
def dado(num):
    return random.randint(1,num)


#----------------------------//FIM_METODOS\\------------------------------------------




#TOKEN DE CONEXAO
robo.run('TOKEN')

