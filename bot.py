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
    
import discord
import asyncio
import youtube_dl
from discord.ext import commands
from discord.utils import find
import requests as rq



def get_prefix(bot, msg):
    """A callable Prefix for our bot. This could be edited to allow per server prefixes."""

    # Notice how you can use spaces in prefixes. Try to keep them simple though.
    prefixes = ['.']

    return commands.when_mentioned_or(*prefixes)(bot, msg)


bot = commands.Bot(command_prefix=get_prefix,description='A music bot fro discord Kurusaki')
YOUTUBE_API='YOUR YOUTUBE API'
bot.remove_command('help')

from discord import opus
OPUS_LIBS = ['libopus-0.x86.dll', 'libopus-0.x64.dll','libopus-0.dll', 'libopus.so.0', 'libopus.0.dylib']


def load_opus_lib(opus_libs=OPUS_LIBS):
    if opus.is_loaded():
        return True

    for opus_lib in opus_libs:
            try:
                opus.load_opus(opus_lib)
                return
            except OSError:
                pass

    raise RuntimeError('Could not load an opus lib. Tried %s' %(', '.join(opus_libs)))


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
    
   
client.run('NTUxNjczMTM2NTM4NDUxOTY5.D2Gcog.ck27miUQZIIsjh_UqV3kqAPDSUI')
