import diceRolls
import bossFight as bossF
import discord
import os
import wheelsMaker
import stringManipTools as strManip
from discord_slash.utils.manage_commands import create_choice, create_option
from discord import guild
from discord_slash import SlashCommand, SlashContext
from discord.ext import commands
import keep_alive
import oc
import time
import rules
from os import system


class Spike():
    def diceRolls(self, message):
        command = self.commandParser(message)
        dices = command[1]
        results = diceRolls.roll_dice(dices)
        return results

    def commandParser(self, message):
        return strManip.stringParser(message)

    def help(self):
        toSend = "My currently available commands are: \n"
        toSend += "- help: shows the list of available com-... wait...\n"
        toSend += "- roll: allow to roll dices. support multiple dices and modifiers \n"
        toSend += "- boss: a mini-game all about coordination without comunicating your intentions! (W.I.P)\n"
        toSend += "- oc: Tired of sifting trough the #oc-info-channel  to find a char description? Now you can put the first name of a char and get a direct link to their info page! (if they added their page to the list first)\n"
        toSend += "- wheel: make a list of words and randomly pick one of them, like your own mini wheel of fortune. type " + self.botCaller + "wheel help for more info \n"
        toSend += "- rules: Show the specified rule of the server"
        return toSend

    def bossCmd(self, message):
        print("Calling the boss!")
        command = self.commandParser(message)
        nbrCmd = len(command)
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

    def wheelCmd(self, message, server):
        self.wheels = self.wheelM.getWheels(server)
        self.wheelNames = []
        for w in self.wheels:
            self.wheelNames.append(w.getName())
        command = self.commandParser(message)
        nbrCmd = len(command)
        helpMessage = "Spin the wheel and get a random result! Current options:\n !wheel list (return the list of the currently available wheels) \n- !wheel [name of the wheel] (spin the wheel) \n - !wheel [name of the wheel] list (returns the content of the wheel) \n - !wheel [name of the wheel] add [word] (adds the word to wheel. Warning, any additions to the wheel will be lost on bot reload. will be fixed later) \n - !wheel [name of the wheel] remove [word] (Remove a option from the wheel) \n Note: Please replace any spaces by the character '-', example: Seven-Jefferson"
        if nbrCmd == 1:
            return helpMessage
        elif command[1] == "help":
            return helpMessage
        elif command[1] in self.wheelNames:
            position = self.wheelNames.index(command[1])
            aWheel = self.wheels[position]
            if nbrCmd > 2:
                if command[2] == "list":
                    return "The wheel contains: " + str(aWheel.getContent())
                elif command[2] == "add":
                    if nbrCmd > 3:
                        aWheel.addContent(command[3])
                        try:
                            self.wheelM.updateWheel(aWheel, server)
                        except:
                            return "Error: There was a problem when trying to save the change"
                        return command[
                            3] + " was added to the wheel successfully"
                    else:
                        return 'Error: message was "' + message + '" and is not a valid input. please do "!wheel help" for more details.'
                elif command[2] == "remove":
                    toSend = aWheel.removeContent(command[3])
                    try:
                        self.wheelM.updateWheel(aWheel, server)
                    except:
                        return "Error: There was a problem when trying to save the change"
                    return toSend
            else:
                return aWheel.spin()
        elif command[1] == "list":
            return "The available wheels are: " + str(self.wheelNames)
        else:
            return 'Error: message was "' + message + '" and is not a valid input. please do "!wheel help" for more details.'

    def rulesCmd(self, message, server):
        command = self.commandParser(message)
        self.rules = rules.rulesList()
        nbrCmd = len(command)
        #self.rules.addRule(0,server)
        #print(ruleNumber)
        if nbrCmd > 1:
            ruleNumber = command[1]
            description = self.rules.getRule(ruleNumber, server)
            if description.startswith("Error:"):
                return description
            else:
                return "Rule " + ruleNumber + ": " + description
        else:
            return "Use !rules [rule number] too show a specific rule of the server\n\nAdd an 'r' before the number to get the roleplay rules\nExemple: " + self.botCaller + "rules r1"

    def ocCmd(self, message):
        command = self.commandParser(message)
        self.rules = rules.rulesList()
        nbrCmd = len(command)
        helpMsg = "- " + self.botCaller + "oc [OC first name] (return the discord link of a character description sheet) \n"
        helpMsg = helpMsg + "- " + self.botCaller + "oc add [OC first name] [discord link] (Add your oc to the list so people can find them easily)"
        nameList = self.ocBox.getList()
        if nbrCmd == 2:
            if command[1] == "help":
                return helpMsg
            else:
                if command[1] == "list":
                    return nameList
                elif command[1] in nameList:
                    return self.ocBox.getOC(command[1])
                return "Name not found, try " + self.botCaller + "oc list"
        if nbrCmd == 4:
            if command[1] == "add":
                if command[3].startswith("https://discord.com/channels/"):
                    self.ocBox.addOC(command[2], command[3])
                    return "successfully added " + command[2] + " to the list"
                else:
                    return "Last argument must contain a discord link. Ex: " + self.botCaller + "oc add [Oc name] [https: //discord.com/channels/...]"
        return self.wrongCommand

    def __init__(self, web):
        self.wheelM = wheelsMaker.wheelMaker()
        self.botCaller = '!'
        self.client = discord.Client()
        self.boss = bossF.Boss()
        self.wrongCommand = "The command was miswritten or does not exist. try typing " + self.botCaller + "help"
        self.limiter = 0
        self.web = web

        @self.client.event
        async def on_ready():
            print('{0.user} is here to assist!'.format(self.client))
            self.web.addSuccess(self.web)
            self.web.updateStat(self.web, "Online (! commands)")

        self.ocBox = oc.ocStorage()

        @self.client.event
        async def on_message(message):
            toSend = "Error, something went wrong with my coding"
            global server
            server = message.guild

            if message.author == self.client.user:
                return
            if not message.content.startswith(self.botCaller):
                return

            server = message.guild
            #print(message)

            if message.content.startswith(self.botCaller + 'roll'):
                toSend = self.diceRolls(message.content)
            elif message.content.startswith(self.botCaller + 'boss'):
                #print(message)
                toSend = self.bossCmd(message.content)
            elif message.content.startswith(self.botCaller + 'help'):
                toSend = self.help()
            elif message.content.startswith(self.botCaller + 'wheel'):
                toSend = self.wheelCmd(message.content, server)
            elif message.content.startswith(self.botCaller + 'rules'):
                toSend = self.rulesCmd(message.content, server)
            elif message.content.startswith(self.botCaller + 'oc'):
                toSend = self.ocCmd(message.content)
            else:
                toSend = self.wrongCommand

            #print(self.limiter)
            if toSend != None:
                if self.limiter < 10:
                    await message.channel.send(toSend)
                    print(self.limiter)
                    self.limiter += 1
                else:
                    print("slowing down")
                    time.sleep(2)
                    await message.channel.send(toSend)
                    self.limiter = 0
            else:
                print(
                    "Error: No message was prepared, please recheck the code")

        status = "null"
        keep_alive.keep_alive()
        try:
            self.client.run(os.getenv('TOKEN2'))
        except discord.errors.HTTPException:
            print("\nBLOCKED BY RATE LIMITS\nRESTARTING NOW\n")
            self.web.addAttempt(self.web)
            status = "Offline"
            self.web.updateStat(self.web, status)
            system("python restarter.py")
            system('kill 1')
