import discord
from sheets import *

client = discord.Client()
sheet = Sheets()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Command to insert data to excel
    if message.content.startswith('!add'):
        SPREADSHEET_ID = '1D6Mq_Y9OS17GH3Dp8VCsoRmCISmGG21o2L_AL0h4Tw4'  # Add ID here
        RANGE_NAME = 'A2'
        FIELDS = 3  # main/alt/notes


    msg = message.content[4:]
    result = [x.strip() for x in msg.split(',')]
    if len(result) == FIELDS:
        # Add
        print(message.created_at)
        DATA = [message.author.name] + [message.author.id] + [str(message.created_at)] + result
        sheet.add(SPREADSHEET_ID, RANGE_NAME, DATA)
        await message.channel.send('Your data has been successfully submitted!')
    else:
        # Needs more/less fields
        await message.channel.send(
            'Error: You need to add {0} fields, meaning it can only have {1} comma.'.format(FIELDS, FIELDS - 1))

client.run('NjQwOTIwNDc3Mzc1OTIyMTc2.XcA2WQ.q1ohtSAznQiPQdm-MhK3tCIeQZM')
