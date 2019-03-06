from discord.ext import commands

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
    
    
client.event
async def on_member_join(member):
   
    users = json.load(f)

    await update_data(users, member)

    with open('users.json', 'w') as f:
      json.dump(users, f)

@client.event
async def on_message(message):
  with open('users.json', 'r') as f:
    users = json.load(f)

    await update_data(users, message.author)
    await add_experience(users, message.author, 5)
    await level_up(users, message.author, message.channel)

    with open('users.json', 'w') as f:
      json.dump(users, f)

async def update_data(users, user):
  if not user.id in users:
    users[user.id] = {}
    users[user.id]['experience'] = 0
    users[user.id]['level'] = 1

async def add_experience(users, user, exp):
  users[user.id]['experience'] + exp

async def level_up(users, user, channel):
  experience = users[user.id]['experience']
  lvl_start = users[user.id]['level']
  lvl_end = int(experience ** (1/4))

if lvl_start < lvl_end:
   await client.send_message(ctx.message.channel, "{} Ist Aufgeleveld zu Level {}")


client.run(str(os.environ.get('BOT_TOKEN')))
