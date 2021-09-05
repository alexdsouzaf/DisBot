import discord 
import subprocess
import asyncio
from discord.ext import commands
import discord.ext.tasks #import commands
import random

#COMANDO PARA CHAMAR O BOT
client = commands.Bot(command_prefix='/')

#-----------------------------//COMANDOS\\--------------------------------------------
@client.command()
async def ping(ctx):
        await ctx.send('pong')


@client.command()
async def d10(ctx):
    await ctx.send(dado())

def dado():
    return random.randint(1,10)


@client.event #UNICO EVENTO QUE TA FUNCIONANDO 
async def on_ready():
    print("Logged")

@client.event #NAO FOI IMPLEMENTADO, OUTRAS TENTATIVAS FALHARAM
async def on_member_join():
    pass

@client.command()
async def salve(ctx):
    await ctx.send("Olá meu chapa")
    

#-------------------------------------------------------------------------------------------
    
#-----------------------------//NECESSARIO REVER\\--------------------------------------------
#@client.event
#async def on_member_join(member):
#    print("client.send_message")
#    await client.send_message(message.channel, 'Hello')

#@client.event
#async def on_member_join(member):
#    print("client.say")
#    await client.say('Funcionou?')

#-------------------------------------------------------------------------------------------


#-----------------------------//DESUSO\\--------------------------------------------
class MyClient(discord.Client):

    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')

        if message.content == 'Salve':
            await message.channel.send('Olá meu chapa')  


    async def on_member_join(member):
        await message.channel.send('Bem-Vindo ' + member)


#INSTANCIA DA CLASSE ACIMA
#client = MyClient()
#--------------------------------------------------------------------------------

#TOKEN DE CONEXAO
client.run('STRING DO TOKEN')
