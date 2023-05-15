import lightbulb
import hikari
from .commands import checkAdmin


GAMECOMMANDS =[
    "**WASD** - Movement",
    "**WASD + Shift** - Run",
    "**Space** - Normal Attack",
    "**Q** - Double Attack",
    "**R** - Special Attack",
    "**F** - Take/Stick Sword (Combatstance)",
    "**E** - Interact",
    "**ESC** - Ingame Pause/Menu",
    "**F1** - Quicksave"
]


gamedev_plugin = lightbulb.Plugin('gamedev','Help Devs with my Gameproject')
@gamedev_plugin.command
@lightbulb.command('gamedev', 'All Gamedev commands.')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def gamedev_commands(ctx):
    pass

@gamedev_commands.child
@lightbulb.command('keys', 'Ingame Keyboard Settings.', auto_defer=True, pass_options = True)
@lightbulb.implements(lightbulb.SlashSubCommand)
async def linux_basic(ctx: lightbulb.Context):
    coms = "**Game Ingame Keysettings:**\nHier sind die Ingame-Keyboardsettings, Formatierung:\n\n **Key** - **Action**\n\n"
    for command in GAMECOMMANDS:
        coms += f"{command}" +'\n'
    e = hikari.Embed(
        title="Game - Basiccommands",
        description=coms
    )
    e.set_thumbnail('./image/logo1.png')
    return await ctx.respond(embed=e)

@gamedev_commands.child
@lightbulb.command('info', 'Information about my Gameproject', auto_defer=True, pass_options = True)
@lightbulb.implements(lightbulb.SlashSubCommand)
async def linux_basic(ctx: lightbulb.Context):
    coms = (f"**Gameproject Informationen:**\nHier die allgemeinen Informationen:\n\n"+
        f"Das Spiel wird in der Godot Engine 4 entwickelt. Ein Action-RPG im Style des Klassikers _Secret of Mana_ für das _Super Nintendo Entertainment System_.\n"+
        f"Die Grafik ist daher in _2D Pixelart_. Viele typische Elemente wie Quests, unterschiedliche Welten mit Dungeons und Monstern.\n"+
        f"Ein Kampfsystem mit verschiedenen Angriffen und Zaubern. Das Projekt ist noch in einer frühen Phase und daher noch nicht vollständig.\n\n"+
        f"Das Spiel ist auf Github zu finden:\n*https://www.github.com/sera619/Godot4-RPG*\n")
    e = hikari.Embed(
        title="Game - Informationen",
        description=coms
    )
    e.set_thumbnail('./image/logo1.png')
    return await ctx.respond(embed=e)



def load(bot):
    bot.add_plugin(gamedev_plugin)