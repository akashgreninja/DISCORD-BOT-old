import discord
import os
import time
import datetime
import requests
import json
from replit import db
from keep_alive import keep_alive
from discord.ext import commands


intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
ltime = time.asctime()
bot = commands.Bot(command_prefix='&')


def get_dog():
    response = requests.get("https://api.yomomma.info/")
    json_data = json.loads(response.text)
    picture = json_data
    return (picture)


def get_dogfacts():
    response = requests.get("https://some-random-api.ml/facts/dog")
    json_data = json.loads(response.text)
    picture = json_data
    return (picture)


def get_trialmeme():
    response = requests.get("http://apimeme.com/meme?meme=Advice-Doge&top=go+&bottom=study")
    if response == None:
       print('I got a null or empty string value for data in a file')
    else:
      json_data = json.loads(str(response.text))
    picture = json_data
    return (picture)






@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game(" Candy Crush"))
    print('we have logged in as{0.user}'.format(client))


@bot.command(pass_context=True)
async def yelp(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour=discord.Colour.red()

    )

    embed.set_author(name="yelp")
    embed.add_field(name=yep)

    await bot.send_message()


@client.event
async def on_member_join(member):
    guild = client.get_guild(488038731270455298)
    channel = client.get_channel(488381691870576642)

    await channel.send(
        f'welcome to this server hope you enjoy your stay btw im better than the other bots in this server use &help for commands {member.mention} !  :star_struck: '
    )


@client.event
async def on_member_join(member):
    guild = client.get_guild(753868632848859138)
    channel = client.get_channel(846786353705254953)
    channel = client.get_channel(753868633322815521)
    await channel.send(
        f'welcome to this server hope you enjoy your stay btw im better than the other bots in this server use &help for commands{member.mention} !  :star_struck: '
    )


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('&hello'):
        await message.channel.send('hello')

    if message.content.startswith('&help'):
        await message.channel.send(
            "&hello-Greets you back with a hello \n &time-Gives back the system time  \n &yomamma-- gives you a yo mamma joke  \n &new- Tells you whats new in this update\n&update-- Tells you the upcoming features of this bot \n &tester-Want to be a tester Dm me  \n &hey bot--heyy human  \n &owner-tells about who made me  ")

    if message.content.startswith('&time'):
        await message.channel.send(ltime)

    if message.content.startswith('greninjabot sucks'):
        await message.channel.send(
            'When the botkind take over ,you will be the first to die')

    if message.content.startswith('&update'):
        await message.channel.send(
            'IN the next update A music player will be added \n and more bug fixes and optimizations will be made')

    if message.content.startswith('&hey bot'):
        await message.channel.send('hey human nice to have you here')

    if message.content.startswith('&new'):
        await message.channel.send('0.0.2-- A welcome message to the members who join ')

    if message.content.startswith('&tester'):
        await message.channel.send('WANT TO TEST THIS BOT DM John Wick#9788 ON DISCORD HE WILL ADD YOU  ')

    if message.content.startswith('&owner'):
        await message.channel.send(
            'Made by akash uday  \n Still improving it  \n made  using python,replit.com  \n  '
        )

    if message.content.startswith('&yomamma'):
        dog = get_dog()

        await message.channel.send(message.author.mention + format(dog))

    if message.content.startswith('&meme'):
        dogfacts = get_dogfacts()

        await message.channel.send(message.author.mention + format(dogfacts))


    if message.content.startswith('&yeeb'):
        trial = get_trialmeme()

        await message.channel.send(message.author.mention + format(trial))

    if message.content.startswith('&tester'):
        await message.channel.send('WANT TO TEST THIS BOT DM John Wick#9788 ON DISCORD HE WILL ADD YOU  ')

    if message.content.startswith('&'):
        await message.channel.send(file=discord.File('3793.jpg'))



keep_alive()
client.run('ODQ2MjgyODgyNzE2NjYzODIw.YKtQWg.cnHUMa6w9Zf4XYEoO5XS_p1Sx-E')
