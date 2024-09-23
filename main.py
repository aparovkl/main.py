import discord
import random
from discord.ext import commands
from defs_logic import *
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command("мем")
async def мем(ctx):
    numb = random.randint(1, 4)
    if numb == 1:
        with open(f'meme collection/images/mem1.jpg', 'rb') as f:
                picture = discord.File(f)
            # Можем передавать файл как параметр!
        await ctx.send(file=picture)
    elif numb == 2:
        with open(f'meme collection/images/mem2.jpg', 'rb') as f:
                picture = discord.File(f)
            # Можем передавать файл как параметр!
        await ctx.send(file=picture)
    elif numb == 3:
        with open(f'meme collection/images/mem3.jpg', 'rb') as f:
                picture = discord.File(f)
            # Можем передавать файл как параметр!
        await ctx.send(file=picture)
    elif numb == 4:
        with open(f'meme collection/images/mem4.jpg', 'rb') as f:
                picture = discord.File(f)
            # Можем передавать файл как параметр!
        await ctx.send(file=picture)


@bot.command('животные')
async def животные(ctx):
    '''По команде duck вызывает функцию get_random_animal_image_url'''
    image_url = get_random_animal_image_url()
    await ctx.send(image_url)

@bot.command('команды' or 'help' or 'помощь')
async def duck(ctx):
     await ctx.send('Привет, это список команд моего бота!')
     await ctx.send('!мем - Кидает в чат рандомный мем')
     await ctx.send('!животные - Кидает в чат картинку с уточкой')
     

bot.run('')