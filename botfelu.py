import discord

client = dicord.client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if "felu" in message.content:
        if ("cześć" or "czesc" or "hej" or "siema" or "elo") in message.content:
            msg = "uwu dzień dobry {0.author.mention}".format(message)
            await client.send_message(message.channel,msg)
        if ("hi" or "hello" or "henlo") in message.content:
            msg = "uwu henlo {0.author.mention}".format(message)
            await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
