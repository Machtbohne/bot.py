from discord.ext import commands
import discord
import asyncio
import youtube_dl
from discord.ext import commands
from discord.utils import find
import requests as rq

client = commands.Bot(command_prefix="/")
player_dict = dict()


@client.event
async def on_ready():
    print("Bot ist bereit")
   
@client.command(pass_context=True)
async def play(ctx, url):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)
    server = ctx.message.server
    voice = client.voice_client_in(server)
    player = await voice.create_ytdl_player(url)
    player_dict[server.id] = player
    await client.send_message(ctx.message.channel, "Spiele `%s` ab" % player.title)
    player.start()


@client.command(pass_context=True)
async def stop(ctx):
    server = ctx.message.server
    player = player_dict[server.id]
    await client.send_message(ctx.message.channel, "Stoppe `%s` " % player.title)
    player.stop()
    del player_dict[server.id]
    
   
client.run(str(os.environ.get('BOT_TOKEN')))
