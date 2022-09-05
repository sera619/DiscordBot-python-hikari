import datetime
import hikari
import lightbulb
from .commands import checkAdmin

moderator_plugin = lightbulb.Plugin('moderator', 'All chat moderation relevant')

# Create Base Command Group

@moderator_plugin.command
@lightbulb.command('moderator', 'All chat moderation relevant commands. (Admin only)')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def moderation_commands(ctx):
    pass

# create moderation subcommands

@moderation_commands.child
@lightbulb.option('title', 'The title of the new banner.', modifier=lightbulb.OptionModifier.CONSUME_REST, required=True, autocomplete=True)
@lightbulb.option('text', 'The message of the new banner.', modifier=lightbulb.OptionModifier.CONSUME_REST, required=True, autocomplete=True)
@lightbulb.option('thumbnail', 'Add a thumbnail image to new banner.', modifier=lightbulb.OptionModifier.CONSUME_REST,required=False, autocomplete=True)
@lightbulb.command('banner', 'Create a embed (Banner looklike) message.', auto_defer = True, pass_options = True)
@lightbulb.implements(lightbulb.SlashSubCommand)
async def new_banner(ctx: lightbulb.Context, title: str, text:str, thumbnail:str):
    assert (ctx.get_guild)
    new_embed = hikari.Embed(
        title=title,
        description=text,
    ) 
    if thumbnail is not None:
        new_embed.thumbnail = thumbnail
    await moderator_plugin.bot.rest.create_message(embed=new_embed, channel=ctx.channel_id)
    return await ctx.respond("Banner erstellt")

@moderation_commands.child
@lightbulb.option('amount', 'Select the amount of message to delete', required=True, autocomplete=True, modifier=lightbulb.OptionModifier.CONSUME_REST)
@lightbulb.command('clear', 'Clear text message in channel for given amount', auto_defer = True, pass_options = True)
@lightbulb.implements(lightbulb.SlashSubCommand)
async def clearTextMsg(ctx: lightbulb.Context, amount: str):
    assert (ctx.get_guild)
    isAdmin = await checkAdmin(ctx.author.id, ctx.guild_id)
    if not isAdmin:
        return
    messages = (
        await moderator_plugin.bot.rest.fetch_messages(ctx.channel_id)
        .take_until(lambda m: datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=14) > m.created_at)
        .limit(int(amount) + 2)
    )

    await moderator_plugin.bot.rest.delete_messages(ctx.channel_id, messages)
    return await ctx.respond("Es wurden " + str(amount) + " Nachrichten gelöscht!")




def load(bot):
    bot.add_plugin(moderator_plugin)