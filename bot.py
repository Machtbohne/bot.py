import discord

def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()
       
token = read_token()

client = discord.Client()

@client.event
async def on_message(message):
    if message.content.find("!bewerbung") != -1:
        await message.channel.send("Hey Liebe Community,


Es ist endlich soweit hiermit Eröffne ich die Bewerbungphase Offiziell!

Wir suchen:

10 Supporter 

2 Moderator GESCHLOSSEN

3 Developer

2 Designer

3 Builder 

Alle Bewerbungen Per Privat Nachricht mir schicken! Falls ihr euch als Moderator Beworben habt aber wir schon Moderator haben werdet ihr warscheinlich Supporter. 

Nachdem ihr die Bewerbung geschickt habt werde ich euch nach Mindestens 7 tagen antworten ob ihr angenommen seit dann habt ihr erstmal ein Bewerbungsgespräch wo ihr paar Fragen beantworten müsst. 


Viel Glück an alle!

MFG GameSucht Administration")


    
    
client.run(NTUxNjczMTM2NTM4NDUxOTY5.D3KoSQ.eALZ0su8KyHfdt7f0UVVFKJbaWc)
client.run(str(os.environ.get('BOT_TOKEN')))
