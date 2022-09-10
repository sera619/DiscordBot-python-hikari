import hikari
import lightbulb
import os
import miru
from dist.customviews import ClassView
from plugins.config import SERA_DISCORD_ID, WoWClassHandler
from plugins.config import (
    CLASS_DRUID_LIST,
    CLASS_DK_LIST,
    CLASS_MAGE_LIST,
    CLASS_DH_LIST,
    CLASS_HUNTER_LIST,
    CLASS_PALADIN_LIST,
    CLASS_PRIEST_LIST,
    CLASS_SHAMAN_LIST,
    CLASS_MONK_LIST,
    CLASS_ROGUE_LIST,
    CLASS_WARLOCK_LIST,
    CLASS_WARRIOR_LIST
)

wow_plugin = lightbulb.Plugin('wow', 'World of Warcraft Features')
   

@wow_plugin.listener(hikari.StartedEvent)
async def loadWoWPlugin(event: hikari.StartedEvent):
    WoWClassHandler().LoadClassAll()
    print("WoW Plugin: Classes loaded")

@wow_plugin.listener(hikari.GuildMessageCreateEvent)
async def classCheck(event: hikari.GuildMessageCreateEvent):
    if event.author_id == 1009782142923972659 or not event.content:
        return
    if event.content == "classcheck":
        view = ClassView(timeout= 5.0)
        message = await event.message.respond("Check your ingame class", components=view.build())
        view.start(message)
        await view.wait()

        return print('Classcheck done!')

@wow_plugin.command
@lightbulb.command('wow', 'World of Warcraft Plugin Commands')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def WoWCommands(ctx):
    pass

@WoWCommands.child
@lightbulb.command('dk', 'Shows a list with all DK players.',auto_defer = True)
@lightbulb.implements(lightbulb.SlashSubCommand)
async def ShowDKList(ctx:lightbulb.Context):
    user_string = ""
    for user in CLASS_DK_LIST:
        user_string += str(user) + "\n"
    if user_string == "":
        user_string = "No Hunter DK found."

    new_embed = hikari.Embed(
        title='**All DK Players**',
        description=user_string,
        colour=0xC41E3A
    )
    await ctx.respond(embed=new_embed)

@WoWCommands.child
@lightbulb.command('dh', 'Shows a list with all DK players.',auto_defer = True)
@lightbulb.implements(lightbulb.SlashSubCommand)
async def ShowDHList(ctx:lightbulb.Context):
    user_string = ""
    for user in CLASS_DH_LIST:
        user_string += str(user) + "\n"
    if user_string == "":
        user_string = "No Demon Hunter player found."

    new_embed = hikari.Embed(
        title='**All Demon Hunter Players**',
        description=user_string,
        colour=0xA330C9 
    )
    await ctx.respond(embed=new_embed)

@WoWCommands.child
@lightbulb.command('mage', 'Shows a list with all Mage players.',auto_defer = True)
@lightbulb.implements(lightbulb.SlashSubCommand)
async def ShowMageList(ctx:lightbulb.Context):
    user_string = ""
    for user in CLASS_MAGE_LIST:
        user_string += str(user) + "\n"
    new_embed = hikari.Embed(
        title='**All Mage Players**',
        description=user_string,
        colour=0x3FC7EB 
    )
    await ctx.respond(embed=new_embed),

@WoWCommands.child
@lightbulb.command('druid', 'Shows a list with all Druid players.',auto_defer = True)
@lightbulb.implements(lightbulb.SlashSubCommand)
async def ShowDruidList(ctx:lightbulb.Context):
    user_string = ""
    for user in CLASS_DRUID_LIST:
        user_string += str(user) + "\n"
    if user_string == "":
        user_string = "No Druid player found."

    new_embed = hikari.Embed(
        title='**All Druid Players**',
        description=user_string,
        colour=0xFF7C0A 
    )
    await ctx.respond(embed=new_embed)

@WoWCommands.child
@lightbulb.command('hunter', 'Shows a list with all Hunter players.',auto_defer = True)
@lightbulb.implements(lightbulb.SlashSubCommand)
async def ShowHunterList(ctx:lightbulb.Context):
    user_string = ""
    for user in CLASS_HUNTER_LIST:
        user_string += str(user) + "\n"
    if user_string == "":
        user_string = "No Hunter player found."
    new_embed = hikari.Embed(
        title='**All Hunter Players**',
        description=user_string,
        colour=0xAAD372
    )
    await ctx.respond(embed=new_embed)

@WoWCommands.child
@lightbulb.command('paladin', 'Shows a list with all Paladin players.',auto_defer = True)
@lightbulb.implements(lightbulb.SlashSubCommand)
async def ShowPaladinList(ctx:lightbulb.Context):
    user_string = ""
    for user in CLASS_PALADIN_LIST:
        user_string += str(user) + "\n"
    if user_string == "":
        user_string = "No Paladin player found."

    new_embed = hikari.Embed(
        title='**All Paladin Players**',
        description=user_string,
        colour=0xF48CBA
    )
    await ctx.respond(embed=new_embed)
@WoWCommands.child
@lightbulb.command('priest', 'Shows a list with all Priest players.',auto_defer = True)
@lightbulb.implements(lightbulb.SlashSubCommand)
async def ShowPriestList(ctx:lightbulb.Context):
    user_string = ""
    for user in CLASS_PRIEST_LIST:
        user_string += str(user) + "\n"
    if user_string == "":
        user_string = "No Priest player found."

    new_embed = hikari.Embed(
        title='**All Priest Players**',
        description=user_string,
        colour=0xFFFFFF
    )
    await ctx.respond(embed=new_embed)
@WoWCommands.child
@lightbulb.command('rogue', 'Shows a list with all Rogue players.',auto_defer = True)
@lightbulb.implements(lightbulb.SlashSubCommand)
async def ShowRogueList(ctx:lightbulb.Context):
    user_string = ""
    for user in CLASS_ROGUE_LIST:
        user_string += str(user) + "\n"
    new_embed = hikari.Embed(
        title='**All Rogue Players**',
        description=user_string,
        colour=0xFFF468
    )
    await ctx.respond(embed=new_embed)

@WoWCommands.child
@lightbulb.command('shaman', 'Shows a list with all Shaman players.',auto_defer = True)
@lightbulb.implements(lightbulb.SlashSubCommand)
async def ShowShamanList(ctx:lightbulb.Context):
    user_string = ""
    for user in CLASS_SHAMAN_LIST:
        user_string += str(user) + "\n"
    if user_string == "":
        user_string = "No Shaman player found."

    new_embed = hikari.Embed(
        title='**All Shaman Players**',
        description=user_string,
        colour=0x0070DD
    )
    await ctx.respond(embed=new_embed)

@WoWCommands.child
@lightbulb.command('warlock', 'Shows a list with all Warlock players.',auto_defer = True)
@lightbulb.implements(lightbulb.SlashSubCommand)
async def ShowWarlockList(ctx:lightbulb.Context):
    user_string = ""
    for user in CLASS_WARLOCK_LIST:
        user_string += str(user) + "\n"
    if user_string == "":
        user_string = "No Walock player found."

    new_embed = hikari.Embed(
        title='**All Warlock Players**',
        description=user_string,
        colour=0x8788EE
    )
    await ctx.respond(embed=new_embed)

@WoWCommands.child
@lightbulb.command('warrior', 'Shows a list with all Warrior players.',auto_defer = True)
@lightbulb.implements(lightbulb.SlashSubCommand)
async def ShowWarriorList(ctx:lightbulb.Context):
    user_string = ""
    for user in CLASS_WARRIOR_LIST:
        user_string += str(user) + "\n"
    if user_string == "":
        user_string = "No Warrior player found."

    new_embed = hikari.Embed(
        title='**All Warrior Players**',
        description=user_string,
        colour=0xC69B6D
    )
    await ctx.respond(embed=new_embed)

@WoWCommands.child
@lightbulb.command('monk', 'Shows a list with all Monk players.',auto_defer = True)
@lightbulb.implements(lightbulb.SlashSubCommand)
async def ShowMonkList(ctx:lightbulb.Context):
    user_string = ""
    for user in CLASS_MONK_LIST:
        user_string += str(user) + "\n"
    new_embed = hikari.Embed(
        title='**All Monk Players**',
        description=user_string,
        colour=0x00FF98
    )
    await ctx.respond(embed=new_embed)


def load(bot):
    bot.add_plugin(wow_plugin)