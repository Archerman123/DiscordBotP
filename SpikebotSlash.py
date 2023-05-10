import discord
from discord.ext import commands
from discord import guild
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option
import os
from os import system
import wheelsMaker
import diceRolls
import rules
import keep_alive

client = commands.Bot(command_prefix="!")
slash = SlashCommand(client, sync_commands=True)
wheelM = wheelsMaker.wheelMaker()
server = "Seven's Server"  #client.get_guild(224344566042591235)
allGuilds = [572411470105673729, 224344566042591235, 832720743372292127]
rulesObj = rules.rulesList()
message = None
web = None



@client.event
async def on_ready():
    print('{0.user} is here to assist!'.format(client))
    web.addSuccess(web)
    web.updateStat(web, "Online (Slash commands)")


@client.event
async def on_message(msg):
    global message
    global server
    message = msg
    server = message.guild


@slash.slash(name="rules",
             description="Show the specified rule of the server",
             guild_ids=[224344566042591235],
             options=[
                 create_option(
                     name="rule_number",
                     description="enter the number associated with the rule",
                     required=True,
                     option_type=3)
             ])
async def _rules(ctx, rule_number):
    description = rulesObj.getRule(rule_number, server)
    if description.startswith("Error:"):
        await ctx.send(description)
    else:
        await ctx.send("Rule " + rule_number + ": " + description)


@slash.slash(
    name="wheel",
    description="randomly pick from a list of names",
    guild_ids=[224344566042591235, 832720743372292127],
    options=[
        create_option(
            name="action",
            description="enter the name of the action you want to perform",
            required=True,
            option_type=3,
            choices=[
                create_choice(name="list", value="list"),
                create_choice(name="spin", value="spin"),
                create_choice(name="help", value="help"),
                create_choice(name="remove", value="remove"),
                create_choice(name="add", value="add")
            ]),
        create_option(
            name="wheel_name",
            description=
            "enter the name of the wheel you want to perform the action on",
            required=False,
            option_type=3),
        create_option(
            name="content_name",
            description=
            "enter the name of the the content you wish to add or remove",
            required=False,
            option_type=3)
    ])
async def _wheel(ctx, action, wheel_name="Empty", content_name="Empty"):
    wheels = wheelM.getWheels(server)
    wheelNames = []

    for w in wheels:
        wheelNames.append(w.getName())

    if wheel_name == "Empty":
        if action == "spin" or action == "add" or action == "remove":
            toSend = "Error: to use the '" + action + "' action, you must specify a wheel and the name of the content to be added"
            await ctx.send(toSend)
            return "Error: No specified wheel name when required"
    else:
        if content_name == "Empty":
            if action == "add" or action == "remove":
                toSend = "Error: to use the 'add' action, you must also specify a the name of the content to be added"
                await ctx.send(toSend)
                return "Error: No specified content name when required"

        position = wheelNames.index(wheel_name)
        aWheel = wheels[position]

    if action == "help":
        toSend = '''
    Here are the available options:
    - list: when used without a wheel name, list all
    the available wheels. when used with a wheel name, it list the wheel content

    - spin: require a wheel name, it randomly picks one of its content

    - add: require a wheel name and a content name, add the specified element to the specified wheel so it may be potentially chosen in future spins

    - remove: require a wheel name and a content name, remove the specified element from the specified wheel so it may not be chosen in future spins

    - help: it explai- wait...
    '''
        await ctx.send(toSend)
    elif action == "list":
        if wheel_name == "Empty":
            toSend = "The available wheels are: " + str(wheelNames)
            await ctx.send(toSend)
        elif wheel_name in wheelNames:
            await ctx.send("The wheel contains: " + str(aWheel.getContent()))
        else:
            await ctx.send(
                "Error: The wheel does not exist. type !wheel list to know the available wheels"
            )
    elif action == "spin":
        if wheel_name in wheelNames:
            await ctx.send(aWheel.spin())
        else:
            await ctx.send(
                "Error: The wheel does not exist. type !wheel list to know the available wheels"
            )
    elif action == "add":
        if wheel_name in wheelNames:
            aWheel.addContent(content_name)
            try:
                wheelM.updateWheel(aWheel, server)
            except:
                await ctx.send(
                    "Error: There was a problem when trying to save the change"
                )
            await ctx.send(content_name +
                           " was added to the wheel successfully")
        else:
            await ctx.send(
                "Error: There was a problem when trying to save the change")
    elif action == "remove":
        if wheel_name in wheelNames:
            aWheel.removeContent(content_name)
            try:
                wheelM.updateWheel(aWheel, server)
            except:
                await ctx.send(
                    "Error: There was a problem when trying to save the change"
                )
            await ctx.send(content_name +
                           " was removed from the wheel successfully")
        else:
            await ctx.send(
                "Error: Wheel not found, try !wheel list to know the name of the wheels"
            )


@slash.slash(
    name="roll",
    description="Allow to roll dices. support multiple dices and modifiers",
    options=[
        create_option(
            name="dice",
            description="enter the value of the dices, exemple: 2d20+3",
            required=True,
            option_type=3)
    ])
async def roll(ctx, dice):
    message = diceRolls.roll_dice(dice)
    if message != None:
        await ctx.send("You rolled: " + dice + "\n" +
                       diceRolls.roll_dice(dice))
    else:
        await ctx.send("A error as occured, call the nearest programer")
        print(message)


@slash.slash(
    name="oc",
    description=
    "Return the discord link of the message describing the specified OC",
    options=[
        create_option(
            name="dice",
            description=
            "Name of the OC you desire to find or define its location",
            required=True,
            option_type=3),
        create_option(name="link",
                      description="link to the oc's location",
                      required=True,
                      option_type=3)
    ])
async def oc(ctx, oc_name):
    pass


keep_alive.keep_alive()
try:
    client.run(os.getenv('TOKEN2'))
except discord.errors.HTTPException:
    print("\nBLOCKED BY RATE LIMITS\nRESTARTING NOW\n")
    web.addAttempt(web)
    status = "Offline"
    web.updateStat(web, status)
    system("python restarter.py")
    system('kill 1')
