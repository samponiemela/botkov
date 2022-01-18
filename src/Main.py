
import discord
import random

client = discord.Client()
loadouts = ["Pistolboi", "Gigachad", "Journalist", "Halexboi"]
maps = ["Woods", "Factory", "Labs", "Shoreline", "Customs", "Lighthouse", "Reserve"]
user = discord.utils.get(client.users, name = "USERNAME", discriminator='1234')

@client.event
async def on_ready():
    print('{0.user} logging in'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!commands'):
        await message.channel.send('Ammochart: !ammochart')
        await message.channel.send('Maps: !maps')
        await message.channel.send('Reddit: !reddit')
        await message.channel.send('Flea market prices: !flea')
        await message.channel.send('Quest helper: !quests')
        await message.channel.send('Quest items: !taskitems')

    if message.content.startswith('!ammochart'):
        await message.channel.send('https://tarkov-ballistics.com/')

    if message.content.startswith('!maps'):
        await message.channel.send('https://mapgenie.io/tarkov')

    if message.content.startswith('!reddit'):
        await message.channel.send('https://new.reddit.com/r/EscapefromTarkov/')

    if message.content.startswith('!flea'):
        await message.channel.send('https://tarkov-market.com/')

    if message.content.startswith('!quests'):
        await message.channel.send('https://escapefromtarkov.fandom.com/wiki/Quests')

    if message.content.startswith('!taskitems'):
        await message.channel.send(file=discord.File('QuestItemRequirements.png'))

    if message.content.startswith('!rmap'):
        await message.channel.send(random.choice(maps))

    if message.content.startswith('!curse'):
        await message.channel.send(random.choice(loadouts))



client.run('OTMyMzg3ODg4MTY1OTUzNTM2.YeSP4w.OMavdtt8-ldMg4a32-C4iNW4S1A')
