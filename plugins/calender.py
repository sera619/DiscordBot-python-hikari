import hikari
import miru
import lightbulb



calendar_plugin = lightbulb.Plugin('calendar', 'Simple calendar system.')


@calendar_plugin.command
@lightbulb.command('calendar', 'All Calendar relevant commands')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def calendarCommands(ctx):
    pass


@calendarCommands.child
@lightbulb.command('show', 'shows the current calendar entrys')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def showCalendar(ctx: lightbulb.Context):
    new_embded = hikari.Embed(
        title='New Calendar',
        description='Your current calendar entrys.'
    )

    await ctx.respond(embed=new_embded)







def load(bot):
    bot.add_plugin(calendar_plugin)
