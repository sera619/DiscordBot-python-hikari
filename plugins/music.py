import hikari
import lightbulb
import os
from dotenv import load_dotenv
from .commands import SERA_ID
from songbird import ytdl, Driver

music_plugin = lightbulb.Plugin('music', "Musicbot relevant commands")



async def _join(ctx: lightbulb.Context):
    assert ctx.guild_id is not None

    states = music_plugin.bot.cache.get_voice_states_view_for_guild(ctx.guild_id)
    voice_state = [ state async for state in states.iterator().filter(lambda i: i.user_id == ctx.author.id)]
    
    # check if user is in voice channel
    if not voice_state:
        embed = hikari.Embed(title="**YOU ARE NOT IN A VOICE CHANNEL**", colour=0xC80000)
        await ctx.respond(embed=embed)
        return None

    channel_id = voice_state[0].channel_id

    await music_plugin.bot.update_voice_state(ctx.guild_id, channel_id, self_deaf=True, self_mute=False)

    return channel_id

@music_plugin.command
@lightbulb.option('url',' Youtube URL of the song', required=True,  modifier=lightbulb.OptionModifier.CONSUME_REST, required=True, autocomplete=True)
@lightbulb.command('play','Play a song from youtube.', auto_defer = True, pass_options = True)
@lightbulb.implements(lightbulb.SlashSubCommand)
async def playSong(ctx: lightbulb.Context):
    channel_id = await _join(ctx)
    


@music_plugin.command
@lightbulb.command('join', 'Joins your voicechannel', auto_defer = True)
@lightbulb.implements(lightbulb.SlashCommand)
async def join(ctx: lightbulb.Context):
    channel_id = await _join(ctx)
    if channel_id:
        embed = hikari.Embed(
            title="**Joined voice channel.**",
            colour=ctx.author.accent_color
            )
        await ctx.respond(embed=embed)

@music_plugin.command
@lightbulb.command('leave', 'Leave the current connected voice channel', auto_defer = True, aliases=['stop'])
@lightbulb.implements(lightbulb.SlashCommand)
async def leave(ctx: lightbulb.Context):
    assert (ctx.get_guild)
    
    states = music_plugin.bot.cache.get_voice_states_view_for_guild(ctx.guild_id)
    voice_state = [state async for state in states.iterator().filter(lambda i: i.user_id == ctx.author.id)]

    if not voice_state:
        embed = hikari.Embed(title='**Your are not in a voice channel.**', colour = ctx.author.id)
        await ctx.respond(embed=embed)
        return
    
    if ctx.guild_id is not None:
        await music_plugin.bot.update_voice_state(ctx.guild_id, None)

    embed = hikari.Embed(title='**Stopped music bot and left voice channel.**', color= ctx.author.accent_color)
    await ctx.respond(embed=embed)















def load(bot):
    bot.add_plugin(music_plugin)