import lightbulb
import hikari
from .commands import checkAdmin

linux_plugin = lightbulb.Plugin('linux','Helps with linux usage')
LINUX_BASIC_COMMANDS= [
    "strg + c -- Bricht den Vorgang in der Shell ab -- strg + c ",
    "d [Verzeichnis] -- in ein beliebiges Verzeichnis -- cd /media/disk",
    "cd .. -- Wechselt ein Verzeichnis zurück (/media/disk -> /media) -- cd ../",
    "cd / -- Wechselt in das tiefste Verzeichnis -- cd /",
    "cd – -- Wechselt in das zuletzt besuchte Verzeichnis -- cd –",
    "cp -- Kopiert eine Datei in das angegebene Verzeichnis -- cp /tmp/test.txt /media/disk",
    "mv -- Verschiebt eine Datei und löscht die Quelldatei -- mv /tmp/bla.txt /media/disk",
    "mv -- Benennt auch Dateien um 	mv /tmp/x1.txt /tmp/x3.txt",
    "rm -- Löscht eine Datei -- rm /tmp/bla.txt",
    "rm -rf -- Löscht alles in dem Verzeichnis 	rm -rf /tmp/",
    "mkdir -- Erstellt ein Verzeichnis -- mkdir /media/disk/bla",
    "rmdir -- Löscht ein Verzeichnis -- rmdir /media/disk/bla",
    "ls -- Zeigt alle Dateien in einem Ordner an -- ls /home/ubuntu",
    "ls -l -- Zeigt eine ausführliche Liste, mit ausführlichen Rechten an -- ls -l /home/ubuntu",
    "ls -la -- Zeigt auch versteckte Dateien an -- ls -la /home/ubuntu",
    "pwd -- Zeigt den Pfad zum aktuellen Verzeichnis -- pwd",
    "cat -- Zeigt Inhalt einer Textdatei an -- cat /home/test.txt",
    "more -- Zeigt Inhalt einer Datei seitenweise an -- more test.txt",
    "touch -- Erstellt eine leere Datei in einem beliebigen Ordner -- touch /ubuntu/123.txt",
]
LINUX_INSTALL_COMMANDS = [
    "apt-get install\n\tinstalliert ein Paket [root-Rechte benötigt]\napt-get install [Paketname]",
    "apt-get remove\n\tDeinstalliert ein Paket [root-Rechte benötigt]\napt-get remove [Paketname]",
    "apt-get update\n\tAktualisiert die Liste der Verfügbaren Pakete\napt-get update",
    "apt-get upgrade\n\tBringt das System auf den neusten Stand.\napt-get upgrade",
    "apt-get autoremove\n\tentfernt alle nicht mehr benötigten Pakete [root-Rechte benötigt]\napt-get autoremove",
    "apt-cache search\n\t Sucht nach Paketen",
]

FLASK_START = [
    "In das verzeichnis **h2**",
    "Befehle nacheinander einegeben:",
    "source env-h2/bin/activate",
    "export FLASK_ENV=development",
    "export FLASK_APP=app.py",
    "export FLASK_DEBUG=1",
    "flask run",
]


@linux_plugin.command
@lightbulb.command('linux', 'All linux commands.')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def linux_commands(ctx):
    pass

@linux_commands.child
@lightbulb.command('basic', 'Basic Terminal commands.', auto_defer=True, pass_options = True)
@lightbulb.implements(lightbulb.SlashSubCommand)
async def linux_basic(ctx: lightbulb.Context):
    coms = "**Linux Basiccommands:**\nHier sind die Basic-Commands. Formatierung:\n\n **Command** -- **Info** -- **Beispiel **\n\n"
    for command in LINUX_BASIC_COMMANDS:
        coms += f"{command}" +'\n'
    e = hikari.Embed(
        title="Linux - Basiccommands",
        description=coms
    )
    e.set_thumbnail('./image/logo1.png')
    return await ctx.respond(embed=e)


@linux_commands.child
@lightbulb.command('flask', 'Run flask on linux.', auto_defer=True, pass_options = True)
@lightbulb.implements(lightbulb.SlashSubCommand)
async def flask_start(ctx: lightbulb.Context):
    coms = "**Flask - Hackerhomepage starten:**\n\n"
    for command in FLASK_START:
        coms += f"{command}"+ '\n' 
    coms += f'\nUm das env zu verlassen:\n\nCtrl+C in der Konsole um Flask zubeenden.\nIm Terminal deactivate eingeben\n\nViel Spaß! =)'
    e = hikari.Embed(
        title="Flask - Basiccommands",
        description=coms
    )
    e.set_thumbnail('./image/logo1.png')
    return await ctx.respond(embed=e)


@linux_commands.child
@lightbulb.command('install', 'Install Terminal commands.', auto_defer=True, pass_options = True)
@lightbulb.implements(lightbulb.SlashSubCommand)
async def linux_install(ctx: lightbulb.Context):
    coms = "**Linux Basiccommands:**\nHier sind die Install-Commands. Formatierung:\n\n **Command**\n**Info**\n**Beispiel **\n\n"
    for command in LINUX_INSTALL_COMMANDS:
        coms += f"{command}" +'\n\n'
    e = hikari.Embed(
        title="Linux - Installcommands",
        description=coms
    )
    e.set_thumbnail('./image/logo1.png')
    return await ctx.respond(embed=e)


def load(bot):
    bot.add_plugin(linux_plugin)