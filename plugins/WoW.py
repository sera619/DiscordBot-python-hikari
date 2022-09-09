from msilib.schema import Icon
import hikari
import lightbulb
import os
import miru
from dist.customviews import ClassView
from plugins.config import SERA_DISCORD_ID

wow_plugin = lightbulb.Plugin('wow', 'World of Warcraft Features')
   

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



def load(bot):
    bot.add_plugin(wow_plugin)