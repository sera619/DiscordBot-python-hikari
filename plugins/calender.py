import hikari
import miru
import lightbulb
import os
import pickle
from main import LOGO_URL


calendar_plugin = lightbulb.Plugin('calendar', 'Simple calendar system.')
RAID_TERMS_PATH = './data/raids/raid_terms-'

base_raid_term = {
    "id":None,
    "date": None,
    "time": None,
    "raid": None,
    "member": []
}


def SaveRaidTerms(id,date, time, raid):
    base_raid_term['id'] = str(id)
    base_raid_term['date'] = str(date)
    base_raid_term['raid'] = str(raid)
    base_raid_term['time'] = str(time)
    base_raid_term['member'] = []
    with open(RAID_TERMS_PATH + str(id) + '.txt', 'wb') as f:
        pickle.dump(base_raid_term, f)

def getRaidMember(raid: dict):
    raid_member = ""
    for member in raid['member']:
        if member == []:
            raid_member = "**Currently no member joined**"
            break
        raid_member += "**"+str(member) + "**, "
    print(raid_member)
    return raid_member

def setRaidMember(id, member):
    raid = LoadRaidTerms(id)
    for mem in raid['member']:
        if mem == member:
            print('Error User exists')
            return False
    raid['member'].append(str(member))
    id = raid['id']

    with open(RAID_TERMS_PATH + str(id) + ".txt", 'wb') as f:
        pickle.dump(raid, f)
    print(f'Member: {str(member)} set to raid: {str(raid["id"])}')
    return True

def LoadRaidTerms(id):
    with open(RAID_TERMS_PATH+str(id)+'.txt','rb') as f:
        loaded_dict = pickle.load(f)
        print(loaded_dict)
        return loaded_dict


@calendar_plugin.command
@lightbulb.command('calendar', 'All Calendar relevant commands')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def calendarCommands(ctx):
    pass


@calendarCommands.child
@lightbulb.option('id', 'The UNIQUE ID for the Raid you looking for.', modifier=lightbulb.OptionModifier.CONSUME_REST, required=True, autocomplete=True)
@lightbulb.command('show', 'shows the current calendar entrys', auto_defer= True, pass_options = True)
@lightbulb.implements(lightbulb.SlashSubCommand)
async def showCalendar(ctx: lightbulb.Context, id):
    raid_term = LoadRaidTerms(str(id))
    id = raid_term['id']
    time = raid_term['time']
    date = raid_term['date']
    raid = raid_term['raid']
    member = getRaidMember(raid_term)
    if member == []:
        member = "No raid member currently joined the raid."
    new_embded = hikari.Embed(
        title='Raid Calendar',
        description='Your current calendar entrys.\n\n'
        f"ID: **{str(id)}**\nTime: **{str(time)}**\nDate: **{str(date)}**\nRaid: **{str(raid)}**\n\nMember: {str(member)}",
        colour=0xFF8800
    )
    new_embded.set_thumbnail(LOGO_URL)
    await ctx.respond(embed=new_embded)
    return

@calendarCommands.child
@lightbulb.option('time', 'Set the time when the raid starts.', modifier=lightbulb.OptionModifier.CONSUME_REST, required=True, autocomplete=True)
@lightbulb.option('raid', 'Set wich type of raid you want to run.', modifier=lightbulb.OptionModifier.CONSUME_REST, required=True, autocomplete=True)
@lightbulb.option('date', 'Set wich date when the raid starts.', modifier=lightbulb.OptionModifier.CONSUME_REST, required=True, autocomplete=True)
@lightbulb.option('id', 'Set a UNIQUE ID for yor Raid, this is needed for member to join the raid at calender.', modifier=lightbulb.OptionModifier.CONSUME_REST, required=True, autocomplete=True)
@lightbulb.command('create', 'Creates a new raid calendar entry', auto_defer = True, pass_options = True)
@lightbulb.implements(lightbulb.SlashSubCommand)
async def saveRaid(ctx: lightbulb.Context, id, time, raid, date):
    SaveRaidTerms(id,date,time,raid)
    new_embed = hikari.Embed(
        title="New raid created!",
        description="New Raid was added to calender!\n\n"
        f"ID: {str(id)}\nRaid: {str(raid)}\nDate: {str(date)}\nTime: {str(time)}",
        colour=0xFF8800
    )
    new_embed.set_thumbnail(LOGO_URL)
    await ctx.respond(embed=new_embed)
    return

@calendarCommands.child
@lightbulb.option('id', 'The UNIQUE ID from the raid you want to join', modifier=lightbulb.OptionModifier.CONSUME_REST, required=True, autocomplete=True)
@lightbulb.command('join', 'Join a raid in the calender', auto_defer= True, pass_options = True)
@lightbulb.implements(lightbulb.SlashSubCommand)
async def joinRaid(ctx: lightbulb.Context, id):
    if setRaidMember(id, str(ctx.author)) == True:
        new_embed = hikari.Embed(
            title='You joined a raid.',
            description=f'The User: **{ctx.author}** successfully joined the raid-id: **{str(id)}**',
            colour=0xFF8800
        )
        new_embed.set_thumbnail(LOGO_URL)
        await ctx.respond(embed=new_embed)
        return
    error_embed = hikari.Embed(
        title='Error: User exists',
        description=f'The user: **{ctx.author}** already exists in raid-id: **{id}**'
    )
    error_embed.set_thumbnail(LOGO_URL)
    await ctx.respond(embed=error_embed)
    return

def load(bot):
    bot.add_plugin(calendar_plugin)
