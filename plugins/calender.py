import hikari
import miru
import lightbulb



calendar_plugin = lightbulb.Plugin('calendar', 'Simple calendar system.')
RAID_TERMS_PATH = './data/raid_terms.txt'

base_raid_term = {
    "date": None,
    "time": None,
    "raid": None
}


def SaveRaidTerms(date, time, raid):
    base_raid_term['date'] = str(date)
    base_raid_term['raid'] = str(raid)
    base_raid_term['time'] = str(time)
    print(base_raid_term)

@calendar_plugin.command
@lightbulb.command('calendar', 'All Calendar relevant commands')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def calendarCommands(ctx):
    pass


@calendarCommands.child
@lightbulb.command('show', 'shows the current calendar entrys', auto_defer= True, pass_options = True)
@lightbulb.implements(lightbulb.SlashSubCommand)
async def showCalendar(ctx: lightbulb.Context):
    new_embded = hikari.Embed(
        title='New Calendar',
        description='Your current calendar entrys.'
    )

    await ctx.respond(embed=new_embded)


@calendarCommands.child
@lightbulb.option('time', 'the time the raid starts.', modifier=lightbulb.OptionModifier.CONSUME_REST, required=True, autocomplete=True)
@lightbulb.option('raid', 'wich type of raid to start off', modifier=lightbulb.OptionModifier.CONSUME_REST, required=True, autocomplete=True)
@lightbulb.option('date', 'wich date the raid start', modifier=lightbulb.OptionModifier.CONSUME_REST, required=True, autocomplete=True)
@lightbulb.command('save', 'save new calendar entry', auto_defer = True, pass_options = True)
@lightbulb.implements(lightbulb.SlashSubCommand)
async def saveRaid(ctx: lightbulb.Context, time, raid, date):
    SaveRaidTerms(date,time,raid)
    await ctx.respond('done')




def load(bot):
    bot.add_plugin(calendar_plugin)
