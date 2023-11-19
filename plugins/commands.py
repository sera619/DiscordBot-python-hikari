import hikari
import miru
import lightbulb
import os



from dist.customviews import DiceView, RoleView
plugin = lightbulb.Plugin('commands')
global CONTROL_CHANNEL
CONTROL_CHANNEL = None


async def checkAdmin(member_id, guild) -> bool: 
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
    if event.author_id == 1081224695770271894 or not event.content:
        return
    #is_admin = await checkAdmin(member_id=event.author_id, guild=event.guild_id)
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
        await view.start(message)
        await view.wait()
        return print("Rolecheck done!")


    if event.content == 'whoami':
        embed = hikari.Embed(
            title = "**Who am i?**",
            description= f"Characteristics:\n"+
            f"**Name:** S3R43o3\n"+
            f"**Description**: Soziopath, Misantroph and a Hacker since the early 90's. Member and Cyberwarrior of Anonymous. Experience in more than 4500 hacked machines. Top 100 www.TryHackme.com CTF Player.\n\n"
            f"**Job:** Black Hat Hacker, Gamedeveloper, FullStack Developer\n"+
            f"**Skill-Set:** BASH, C, C++, C#, CSS/SASS, Dart, GDScript, GO, HTML, Java, JavaScript, Kotlin, Markdown, Pearl, PHP, Python, PowerShell, R, Ruby, Swift, SQL, XML and others.\n"+
            f"**OS:** Kali Linux, Fedora, Parrot, Windows\n"+
            f"**Social Links:**"+
            f"\n\tTry Hack Me:\n\thttps://tryhackme.com/p/S3R43o3"+
            f"\n\tYoutube:\n\thttps://www.youtube.com/@S3R43o3"+
            f"\n\tGithub:\n\thttps://www.github.com/sera619"+
            f"\n\tCodepen:\n\thttps://codepen.io/sera619\n"+
            f"**\"No system is safe. Expect us!\"**",
            color=hikari.Color.from_rgb(255, 0, 0)
        )
        embed.set_thumbnail("./image/blackhat.png")
        return await event.message.respond(embed=embed)
    # if event.content != "buttons" and event.content != 'classcheck' and event.content != "rolecheck":
    #     if is_admin:
    #         return await plugin.bot.rest.create_message(content="Your are a Admin",channel= event.channel_id)
    #     else:
    #         return await plugin.bot.rest.create_message(content="You are not a Admin.", channel=event.channel_id)

############# CREATE CHAT COMMANDS ############
@plugin.command
@lightbulb.command('ping', 'Say pong!')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await plugin.bot.update_presence(
        status=hikari.Status.ONLINE,
        activity=hikari.Activity(
            name="S3R43o3",
            type=hikari.ActivityType.COMPETING
        )
    )
    await ctx.respond('Presence updated!')



# load function required by lightbulb
def load(bot):
    bot.add_plugin(plugin)