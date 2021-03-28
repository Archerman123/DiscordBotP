import diceRolls
import bossFight as bossF
import wheel
import discord
import os
import wheelsMaker
import stringManipTools as strManip
import rules
from keep_alive import keep_alive

class Spike():

  def diceRolls(self, message):
    command = self.commandParser(message)
    print("Rolling some dices")
    dices = command[1]
    results = diceRolls.parse_dice(dices)
    if not isinstance(results,str):
      if isinstance(results,list):
        total = 0
        for nb in results:
          total += nb
      else:
        total = results
      return "The total is: " + str(total) + "\n" + "Rolls: " + str(results) 
    else:
      return results

  def callRemover(self,message):
    toRemove = ''
    if message.startswith(self.botCaller + 'roll'):
        toRemove = self.botCaller + 'roll'
    elif message.startswith(self.botCaller + 'boss'):
        toRemove = self.botCaller + 'boss'
    elif message.startswith(self.botCaller + 'wheel'):
        toRemove = self.botCaller + 'wheel'
    message = message.replace(toRemove,'')
    if message.startswith(' '):
      message = message[1:]
    return message

  def commandParser(self, message):
    return strManip.stringParser(message)

  def help(self):
    toSend = "My currently available commands are: \n"
    toSend += "- help: shows the list of available com-... wait...\n"
    toSend += "- roll: allow to roll dices. support multiple dices and modifiers \n"
    toSend += "- boss: a mini-game all about coordination without comunicating your intentions! (W.I.P)\n"
    toSend += "- wheel: make a list of words and randomly pick one of them, like your own mini wheel of fortune. type " + self.botCaller + "wheel help for more info \n"
    toSend += "- rules: Show the specified rule of the server"
    return toSend

  def bossCmd(self,message):
    print("Calling the boss!")
    command = self.commandParser(message)
    #print(command)
    nbrCmd = len(command)
    #print(nbrCmd)
    helpMessage = "This is a work in progress boss fight mini game. Available commands:"
    helpMessage += "\n - !boss join [character name] (register a character to join in the fight)"
    helpMessage += "\n - !boss [character] \|\|attack\|\| (attack the boss with the specified character)"
    helpMessage += "\n - !boss reset (reset the fight and the list of participents)"
    helpMessage += "\n - !boss status (tells you who is alive and isn't. also gives a estimate of how well the boss is doing)"
    helpMessage += "\n - !boss round (end the current round. should only be used by the game master when all players have taken action)"
    
    if nbrCmd > 1:
      if command[1] == "help":
        return helpMessage
      elif command[1] == "reset":
        return self.boss.reset()
      elif command[1] == 'status':
        return self.boss.status()
      elif command[1] == 'round':
        return self.boss.endRound()
      elif command[1] == 'hp':
        if nbrCmd > 2:
          self.boss.setHP(int(command[2]))
          return "Boss HP changed successfully"
        else:
          return "Error: must specify the new boss hp ammount"
      elif command[1] == 'difficulty':
        if nbrCmd > 2:
          self.boss.setAC(int(command[2]))
          return "Boss difficulty changed successfully"
        else:
          return "Error: must specify the new boss armor class ammount"
      elif command[1] == 'join':
        if nbrCmd > 2:
          if self.boss.isCharLegit(command[2]):
            return "Error: character already registered"
          else:
            self.boss.join(command[2])
            return str(command[2]) + " was registered successfully"
        else: 
          return "Error: no character name specified"
      elif nbrCmd > 2:
        if command[2] == '||attack||' or command[2] == 'attack':
          return self.boss.canAttack(command[1])
      else:
        return "Error: The command does not exist or was misswritten. try typing !boss help"
    else:
      return helpMessage

  def wheelCmd(self,message):
    command = self.commandParser(message)
    nbrCmd = len(command)
    helpMessage = "Spin the wheel and get a random result! Current options:\n !wheel list (return the list of the currently available wheels) \n- !wheel [name of the wheel] (spin the wheel) \n - !wheel [name of the wheel] list (returns the content of the wheel) \n - !wheel [name of the wheel] add [word] (adds the word to wheel. Warning, any additions to the wheel will be lost on bot reload. will be fixed later) \n - !wheel [name of the wheel] remove [word] (Remove a option from the wheel) \n Note: Please replace any spaces by the character '-', exemple: Seven-Jefferson"
    if nbrCmd == 1:
      return helpMessage
    elif command[1] == "help":
      return helpMessage
    elif command[1] in self.wheelNames:
      position = self.wheelNames.index(command[1])
      wheel = self.wheels[position]
      if nbrCmd > 2:
        if command[2] == "list":
          return "The wheel contains: " + str(wheel.getContent())
        elif command[2] == "add":
          if nbrCmd > 3:
            wheel.addContent(command[3])
            try:
              self.wheelM.updateWheel(wheel)
            except:
              return "Error: There was a problem when trying to save the change" 
            return command[3] + " was added to the wheel successfully"
          else:
             return 'Error: message was "' + message + '" and is not a valid input. please do "!wheel help" for more details.'
        elif command[2] == "remove":
          toSend = wheel.removeContent(command[3])
          try:
            self.wheelM.updateWheel(wheel)
          except:
            return "Error: There was a problem when trying to save the change" 
          return toSend
      else:
        return wheel.spin()
    elif command[1] == "list":
      return "The available wheels are: " + str(self.wheelNames)
    else:
      return 'Error: message was "' + message + '" and is not a valid input. please do "!wheel help" for more details.'

  def rulesCmd(self, message):
    command = self.commandParser(message)
    self.rules = rules.rulesList()
    nbrCmd = len(command)
    #print(ruleNumber)
    if nbrCmd > 1:
      ruleNumber = command[1]
      description = self.rules.getRule(ruleNumber)
      if description.startswith("Error:"):
        return description
      else:
        return "Rule " + ruleNumber + ": " + description
    else:
      return "Use !rules [rule number] too show a specific rule of the server"


  def __init__(self):
    self.wheelM = wheelsMaker.wheelMaker()
    self.botCaller = '!'
    self.client = discord.Client()
    self.boss = bossF.Boss()
    self.charWheel = wheel.wheel('chars',['Seven','Ninia','Vikki'])
    self.wheels = self.wheelM.getWheels()
    self.wheelNames = []
    for w in self.wheels:
        self.wheelNames.append(w.getName())
    self.charWheel = self.wheels[0]
    self.wrongCommand = "The command was miswritten or does not exist. try typing " + self.botCaller + "help"
    @self.client.event
    async def on_ready():
      print('{0.user} is here to assist!'.format(self.client))
    
    @self.client.event
    async def on_message(message):
      toSend = "Error, something went wrong with my coding"
      if message.author == self.client.user:
        return
      if not message.content.startswith(self.botCaller):
        return

      if message.content.startswith(self.botCaller + 'roll'):
        toSend = self.diceRolls(message.content)
      elif message.content.startswith(self.botCaller + 'boss'):
        #print(message)
        toSend = self.bossCmd(message.content)
      elif message.content.startswith(self.botCaller + 'help'):
        toSend = self.help()
      elif message.content.startswith(self.botCaller + 'wheel'):
        toSend = self.wheelCmd(message.content)
      elif message.content.startswith(self.botCaller + 'rules'):
        toSend = self.rulesCmd(message.content)
      else:
        toSend = self.wrongCommand 

      if toSend != None:
        await message.channel.send(toSend)
      else:
        print("Error: No message was prepared, please recheck the code")



    keep_alive()
    self.client.run(os.getenv('TOKEN2'))  

 
