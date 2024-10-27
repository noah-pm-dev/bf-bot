# tmp invite https://discord.com/api/oauth2/authorize?client_id=1299952570797654026&permissions=274877975616&scope=bot%20applications.commands

import discord
import yaml

class Client(discord.Client):
    async def on_ready(self):
        print('Logged in as', self.user)
    
    async def on_message(self, message):
        if message.author == self.user:
            return
        
        if message.content == 'ping':
            await message.channel.send('pong')
intents = discord.Intents.default()
intents.message_content = True
client = Client(intents=intents)

with open("./src/secrets.yml") as stream:
    try:
        client.run(yaml.safe_load(stream)["token"])
    except yaml.YAMLError as exc:
        print(exc)