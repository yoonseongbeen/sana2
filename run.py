#run.py

import discord
from discord.ext import commands

token = ("token")

bot = commands.Bot(command_prefix = '!', help_command = None)




@bot.event
async def on_ready():
    print(f'부팅 성공 : {bot.user.name}!')
    game = discord.Game("조민준") 
    await bot.change_presence(status = discord.Status.online, activity = game)


@bot.command()
async def 도움말(ctx):
    embed = discord.Embed(title = "도움말", description = "**!가입**\n서비스에 가입할 수 있습니다.\n\n**!탈퇴**\n서비스에서 탈퇴할 수 있습니다.\n\n", color = 0xffc0cb)
    embed.set_footer(text = f"{ctx.message.author.name} | 윤성빈#6115", icon_url = ctx.message.author.avatar_url)
    await ctx.send(embed = embed)
    
@bot.command()
async def 가입(ctx):
    signup(ctx.author.name, ctx.author.id)


bot.run(token)




