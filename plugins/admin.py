import hikari
import lightbulb
import asyncio

from .commands import checkAdmin
from .config import ROLE_HPS_USERS, ROLE_TANK_USERS, SERA_ID, ROLE_DPS_USERS, SHOW_START_EMBED, load_bot_setting
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
    
    channels = await admin_plugin.bot.rest.fetch_guild_channels(ctx.guild_id)
    control_exisits = False
    for channel in channels:
        if channel.name == 'bot-commands':
            control_exisits = True
            return await ctx.respond('NecroBot control text channel already exists.')

    if not control_exisits:
        control_exisits = True
        await ctx.edit_last_response('No control channel found, created one.')
        return await admin_plugin.bot.rest.create_guild_text_channel(ctx.guild_id, "bot-commands")


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
@lightbulb.command('rules', "Set the Rules for your guild and post to your rulechannel")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def setRules(ctx: lightbulb.Context):
    await SetGuildRules()
    await ctx.respond("Rules test command finished")
################################################

def load(bot):
    bot.add_plugin(admin_plugin)