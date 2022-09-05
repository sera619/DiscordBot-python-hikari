import hikari
import miru
import lightbulb
import os

from .config import ROLE_HPS_USERS, ROLE_TANK_USERS, SERA_ID, LoadRoleList, ROLE_DPS_USERS
from dist.customviews import DiceView, RoleView
plugin = lightbulb.Plugin('commands')

@staticmethod
async def checkAdmin(member_id, guild): 
    member = await plugin.bot.rest.fetch_member(guild=guild, user=member_id)
    member_roles = await member.fetch_roles()
    permissions = hikari.Permissions.NONE
    for role in member_roles:
        permissions |= role.permissions
    
    if (permissions and hikari.Permissions.ADMINISTRATOR) == hikari.Permissions.ADMINISTRATOR:
        return True
    else:
        return False



@plugin.listener(hikari.GuildMessageCreateEvent)
async def printMsg(event: hikari.GuildMessageCreateEvent):
    if event.author_id == 1009782142923972659 or not event.content:
        return
    is_admin = await checkAdmin(member_id=event.author_id, guild=event.guild_id)
    #await plugin.bot.rest.create_message(type(event.content), channel=event.channel_id)

    if event.content == "buttons":
        view = DiceView(timeout=5.0)
        message = await event.message.respond("Roll the dice!", components=view.build())
        view.start(message)
        await view.wait()
        return print("All done!")    
    
    if event.content == 'rolecheck':
        view = RoleView(timeout= 5.0)
        message = await event.message.respond("Check you character role.",components=view.build())
        view.start(message)
        await view.wait()
        return print("Rolecheck done!")


    if is_admin and event.content != "buttons":
        return await plugin.bot.rest.create_message(content="Your are a Admin",channel= event.channel_id)
    else:
        return await plugin.bot.rest.create_message(content="You are not a Admin.", channel=event.channel_id)



##########################################

############# CREATE CHAT COMMANDS ############
@plugin.command
@lightbulb.command('ping', 'Say pong!')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await plugin.bot.update_presence(
        status=hikari.Status.ONLINE,
        activity=hikari.Activity(
            name=":keyboard:",
            type=hikari.ActivityType.COMPETING
        )
    )
    await ctx.respond('Pong!')

# create subcommand, start with empty maincommand
# -- create base admin commands group
@plugin.command
@lightbulb.command('admin', 'Admin commands')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def adminCommands(ctx):
    pass

@adminCommands.child
@lightbulb.command('test', 'simple test command')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def adminSendMsg(ctx: lightbulb.Context):
    isAdmin = await checkAdmin(ctx.author.id, ctx.guild_id)
    if isAdmin:
        return await ctx.respond("Du bist ein admin")
    else:
        return await ctx.respond("Du bist kein admin")

@adminCommands.child
@lightbulb.command('dpsroles', "Get all user with DPS role")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def adminGetDpsRoles(ctx: lightbulb.Context):
    isAdmin = await checkAdmin(ctx.author.id, ctx.guild_id)
    if not isAdmin:
        return
    user_string = ""
    for user in ROLE_DPS_USERS:
        user_string += str(user) + "\n"
    new_embed = hikari.Embed(
        title="DPS Role Users",
        description=user_string
    )
    await ctx.respond(embed=new_embed)

@adminCommands.child
@lightbulb.command('tankroles', "Get all user with Tank role")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def adminGetTankRoles(ctx: lightbulb.Context):
    isAdmin = await checkAdmin(ctx.author.id, ctx.guild_id)
    if not isAdmin:
        return
    user_string = ""
    for user in ROLE_TANK_USERS:
        user_string += str(user) + "\n"
    new_embed = hikari.Embed(
        title="Tank Role Users",
        description=user_string
    )
    await ctx.respond(embed=new_embed)

@adminCommands.child
@lightbulb.command('hpsroles', "Get all user with HPS role")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def adminGetHpsRoles(ctx: lightbulb.Context):
    isAdmin = await checkAdmin(ctx.author.id, ctx.guild_id)
    if not isAdmin:
        return
    user_string = ""
    for user in ROLE_HPS_USERS:
        user_string += str(user) + "\n"
    new_embed = hikari.Embed(
        title="HPS Role Users",
        description=user_string
    )
    return await ctx.respond(embed=new_embed)

################################################


# load function required by lightbulb
def load(bot):
    bot.add_plugin(plugin)