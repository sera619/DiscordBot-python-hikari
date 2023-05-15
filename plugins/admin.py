import os
import hikari
import lightbulb
import asyncio
import json

from .commands import checkAdmin
from .config import ROLE_HPS_USERS, ROLE_TANK_USERS, SERA_ID, ROLE_DPS_USERS, SHOW_START_EMBED, load_bot_setting, WoWClassHandler
admin_plugin = lightbulb.Plugin('admin')


async def SetGuildRules():
    await asyncio.sleep(2.0)
    print("2Sec waited")
    pass


async def save_bot_setting(t):
    with open('./data/bot-set.txt', 'w') as f:
        f.write(str(t))

### Templates to send ingame role lists to discord channel
async def getTankRoles(ctx: lightbulb.Context):
    isAdmin = await checkAdmin(ctx.author.id, ctx.guild_id)
    if not isAdmin:
        return
    user_string = ""
    for user in ROLE_TANK_USERS:
        user_string += str(user) + "\n"
    new_embed = hikari.Embed(
        title="Tank Role Users",
        description=user_string,
        colour=0x0001a8

    )
    await admin_plugin.bot.rest.create_message(ctx.channel_id, embed=new_embed)

async def getHPSRoles(ctx: lightbulb.Context):
    isAdmin = await checkAdmin(ctx.author.id, ctx.guild_id)
    if not isAdmin:
        return
    user_string = ""
    for user in ROLE_HPS_USERS:
        user_string += str(user) + "\n"
    new_embed = hikari.Embed(
        title="HPS Role Users",
        description=user_string,
        colour=0x009a00

    )
    await admin_plugin.bot.rest.create_message(ctx.channel_id, embed=new_embed)

async def getDPSRoles(ctx: lightbulb.Context):
    isAdmin = await checkAdmin(ctx.author.id, ctx.guild_id)
    if not isAdmin:
        return
    user_string = ""
    for user in ROLE_DPS_USERS:
        user_string += str(user) + "\n"
    new_embed = hikari.Embed(
        title="DPS Role Users",
        description=user_string,
        colour=0xC80000
    )
    await admin_plugin.bot.rest.create_message(ctx.channel_id, embed=new_embed)

async def setupRoles(ctx: lightbulb.Context):
    isAdmin = await checkAdmin(ctx.author.id, ctx.guild_id)
    if not isAdmin:
        return

    base_rolelist = [
        ['[0x41] Developer', 0x9900FF],
        ['[0x41] Moderator', 0x05C4BC],
        ['[0x41] Member', 0xFF7C0A]
    ]
    wow_rolelist = [
        ['[WoW] Deamon Hunter', 0xA330C9],
        ["[WoW] Death Knight", 0xC41F3B],
        ["[WoW] Druid", 0xFF7D0A],
        ["[WoW] Evoker", 0x33937F],
        ["[WoW] Hunter", 0xABD473],
        ["[WoW] Mage", 0x69CCF0],
        ["[WoW] Monk", 0x00FF96],
        ["[WoW] Paladin", 0xF58CBA],
        ["[WoW] Priest", 0xFFFFFF],
        ["[WoW] Rogue", 0xFFF569],
        ["[WoW] Shaman", 0x0070DE],
        ["[WoW] Warlock", 0x9482C9],
        ["[WoW] Warrior", 0xC79C6E]
    ]
    wow_dic = {}

    
    base_dic = {}
    base_count = 0
    for base_role in base_rolelist:
        new_base_role = await admin_plugin.bot.rest.create_role(
            ctx.guild_id,
            name = base_role[0],
            permissions=(
                hikari.Permissions.READ_MESSAGE_HISTORY |
                hikari.Permissions.SPEAK |
                hikari.Permissions.CONNECT |
                hikari.Permissions.USE_VOICE_ACTIVITY
            ),
            colour=base_role[1],
        )
        base_dic[str(base_role[0])] =[str(base_role[1]), f'{new_base_role.id}']
        base_count += 1

    wow_count = 0
    for wow_role in wow_rolelist:
        new_role = await admin_plugin.bot.rest.create_role(
            ctx.guild_id,
            name = wow_role[0],
            permissions=(
                hikari.Permissions.READ_MESSAGE_HISTORY |
                hikari.Permissions.SPEAK |
                hikari.Permissions.CONNECT |
                hikari.Permissions.USE_VOICE_ACTIVITY
            ),
            colour=wow_role[1],
        )
        wow_dic[str(wow_role[0])] = [str(wow_role[1]), f'{new_role.id}']
        wow_count += 1

    
    with open('./data/base_role_id.json', 'w') as f:
        f.write(json.dumps(base_dic, sort_keys=True, indent=4)) 

    with open('./data/wow_role_id.json', 'w') as d:
        d.write(json.dumps(wow_dic, sort_keys=True, indent=4)) 

    return (base_count, wow_count)   

async def delete_roles(ctx:lightbulb.Context):
    if not await checkAdmin(ctx.author.id, ctx.guild_id):
        return
   
    loaded_wow_ids = {}
    with open('./data/wow_role_id.json', 'r') as f:
        loaded_wow_ids = json.load(f)

    loaded_base_ids = {}
    with open('./data/base_role_id.json', 'r') as d:
        loaded_base_ids = json.load(d)    

    base_del_count = 0
    for ke1y, role1 in loaded_base_ids.items():
        await admin_plugin.bot.rest.delete_role(ctx.guild_id, str(role1[1]))
        base_del_count += 1
    
    wow_del_count = 0
    for key2, role2 in loaded_wow_ids.items():
        await admin_plugin.bot.rest.delete_role(ctx.guild_id, str(role2[1]))
        wow_del_count += 1

    os.remove('./data/wow_role_id.json')
    os.remove('./data/base_role_id.json')

    res = f"Finally delete:\n__{base_del_count}x Base-Roles__\n__{wow_del_count}x WoW-Roles__\non your Server!"
    new_embed = hikari.Embed(
        title="Role Delete Complete!",
        description=res,
        colour=0x009a00
    )
    new_embed.set_thumbnail('./image/logo1.png')

    await admin_plugin.bot.rest.create_message(ctx.channel_id, embed=new_embed)


async def create_bot_channel(ctx: lightbulb.Context):
    channels = await admin_plugin.bot.rest.fetch_guild_channels(ctx.guild_id)
    control_exisits = False
    for channel in channels:
        if channel.name == 'bot-commands':
            control_exisits = True


    if not control_exisits:
        control_exisits = True
        #await ctx.edit_last_response('No control channel found, created one.')
        await admin_plugin.bot.rest.create_guild_text_channel(ctx.guild_id, "bot-commands")


async def init_process(ctx: lightbulb.Context):
    await create_bot_channel(ctx)
    await setupRoles(ctx)
    
    new_embed = hikari.Embed(
        title="Initialisation finished!",
        description="The initialisation has been completed.\n\nAll processes have been successfully completed!",
        colour=0x009a00
    )
    new_embed.set_thumbnail('./image/logo1.png')
    return await admin_plugin.bot.rest.create_message(ctx.channel_id, embed=new_embed)

##########################################

@admin_plugin.command
@lightbulb.command('admin', 'Admin commands')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def adminCommands(ctx):
    pass

@adminCommands.child
@lightbulb.command('test', 'Test if you have admin role.')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def adminSendMsg(ctx: lightbulb.Context):
    if not await checkAdmin(ctx.author.id, ctx.guild_id):
        return await ctx.respond("Du bist ein admin")
    else:
        return await ctx.respond("Du bist kein admin")

# create text channel for bot commands (admin)
@adminCommands.child
@lightbulb.command('init', 'Start the first configuration for the bot')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def adminInitBot(ctx: lightbulb.Context):
    if not await checkAdmin(ctx.author.id, ctx.guild_id):
        return
    
    start_msg = f"Start initialisation process!\nThe following tasks are then performed.\n\n\t- Create a bot command channel.\n\t- Create Discord general roles for the bot\n\t- Create Discord roles for the WoW plugin\n\t- Create a database of that roles\n\nThis process will take a few moments, please wait for my message that this process is complete before interacting with me further!\n\n__Please wait...__"
    new_embed = hikari.Embed(
        title="Initialize",
        description=start_msg,
        colour=0x009a00
    )
    new_embed.set_thumbnail("./image/logo1.png")
    await ctx.respond(embed=new_embed)
    await init_process(ctx)



@adminCommands.child
@lightbulb.command('changestart', 'Activate / Deactivate the bot startmessage.')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def changestart(ctx: lightbulb.Context):
    if not await checkAdmin(ctx.author.id, ctx.guild_id):
        return

    load =  load_bot_setting()
    if load == False:
        await save_bot_setting(1)
        await ctx.respond('**Start Output will be shown next start.**')
    else:
        await save_bot_setting(2)
        await ctx.respond("**Start Output will be not shown next start.**")


@adminCommands.child
@lightbulb.command('allroles', "Get all User with choosen ingame role.")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def adminAllRoles(ctx: lightbulb.Context):
    await getTankRoles(ctx)
    await getHPSRoles(ctx)
    await getDPSRoles(ctx)
    await ctx.respond('**Complete Rolelist request done!**')

@adminCommands.child
@lightbulb.command('dpsroles', "Get all user with ingame DPS role")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def adminGetDpsRoles(ctx: lightbulb.Context):
    await getDPSRoles(ctx)
    await ctx.respond('**DPS list request done!**')

@adminCommands.child
@lightbulb.command('tankroles', "Get all user with ingame Tank role")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def adminGetTankRoles(ctx: lightbulb.Context):
    await getTankRoles(ctx)
    await ctx.respond('**Tank list request done!**')

@adminCommands.child
@lightbulb.command('hpsroles', "Get all user with ingame HPS role")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def adminGetHpsRoles(ctx: lightbulb.Context):
    await getHPSRoles(ctx)
    await ctx.respond('**HPS list request done!**')

@adminCommands.child
@lightbulb.command('setuproles', "Create all needed Roles")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def admminSetupRoles(ctx: lightbulb.Context):
    base_role_count, wow_role_count = await setupRoles(ctx)
    res = f"Finally create:\n__{base_role_count}x Basicroles__ and\n__{wow_role_count}x WoW-Roles__\non your Server!"
    new_embed = hikari.Embed(
        title="Role Setup Complete!",
        description=res,
        colour=0x009a00
    )
    new_embed.set_thumbnail('./image/logo1.png')
    return await ctx.respond(embed=new_embed)


@adminCommands.child
@lightbulb.command('deleteroles', "Delete all needed Roles")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def adminDeleteRoles(ctx: lightbulb.Context):
    await ctx.respond(f'Start removing roles, this can take a while please wait...')
    await delete_roles(ctx)


@adminCommands.child
@lightbulb.command('rules', "Set the Rules for your guild and post to your rulechannel")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def setRules(ctx: lightbulb.Context):
    await SetGuildRules()
    await ctx.respond("Rules test command finished")
################################################

def load(bot):
    bot.add_plugin(admin_plugin)