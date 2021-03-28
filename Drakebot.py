import diceRolls
import discord
import os

class Drake():
  def __init__(self):
    self.botCaller = '$'
    self.client = discord.Client()
    
    @self.client.event
    async def on_ready():
      print('{0.user} is at your service'.format(self.client))

    @self.client.event
    async def on_message(message):
      if message.author == self.client.user:
        return
      if message.content.startswith(self.botCaller + 'roll'):
        toSend = diceRolls.dice(message)
        await message.channel.send(toSend)
    self.client.run(os.getenv('TOKEN'))

