import random
import asyncio
import aiohttp
import discord
from discord import Game
from discord.ext.commands import Bot
import time
from discord.ext import commands
from discord.utils import get
import requests
import json
import os
import os.path
import threading
import discord.utils
import pyimgflip

BOT_PREFIX = ("~", ">")
TOKEN = "YourToken"

client = Bot(command_prefix=BOT_PREFIX)
client.remove_command("help")

@client.command(name='8ball',
                description="Answers a yes/no question.",
                brief="Answers from the beyond.",
                aliases=['eight_ball', 'eightball', '8-ball'],
                pass_context=True)
async def eight_ball(context):
    await client.send_typing(context.message.channel)
    possible_responses = [
        'No! Of course not!',
        'Likely to happen',
        'Too hard to tell',
        'Quite possibly',
        'Yes.Definitely',
    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)
@client.command(name='internetroasts',
description="This command will roast you!",
                brief="It will send a roast from the internet, mentioning you.",
                aliases=['internetroast', 'roast', 'roasts'],
                pass_context=True)
async def eight_ball(context):
    possible_responses_roast = [
        "You're as useless as the 'ueue' in `queue`",
        "Some day you’ll go far—and I really hope you stay there",
        "Sometimes it’s better to keep your mouth shut and give the impression that you’re stupid than open it and remove all doubt",
        "Do yourself a favor and ignore anyone who tells you to be yourself. Bad idea in your case",
        "I don’t know what your problem is, but I’m guessing it’s hard to pronounce",
        "There are some remarkably dumb people in this world. Thanks for helping me understand that",
        "You always bring me so much joy—as soon as you leave the room",
        "I believed in evolution until I met you",
    ]
    await client.send_typing(context.message.channel)
    await client.say(random.choice(possible_responses_roast) + ", " + context.message.author.mention)

@client.command(pass_context=True)
async def invite(ctx):
    await client.send_typing(ctx.message.channel)
    embed = discord.Embed(title="INVITE:", description="`Invite Alvi Bot:` http://tiny.cc/invitealvi "
                  "  `Our server:` http://tiny.cc/alviserver", color=0xe91e63)
    invitemessagedm2="To join our server:"
    invitemessagedm="*To invite Alvi Bot to your server, click on this link: * http://tiny.cc/invitealvi ."
    await client.say(embed=embed)
    await client.send_message(ctx.message.author,invitemessagedm)

@client.command(description="A cat gif.",
                brief="This command will send a cat gif to the channel.",
                aliases=['cats', 'catgif', 'ct'],
                pass_context=True)
async def cat(ctx):
    await client.send_typing(ctx.message.channel)
    await client.say("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")


@client.command(description="It will square the number.",
                brief="After ~square , write your number and the bot will square it.",
                aliases=['tothepoweroftwo', 'squares', 'timesbyitself'],
                pass_context=True)
async def square(number):
    await client.send_typing(ctx.message.channel)
    squared_value = int(number) * int(number)
    await client.say(str(number) + " squared is " + str(squared_value))


@client.event
async def on_ready():
    await client.change_presence(game=Game(name="~help ¦ ~invite", url="https://www.twitch.tv/avibn", type=1))
    print("Logged in as " + client.user.name)
    print("Currently active on " + str(len(client.servers)) + " servers.")
    while True:
        await client.change_presence(game=Game(name="~help ¦ ~invite", url="https://www.twitch.tv/avibn", type=1))
        # await client.change_presence(game=Game(name="..help ¦ ..invite", type=3))
        await asyncio.sleep(20)
        await client.change_presence(game=Game(name=" {} Guilds.".format(len(client.servers)), url="https://www.twitch.tv/avibn", type=1))
        # await client.change_presence(game=Game(name="{} guilds".format(len(client.servers)), type=3))
        await asyncio.sleep(10)
    await asyncio.sleep(600)

@client.command(pass_context = True)
async def bitcoin(ctx):
    async with aiohttp.ClientSession() as b:
        async with b.get("https://api.coindesk.com/v1/bpi/currentprice/BTC.json") as r:

            data = await r.json()
            embed = discord.Embed(title="Bitcoin",
                                  description="Price: ${}".format(data['bpi']['USD']['rate']),
                                  color=0xe91e63)
            embed.set_author(name="Alvi Bot" ,icon_url="http://bitcoinist.com/wp-content/uploads/2018/03/btc1.png")

            await client.say(embed=embed)


@client.command()
async def add(one: int, two: int):
    await client.send_typing(ctx.message.channel)
    await client.say(str(one) + " plus " + str(two) + " is " + str(one + two))

@client.command(pass_context=True)
async def info(ctx, user: discord.Member = None):
    await client.send_typing(ctx.message.channel)
    if user is None:
        embed = discord.Embed(title="{}:".format(ctx.message.author.name), description="Here's some info!", color=0xe91e63)
        embed.add_field(name="Name:", value=ctx.message.author.name, inline=True)
        embed.add_field(name="ID:", value=ctx.message.author.id, inline=True)
        embed.add_field(name="Status:", value=ctx.message.author.status, inline=True)
        embed.add_field(name="Account Created: ", value=ctx.message.author.created_at, inline=True)
        embed.add_field(name="Nickname:  ", value=ctx.message.author.display_name, inline=True)
        embed.add_field(name="H.R:", value=ctx.message.author.top_role)
        embed.add_field(name="Joined", value=ctx.message.author.joined_at)
        embed.set_thumbnail(url=ctx.message.author.avatar_url)
        await client.say(embed=embed)
    else:
        embed = discord.Embed(title="{}:".format(user.name), description="Here's some info!", color=0xe91e63)
        embed.add_field(name="Name:", value=user.name, inline=True)
        embed.add_field(name="ID:", value=user.id, inline=True)
        embed.add_field(name="Status:", value=user.status, inline=True)
        embed.add_field(name="Account Created: ", value=user.created_at, inline=True)
        embed.add_field(name="Nickname:  ", value=user.display_name, inline=True)
        embed.add_field(name="H.R:", value=user.top_role)
        embed.add_field(name="Joined", value=user.joined_at)
        embed.set_thumbnail(url=user.avatar_url)
        await client.say(embed=embed)

@client.command(pass_context=True)
async def avatar(ctx, user: discord.Member = None):
    await client.send_typing(ctx.message.channel)
    if user is None:
        embed = discord.Embed(title="{}'s Avatar:".format(ctx.message.author.name), color=0xe91e63)
        embed.set_image(url=ctx.message.author.avatar_url)
        embed.add_field(name="Link: ", value=ctx.message.author.avatar_url, inline=True)
        embed.set_footer(text="Requested by {}".format(ctx.message.author))
    else:
        embed = discord.Embed(title="{}'s Avatar:".format(user.name), color=0xe91e63)
        embed.set_image(url=user.avatar_url)
        embed.add_field(name="Link: ", value=user.avatar_url, inline=True)
        embed.set_footer(text="Requested by {}".format(ctx.message.author))

    await client.say(embed=embed)

@client.command(pass_context = True)
@commands.has_permissions(kick_members=True)
async def kick(ctx, userName: discord.User):
    try:
        await client.send_typing(ctx.message.channel)
        await client.send_message("You have been kicked out from: {}")
        await client.kick(userName)
        await client.say(":wave: **User Has Been Kicked!** :wave:")
        pass
    except:
        await client.say("Hey {} . Something went wrong in the process! \n"
                         "Make sure you mention the user and it cannot be a bot(e.g. ~kick @avib)."
                         " Remember, to kick a user you **MUST have kick members permission.**".format(ctx.message.author.mention))

@client.command(pass_context = True)
@commands.has_permissions(ban_members=True)
async def ban(ctx, userName: discord.User):
    await client.send_typing(ctx.message.channel)
    await client.ban(userName)
    await client.say(":wave: :wave: __**User Has Been Banned!**__")
    pass

@client.command(pass_context = True)
@commands.has_permissions(kick_members=True)
async def warn(ctx, userName: discord.User, *, message:str):
    await client.send_typing(ctx.message.channel)
    await client.send_message(userName, "```You have been warned for: {}```".format(message))
    #await client.send_message(userName, "`{}`".format(message))
    await client.say(":warning: __**{0} Has Been Warned!**__ :warning: Reason:{1} ".format(userName,message))
    pass

@client.command(name = "dice",
                pass_context=True)
async def eight_ball(context):
    await client.send_typing(context.message.channel)
    possible_responses = [
        'You dice rolled 1',
        'You dice rolled 2',
        'You dice rolled 3',
        'You dice rolled 4',
        'You dice rolled 5',
        'You dice rolled 6',
    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)

# Thanks to https://stackoverflow.com/questions/43465082/python-discord-py-delete-all-messages-in-a-text-channel?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa

@client.command(pass_context = True , aliases=['purge', 'clean', 'delete'])
@commands.has_permissions(manage_messages=True)
async def clear(ctx, number):
    mgs = []
    numberr = int(number)+1
    number1 = numberr-1
    async for x in client.logs_from(ctx.message.channel, limit = numberr):
        mgs.append(x)
    await client.delete_messages(mgs)
    botmessage = await client.say("{} messages were purged.".format(number1))
    await asyncio.sleep(5)
    await client.delete_message(botmessage)


@client.command(pass_context = True , aliases=['lpurge', 'lp', 'longclear'])
@commands.has_permissions(manage_messages=True)
async def longpurge(ctx, nmbr):
    number = int(nmbr)
    counter = 0
    async for x in client.logs_from(ctx.message.channel, limit = number):
        if counter < number:
            await client.delete_message(x)
            counter += 1
            await asyncio.sleep(1.2)
    await client.say("{} messages were purged.".format(nmbr))

@client.command(pass_context =True)
async def ping(ctx):
    await client.send_typing(ctx.message.channel)
    pingtime = time.time()
    e = discord.Embed(title="Pinging...", colour=0xFF0000)
    msg = await client.say(embed=e)
    ping = time.time() - pingtime
    await asyncio.sleep(1.5)
    complete = "Ping: %.01f seconds :ping_pong: " % ping
    em = discord.Embed(title=complete, colour=0xFF0000)
    await client.edit_message(msg, embed=em)

@client.command()
@commands.has_permissions(manage_messages=True)
async def spam(ctx , times : int, * , content):
    await client.send_typing(ctx.message.channel)
    for i in range(times):
        await client.say(content)

@client.command(pass_context=True)
@commands.has_permissions(send_tts_messages=True)
async def ohyeah(ctx):
    await client.send_typing(ctx.message.channel)
    await client.say("Oh Yeah!", tts=True)
#TODO : Add reminders to a database.
@client.command(pass_context = True , aliases=['remind', 'rm', 'reminder'])
async def remindme(ctx, time:int , *, reminder:str):
    await client.send_typing(ctx.message.channel)
    #await client.send_message(userName, "`{}`".format(message))
    botmsg = await client.say("**{0}, You have set a reminder.Your reminder is: ** `{1}`  (Your reminder will start in 5seconds).".format(ctx.message.author,reminder))
    await client.delete_message(ctx.message)
    await asyncio.sleep(5)
    await client.delete_message(botmsg)
    await asyncio.sleep(time)
    await client.send_message(ctx.message.author, "https://media.giphy.com/media/xU9TT471DTGJq/giphy.gif" )
    await client.send_message(ctx.message.author, ":clock: :clock: :clock: ```Your reminder:{}``` :clock: :clock: :clock: ".format(reminder))
    pass

@client.command(pass_context=True)
async def roles(context):
    await client.send_typing(context.message.channel)
    roles = context.message.server.roles
    result = "**Roles on this server: **"
    for role in roles:
        result += role.name + ", "
    await client.say(result.replace("@everyone",'')) #So it doesn't ping everyone. :D

@client.command(pass_context=True)
async def help(ctx):
    embed1 = discord.Embed(title="Commands:", description="**Moderation:**\n"
                                                          "**~purge**"
                                                          " - Purge messages (Range:1-100).\n"
                                                          "**~longpurge**"
                                                          " - Purge messages (Range:1-...).\n"
                                                          "**~kick**"
                                                          " - Kick a user.\n"
                                                          "**~ban**"
                                                          " - Ban a user.\n"
                                                          "**~info**"
                                                          " - Finds information about a user.\n"
                                                          "**~warn**"
                                                          " - Warns a user.\n"
                                                          "**~setup**"
                                                          " - This is only if you want to setup your server!\n"
                                                          "Utilities:"
                                                          ":globe_with_meridians:\n"
                                                          "**~at**"
                                                          " - Alvi Tags are preset tags which can be used by any user.\n"
                                                          "**~poll**"
                                                          " - Poll system. E.g. ~poll 2 Which bot is better? Alvi Bot or MEE6?\n"
                                                          "**~report**"
                                                          " - Report an issue or user to the developers. These reports will be sent directly to the developers.\n"
                                                          "**~suggest**"
                                                          " - Suggest for Alvi Bot! It will be sent to the developers.\n", color=0xe91e63)

    embed1.set_footer(text = "Page 1 / 4")
    await client.delete_message(ctx.message)
    clientsays = await client.say(embed=embed1)
    try:
        await client.add_reaction(clientsays, '\U0001F536')
        await client.add_reaction(clientsays, '\U0001F537')
        await client.add_reaction(clientsays, '\U0001F534')
        await client.add_reaction(clientsays, '\U0001F535')
    except:
        await client.say("An error occurred whilst adding the reactions!"
                         " Please try again and if this keeps on occurring,"
                         " report the issue using `~report {your issue}`. Thank You!")


    embed2 = discord.Embed(title="Commands:", description="**Fun:**\n"
                                                          "**~cat**"
                                                          " - A cat gif.\n"
                                                          "**~battle**"
                                                          " - Battle between two players(you must mention the two).\n"
                                                          "**~roast**"
                                                          " - Alvi Bot will roast you.\n"
                                                          "**~dice**"
                                                          " - Rolls a dice.\n"
                                                          "**~rps**"
                                                          " - Rock paper scissors! E.g.~rps rock.\n"
                                                          "**~ohyeah**"
                                                          " - Sends a tts message saying oh yeah(must have tts permissions).\n"
                                                          "**~meme**"
                                                          " - Info on how to generate a meme with Alvi Bot!", color=0xe91e63)

    embed2.add_field(name="More commands", value="Coming Soon!",inline=False)
    embed2.set_footer(text="Page 2 / 4")

    embed3 = discord.Embed(title="Commands:", description="**COMING SOON!**",
                           color=0xe91e63)
    embed3.set_footer(text="Page 3 / 4")
    embed4 = discord.Embed(title="Commands:", description="**COMING SOON!**",
                           color=0xe91e63)
    embed4.set_footer(text="Page 4 / 4")


    while True:
        reaction, user = await client.wait_for_reaction(['\U0001F536', '\U0001F537', '\U0001F534', '\U0001F535'],
                                                        message=clientsays,
                                                        check=lambda reaction, user: user != client.user)
        if reaction.emoji == "\U0001F536":
            await client.remove_reaction(emoji='\U0001F536', member=ctx.message.author, message=clientsays)
            second_message = await client.edit_message(clientsays, embed=embed1)
        elif reaction.emoji == "\U0001F537":
            await client.remove_reaction(emoji='\U0001F537', member=ctx.message.author, message=clientsays)
            await client.edit_message(clientsays , embed=embed2)
        elif reaction.emoji == "\U0001F534":
            await client.remove_reaction(emoji='\U0001F534', member=ctx.message.author, message=clientsays)
            await client.edit_message(clientsays , embed=embed3)
        elif reaction.emoji == "\U0001F535":
            await client.remove_reaction(emoji='\U0001F535', member=ctx.message.author, message=clientsays)
            await client.edit_message(clientsays , embed=embed4)
@client.command(pass_context=True)
async def help2(ctx):
    await client.send_typing(ctx.message.channel)
    help2msg = await client.say("Help2 (the second documetation for help) will be available soon. `This message will automatically delete in "
                     "7 seconds.`")
    await asyncio.sleep(7)
    await client.delete_message(help2msg)
@client.command(pass_context=True)
async def setup(ctx):
    await client.send_typing(ctx.message.channel)
    await client.say("**Are you sure you want to set up your server?** Setting up your server"
                     " would add many channels and roles. Please be aware that you won't be able"
                     " to undo this command. The only way would be for you to delete all the changes"
                     " that the bot has done. Setting up is ideal for new servers. If you want to"
                     " proceed, please type `~setupconfirm` (**You must have administrator permissions!**). Thank You.")

@client.command(pass_context=True)
@commands.has_permissions(administrator = True)
async def setupconfirm(ctx):
    await client.send_typing(ctx.message.channel)
    hoho = await client.say("**Ok! Setting Up............**")
    await client.create_channel(ctx.message.server, 'Discussion', type=discord.ChannelType.text)
    # channeldicussion = client.get_channel("Discussion")
    # await client.send_message
    await client.create_channel(ctx.message.server, 'off-topic', type=discord.ChannelType.text)
    await client.create_channel(ctx.message.server, 'Games', type=discord.ChannelType.text)
    await client.create_channel(ctx.message.server, 'Programming', type=discord.ChannelType.text)
    await client.create_channel(ctx.message.server, 'Bot-Commands', type=discord.ChannelType.text)
    await client.create_channel(ctx.message.server, 'Partners', type=discord.ChannelType.text)
    await client.create_channel(ctx.message.server, 'Help', type=discord.ChannelType.text)
    await client.create_channel(ctx.message.server, 'suggestions', type=discord.ChannelType.text)
    await client.create_channel(ctx.message.server, 'lobby', type=discord.ChannelType.text)
    await client.create_channel(ctx.message.server, 'News', type=discord.ChannelType.text)
    await client.create_channel(ctx.message.server, 'Self-Promo', type=discord.ChannelType.text)
    await client.create_channel(ctx.message.server, 'Staff-Chat', type=discord.ChannelType.text)
    #Voice:
    await client.create_channel(ctx.message.server, 'General 1', type=discord.ChannelType.voice)
    await client.create_channel(ctx.message.server, 'General 2', type=discord.ChannelType.voice)
    await client.create_channel(ctx.message.server, 'General 3', type=discord.ChannelType.voice)
    await client.create_channel(ctx.message.server, 'Music', type=discord.ChannelType.voice)
    await client.create_channel(ctx.message.server, 'Gaming', type=discord.ChannelType.voice)
    await client.create_channel(ctx.message.server, 'Gaming', type=discord.ChannelType.voice)
    await client.create_channel(ctx.message.server, 'Help', type=discord.ChannelType.voice)
    await client.edit_message(hoho , "**Finished Setup!**")

@client.command(pass_context=True)
async def users(ctx):
    await client.send_typing(ctx.message.channel)
    alvibotxp = 0
    serverCount = 0
    for server in client.servers:
        serverCount += 1
        alvibotxp += len(server.members)
    embed123 = discord.Embed(title="Total Number of users on all servers I'm connected to:", description="{} users.".format(alvibotxp), color=0xe91e63)
    await client.say(embed=embed123)

@client.command(pass_context=True)
async def servers(ctx):
    await client.send_typing(ctx.message.channel)
    alvibotxp = 0
    serverCount = 0
    for server in client.servers:
        serverCount += 1
        alvibotxp += len(server.members)
    embed123 = discord.Embed(title="Total Number of servers I'm connected to:", description="{} servers".format(serverCount), color=0xFF0000)
    await client.say(embed=embed123)


@client.command(pass_context=True)
async def poll(ctx,reaction : int,*,messg):
    #TODO: split the message to find out how many options there are. Then use that for reaction:int instead of users having to type that.
    await client.send_typing(ctx.message.channel)
    embed123 = discord.Embed(title="Poll:", description="{}".format(messg), color=0xe91e63)
    await client.delete_message(ctx.message)
    clientsayss = await client.say(embed=embed123)
    if reaction == 2:
        await client.add_reaction(clientsayss, '\U0001F535')
        await client.add_reaction(clientsayss, '\U0001F534')
    if reaction == 3:
        await client.add_reaction(clientsayss, '\U0001F535')
        await client.add_reaction(clientsayss, '\U0001F534')
        await client.add_reaction(clientsayss, '\U000026AB')
    if reaction == 4:
        await client.add_reaction(clientsayss, '\U0001F535')
        await client.add_reaction(clientsayss, '\U0001F534')
        await client.add_reaction(clientsayss, '\U000026AB')
        await client.add_reaction(clientsayss, '\U000026AA')

@client.command(pass_context=True)
async def at(ctx):
    await client.send_typing(ctx.message.channel)
    embed123 = discord.Embed(title="Alvi Tags", description="Alvi Tags are preset tags which can be used by anyone on the server. There are many tags "
                                                            "from Programming to Gaming.", color=0xe91e63)
    embed123.add_field(name = "Tags:",value="(Remember to not have spaces in between `at` and the command).", inline=True)
    embed123.add_field(name = "~atlongcode",value="A reminder not to post long code.  ", inline=True)
    embed123.add_field(name = "~atdb",value="What is a database?", inline=True)
    embed123.add_field(name = "~atpy",value="What is python?", inline=True)
    embed123.add_field(name = "Coming Soon!",value="Coming soon!", inline=True)
    embed123.add_field(name = "Coming Soon!",value="Coming soon!", inline=True)
    await client.delete_message(ctx.message)
    await client.say(embed=embed123)

@client.command(pass_context=True)
async def atlongcode(ctx):
    await client.send_typing(ctx.message.channel)
    embed123 = discord.Embed(title="Long Codes", description="Please don't flood this chat with long codes. Only post code directly if it is short."
                                                             " You can use websites such as https://hastebin.com/ , https://gist.github.com/ or "
                                                             "even http://collabedit.com/ to paste your code and the post the link onto this chat.", color=0xe91e63)
    # embed123.add_field(name = " ",value="(1: :large_blue_circle: ) , (2: :red_circle: ) , (3: :black_circle: ) , (4: :white_circle: )", inline=False)
    await client.delete_message(ctx.message)
    await client.say(embed=embed123)

@client.command(pass_context=True)
async def atdb(ctx):
    await client.send_typing(ctx.message.channel)
    embed123 = discord.Embed(title="Database", description="Defenition: `a structured set of data held in a computer, especially one that is accessible in various ways.`", color=0xe91e63)
    # embed123.add_field(name = " ",value="(1: :large_blue_circle: ) , (2: :red_circle: ) , (3: :black_circle: ) , (4: :white_circle: )", inline=False)
    await client.delete_message(ctx.message)
    await client.say(embed=embed123)
@client.command(pass_context=True)
async def atpy(ctx):
    await client.send_typing(ctx.message.channel)
    embed123 = discord.Embed(title="Python", description="What is python? (from python website): `Python is an interpreted, object-oriented, "
                                                         "high-level programming language with dynamic semantics. Its high-level built in data "
                                                         "structures, combined with dynamic typing and dynamic binding, make it very attractive for "
                                                         "Rapid Application Development, as well as for use as a scripting or glue language to connect "
                                                         "existing components together. Python's simple, easy to learn syntax emphasizes readability and "
                                                         "therefore reduces the cost of program maintenance. Python supports modules and packages, which "
                                                         "encourages program modularity and code reuse. The Python interpreter and the extensive "
                                                         "standard library are available in source or binary form without charge for all major platforms, "
                                                         "and can be freely distributed.` https://www.python.org/", color=0xe91e63)
    await client.delete_message(ctx.message)
    await client.say(embed=embed123)

@client.command(name='playerbattle',
                aliases=['battle' ,'fight' , 'Fight' , 'Battle'],
                pass_context=True)
async def battlebattle(ctx, user: discord.Member , user2: discord.Member):
    await client.send_typing(ctx.message.channel)
    #I know, I know this is a messy way to write code.
    #I will clean it up SOON!
    possible_responses = [
        '{0} hit {1} with a frying pan!'.format(user.mention, user2.mention),
        '{0} hit {1} with a frying pan!'.format(user2.mention, user.mention),
        '{0} shot {1} with pistol !'.format(user2.mention, user.mention),
        '{0} shot {1} with pistol !'.format(user.mention, user2.mention),
        '{0} ran over {1} with a car!'.format(user.mention, user2.mention),
        '{0} ran over {1} with a car!'.format(user2.mention, user.mention),
        '{0} shot {1} with an RPG!'.format(user2.mention, user.mention),
        '{0} shot {1} with an RPG!'.format(user.mention, user2.mention),
        '{0} kicked {1}!'.format(user.mention, user2.mention),
        '{0} kicked {1}!'.format(user2.mention, user.mention),
        '{0} punched {1}!'.format(user2.mention, user.mention),
        '{0} punched {1}!'.format(user.mention, user2.mention),
        '{0} slapped {1}!'.format(user.mention, user2.mention),
        '{0} slapped {1}!'.format(user2.mention, user.mention),
        '{0} bellyflopped {1}!'.format(user.mention, user2.mention),
        '{0} bellyflopped {1}!'.format(user2.mention, user.mention),
        '{0} dropped {1}!'.format(user.mention, user2.mention),
        '{0} dropped {1}!'.format(user2.mention, user.mention),
        '{0} sliced {1}!'.format(user.mention, user2.mention),
        '{0} sliced {1}!'.format(user2.mention, user.mention),
        '{0} threw a golf ball at {1}!'.format(user.mention, user2.mention),
        '{0} threw a golf ball at {1}!'.format(user2.mention, user.mention),
        '{0} missed {1}!'.format(user.mention, user2.mention),
        '{0} missed {1}!'.format(user2.mention, user.mention),
    ]

    embed123 = discord.Embed(title="Battle", description="Who will win the game? {0} or {1} .".format(user,user2), color=0xe91e63)
    embed123.set_image(url = "https://thumbs.dreamstime.com/b/cartoon-boxing-vector-illustration-30595559.jpg")
    # embed123.add_field(name = ":fist: ",value="{}".format(random.choice(possible_responses)), inline=True)
    embed12 = discord.Embed(title="FIGHT!", description=":fist: :fist:".format(user,user2), color=0xe91e63)
    embed12.add_field(name = "Battle: ",value="{}".format(random.choice(possible_responses)), inline=True)
    embed13 = discord.Embed(title="FIGHT!", description=":fist: :fist:".format(user,user2), color=0xe91e63)
    embed13.add_field(name = "Battle: ",value="{}".format(random.choice(possible_responses)), inline=True)
    embed14 = discord.Embed(title="FIGHT!", description=":fist: :fist:".format(user,user2), color=0xe91e63)
    embed14.add_field(name = "Battle: ",value="{}".format(random.choice(possible_responses)), inline=True)
    embed15 = discord.Embed(title="FIGHT!", description=":fist: :fist:".format(user,user2), color=0xe91e63)
    embed15.add_field(name = "Battle: ",value="{}".format(random.choice(possible_responses)), inline=True)
    embed16 = discord.Embed(title="FIGHT!", description=":fist: :fist:".format(user,user2), color=0xe91e63)
    embed16.add_field(name = "Battle: ",value="{}".format(random.choice(possible_responses)), inline=True)
    embed17 = discord.Embed(title="FIGHT!", description=":fist: :fist:".format(user,user2), color=0xe91e63)
    embed17.add_field(name = "Battle: ",value="{}".format(random.choice(possible_responses)), inline=True)
    embed18 = discord.Embed(title="FIGHT!", description=":fist: :fist:".format(user,user2), color=0xe91e63)
    embed18.add_field(name = "Battle: ",value="{}".format(random.choice(possible_responses)), inline=True)
    embed19 = discord.Embed(title="FIGHT!", description=":fist: :fist:".format(user,user2), color=0xe91e63)
    embed19.add_field(name = "Battle: ",value="{}".format(random.choice(possible_responses)), inline=True)
    em = discord.Embed(title="The winner is........", description="{}".format(random.choice([user,user2])), color=0xe91e63)
    em.set_footer(text="Requested by {}".format(ctx.message.author))

    battlemsg = await client.say(embed=embed123)
    await asyncio.sleep(3)
    await client.edit_message(battlemsg, embed=embed12)
    await asyncio.sleep(2)
    await client.edit_message(battlemsg, embed=embed13)
    await asyncio.sleep(2)
    await client.edit_message(battlemsg, embed=embed14)
    await asyncio.sleep(2)
    await client.edit_message(battlemsg, embed=embed15)
    await asyncio.sleep(2)
    await client.edit_message(battlemsg, embed=embed16)
    await asyncio.sleep(2)
    await client.edit_message(battlemsg, embed=embed17)
    await asyncio.sleep(2)
    await client.edit_message(battlemsg, embed=embed18)
    await asyncio.sleep(2)
    await client.edit_message(battlemsg, embed=embed19)
    await asyncio.sleep(2)
    await client.edit_message(battlemsg, embed=em)

#Meme gen~~~~~~~~~~~

@client.command(name='meme',
                aliases=['memes', 'mem', 'mems', 'mene'],
                pass_context=True)
async def memeinfo(ctx):
    await client.send_typing(ctx.message.channel)
    embed125 = discord.Embed(title="MEMES", description="Meme commands:", color=0xe91e63)
    embed125.add_field(name="~irl", value="Generate a random meme from meme_irl.", inline=False)
    embed125.add_field(name="~memegen", value="Generate your own meme. E.g.`~memegen alvi alvi2`, where `alvi` is the top text and `alvi2` is the bottom text."
                                               " The system currently on supports two words, so please adjust (you could put a symbol instead of space such as"
                                               " `.` or `-`.   ", inline=False)
    embed125.set_footer(text="Requested by {}".format(ctx.message.author))
    await client.say(embed=embed125)

@client.command(name='irl',
                aliases=['meme_irl', 'memirl', 'irll'],
                pass_context = True)
async def memeirl(ctx):
    async with aiohttp.ClientSession() as cs:
        async with cs.get("https://api.reddit.com/r/me_irl/random") as r:
            data = await r.json()
            embed = discord.Embed(title="__Alvi Bot__",
                                  description="Meme:",
                                  color=0xe91e63)
            embed.set_image(url = data[0]["data"]["children"][0]["data"]["url"])

            await client.say(embed=embed)
@client.command(name='memegen',
                aliases=['genmeme' ,'memeg' , 'gmeme' , 'gm'],
                pass_context=True)
async def generatememe(ctx,top:str,bottom:str):
    await client.send_typing(ctx.message.channel)
    api = pyimgflip.Imgflip(username='nicetry', password='verynicetry')
    memes = api.get_memes()
    meme = random.choice(memes)
    print("Generating a meme from template: " + meme.name)
    result = api.caption_image(meme, top, bottom)
    # embed = discord.Embed(title="Your Choice:", description=rpss, color=0xe91e63)
    await client.say("Meme available at URL: " + result['url'])


#~~~~~~~~~~~~~~~~~~~

@client.command(pass_context = True)
async def report(ctx,*,reportmsg):
    embed1 = discord.Embed(title="Report:", description="{0} , {1} , {2}".format(ctx.message.author,ctx.message.author.mention, ctx.message.author.id), color=0xe91e63)
    embed1.add_field(name="Description:",
                       value="{}".format(reportmsg), inline=False)
    embed1.set_footer(text="This is a report!")
    hello = await client.send_message(client.get_channel('447816959648727071'), embed=embed1)
    await client.delete_message(ctx.message)
    embed12 = discord.Embed(title="Report:", description="By user : {0} , {1} , {2}".format(ctx.message.author,ctx.message.author.mention, ctx.message.author.id), color=0xe91e63)
    embed12.add_field(name="Description:",
                       value="{}".format(reportmsg), inline=False)
    embed12.set_footer(text="Remember this is a report and will get sent directly"
                            " to the developers. If these messages contain spam "
                            "or anything inappropriate, the user will get banned from accessing"
                            " the bot and our servers.")
    await client.say(embed=embed12)

@client.command(pass_context = True)
async def suggest(ctx,*,reportmsg):
    embed1 = discord.Embed(title="SUGGESTION", description="{0} , {1} , {2}".format(ctx.message.author,ctx.message.author.mention, ctx.message.author.id), color=0xe91e63)
    embed1.add_field(name="Your Suggestion:",
                       value="{}".format(reportmsg), inline=False)
    embed1.set_footer(text="This is a suggestion:")
    hello = await client.send_message(client.get_channel('447816959648727071'), embed=embed1)
    await client.delete_message(ctx.message)
    embed12 = discord.Embed(title="SUGGESTION", description="By user : {0} , {1} , {2}".format(ctx.message.author,ctx.message.author.mention, ctx.message.author.id), color=0xe91e63)
    embed12.add_field(name="Description:",
                       value="{}".format(reportmsg), inline=False)
    embed12.set_footer(text="Hey! This will be sent to the developers. Thanks for "
                            "contributing. We will dm you if necessary.")
    await client.say(embed=embed12)

@client.event
async def on_server_join(server):
    hello = await client.send_message(client.get_channel('448534687376474114'), "Alvi Bot has joined : {}".format(server))

##########################################

@client.command(pass_context = True)
@commands.cooldown(1, 600, commands.BucketType.user)
async def addcredits(ctx):
    await client.send_message(ctx.message.channel, "10 credit added! You had -  `{}` credits! Do `~credits` to see"
                                                   " how many you have now.".format(get_credits(ctx.message.author.id)))
    user_add_credits(ctx.message.author.id, 10)

@client.command(pass_context = True)
async def credits(ctx):
    await client.send_message(ctx.message.channel, "You have -  `{}` credits!\n`To get more credits, you can do"
                                                   " ~addcredits every 5 minutes to get more credits.`".format(get_credits(ctx.message.author.id)))
def user_add_credits(user_id: int, credits: int):
    if os.path.isfile("userscreditscanary.json"):
        try:
            with open('userscreditscanary.json', 'r') as fp:
                userscreditscanary = json.load(fp)
            userscreditscanary[user_id]['credits'] += credits
            with open('userscreditscanary.json', 'w') as fp:
                json.dump(userscreditscanary, fp, sort_keys=True, indent=4)
        except KeyError:
            with open('userscreditscanary.json', 'r') as fp:
                userscreditscanary = json.load(fp)
            userscreditscanary[user_id] = {}
            userscreditscanary[user_id]['credits'] = credits
            with open('userscreditscanary.json', 'w') as fp:
                json.dump(userscreditscanary, fp, sort_keys=True, indent=4)
    else:
        userscreditscanary = {user_id: {}}
        userscreditscanary[user_id]['credits'] = credits
        with open('userscreditscanary.json', 'w') as fp:
            json.dump(userscreditscanary, fp, sort_keys=True, indent=4)


def get_credits(user_id: int):
    if os.path.isfile('userscreditscanary.json'):
        with open('userscreditscanary.json', 'r') as fp:
            userscreditscanary = json.load(fp)
        return userscreditscanary[user_id]['credits']
    else:
        return 0


##########################################

@client.command(pass_context = True)
async def slots(ctx, slotscredit: int):
    if 1 < slotscredit and slotscredit < get_credits(ctx.message.author.id):
        possible_choices = [
            ":apple:",
            ":tangerine:",
            ":banana:",
            ":watermelon:",
            ":grapes:",
            ":strawberry:",
            ":cherries:",
            ":pineapple:",
        ]
        num1 = "{}".format(random.choice(possible_choices))
        num2 = "{}".format(random.choice(possible_choices))
        num3 = "{}".format(random.choice(possible_choices))
        middle_line = "{0} {1} {2}".format(num1,num2,num3)
        slotss = await client.say("{0} {1} {2} \n"
                         "{3} \n"
                         "{4} {5} {5} ".format(random.choice(possible_choices),random.choice(possible_choices),random.choice(possible_choices),middle_line,
                                                 random.choice(possible_choices),random.choice(possible_choices),random.choice(possible_choices))
        )

        if num1==num2==num3:
            winadd = int(slotscredit) * 2
            user_add_credits(ctx.message.author.id, winadd)
            await client.say("Well done! You won, {}! Credits have been added to your account.".format(ctx.message.author.mention))
        else:
            loseminus = int(slotscredit)*(-1)
            user_add_credits(ctx.message.author.id,loseminus)
            await client.say("Unlucky. Try again, {}. The amount of credits you"
                             " put in have been deducted from your account. ".format(ctx.message.author.mention))
    else:
        return await client.say("Something went wrong! `Make sure you put over 1"
                                " credit, you have enough credits in your account and you do not put"
                                " all of your credits in.`")

@client.command(pass_context = True)
async def announcenews(ctx,*,reportmsg):
    if ctx.message.author.id == "268837679884402688":
        embed1 = discord.Embed(title="Alvi Bot Update/Announcement:", description="{}".format(reportmsg), color=0xe91e63)
        embed1.set_footer(text="This was sent by : {}".format(ctx.message.author))
        hello = await client.send_message(client.get_channel('444898825258139648'), embed=embed1)
        hello2 = await client.send_message(client.get_channel('426434956462522370'), embed=embed1)
        await client.delete_message(ctx.message)
        embed12 = discord.Embed(title="News:", description="By user : {0} , {1} , {2}".format(ctx.message.author,ctx.message.author.mention, ctx.message.author.id), color=0xe91e63)
        embed12.add_field(name="Description:",
                           value="{}".format(reportmsg), inline=False)
        await client.say(embed=embed12)
    else:
        return await client.say("Hey! Only the owner , `avib` , can use this command. Sorry!")

@client.command(pass_context = True)
async def dm(ctx, userName: discord.User, *, message:str):
    if ctx.message.author.id == "268837679884402688":
        embed1 = discord.Embed(title="Alvi Bot DM:", description="{}".format(message),
                               color=0xe91e63)
        embed1.set_footer(text="This message was sent by : {}".format(ctx.message.author))
        await client.send_typing(ctx.message.channel)
        await client.send_message(userName, "{}".format(message))
        #await client.send_message(userName, "`{}`".format(message))
    else:
        return await client.say("You are not allowed!")


@client.command(pass_context = True)
async def announcenewsglobal(ctx,channelid,*,reportmsg):
    if ctx.message.author.id == "268837679884402688":
        embed1 = discord.Embed(title="Alvi Bot Update/Announcement:", description="{}".format(reportmsg), color=0xe91e63)
        embed1.set_footer(text="This was sent by : {}".format(ctx.message.author))
        hello = await client.send_message(client.get_channel(channelid), embed=embed1)
        await client.delete_message(ctx.message)
        embed12 = discord.Embed(title="News:", description="By user : {0} , {1} , {2}".format(ctx.message.author,ctx.message.author.mention, ctx.message.author.id), color=0xe91e63)
        embed12.add_field(name="Description:",
                           value="{}".format(reportmsg), inline=False)
        await client.say(embed=embed12)
    else:
        return await client.say("Hey! Only the owner , `avib` , can use this command. Sorry!")

# we hold our flags of who typed here
typed = {}

# every few calls we'll wipe the list for gc purposes
calls = 0

@client.event
async def on_message(message):
    user_id = message.author.id
    await client.process_commands(message)
    user_add_credits(message.author.id , 0)
    # author_level = get_level(user_id)
    # author_xp = get_xp(user_id)

    # # set a flag now that the user did type
    # we use id's because name's and tags can change
    typed[message.author.id] = True


def update_xp():
    # we have to mention that calls is global
    global calls

    # make the next call of update_xp 60 seconds from now
    t = threading.Timer(60.0, update_xp)
    t.start()

    # iterate through our map handing out xp
    for id in typed:
        # only award xp if they spoke! (some may be false)
        if typed[id] == True:
            award_xp(id)
            user_add_xp(id, 1)

        # update the flag to now be false
        typed[id] = False

    # increment our calls
    calls += 1
    # user_add_xp(id, 1)
    if (calls == 10):
        # reset our variable so GC can clean up
        calls = 0
        typed.clear()


def award_xp(id):
    # TODO: update the user's XP wherever you're storing that data
    return


def user_add_xp(user_id: int, xp: int):
    if os.path.isfile("testxpxp.json"):
        try:
            with open('testxpxp.json', 'r') as fp:
                testxpxp = json.load(fp)
            testxpxp[user_id]['xp'] += xp
            with open('testxpxp.json', 'w') as fp:
                json.dump(testxpxp, fp, sort_keys=True, indent=4)
        except KeyError:
            with open('testxpxp.json', 'r') as fp:
                testxpxp = json.load(fp)
            testxpxp[user_id] = {}
            testxpxp[user_id]['xp'] = xp
            with open('testxpxp.json', 'w') as fp:
                json.dump(testxpxp, fp, sort_keys=True, indent=4)
    else:
        testxpxp = {user_id: {}}
        testxpxp[user_id]['xp'] = xp
        with open('testxpxp.json', 'w') as fp:
            json.dump(testxpxp, fp, sort_keys=True, indent=4)


def get_xp(user_id: int):
    if os.path.isfile('testxpxp.json'):
        with open('testxpxp.json', 'r') as fp:
            testxpxp = json.load(fp)
        return testxpxp[user_id]['xp']
    else:
        return 0
def set_level(user_id: int, level: int):
    if os.path.isfile('users.json'):
        with open('users.json', 'r') as fp:
            users = json.load(fp)
        users[user_id]["level"] = level
        with open('users.json', 'w') as fp:
            json.dump(users, fp, sort_keys=True, indent=4)


def get_level(user_id: int):
    if os.path.isfile('users.json'):
        try:
            with open('users.json', 'r') as fp:
                users = json.load(fp)
            return users[user_id]['level']
        except KeyError:
            return 0

@client.command(pass_context=True)
async def xp(ctx):
    await client.send_message(ctx.message.channel, ":link: :round_pushpin: **You have -**  `{}` **XP!**".format(get_xp(ctx.message.author.id)))


# start update loop
update_xp()
client.run(TOKEN)