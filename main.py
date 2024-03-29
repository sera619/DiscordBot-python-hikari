from datetime import datetime
import os, sys
from re import U
import aiohttp
import concurrent.futures

import lightbulb
import hikari
import miru
from hikari import emojis
from lightbulb.ext import tasks
from plugins.config import SERA_DISCORD_ID, SERA_ID, TOKEN, LoadRoleList, SHOW_START_EMBED, COMMON_CHANNEL_ID
LOGO_URL = './image/logo1.png'
from plugins.config import load_bot_setting

class NecroBot:
    def __init__(self, token, discord_id = None, admin_id = None):

        if token == None:
            print("ERROR: SET A DISCORD TOKEN!")
            exit(1)
        self.TOKEN = token
        
        if discord_id != None:
            self.SERA_DISCORD_ID = discord_id
        if admin_id != None:
            self.SERA_ID = admin_id
        
        LoadRoleList()
        
        self.bot = self.configBot()
        self.bot.d.aio_session = None
        self.bot.d.process_pool = None
        
        ################# LOGIN ###################
        @self.bot.listen(hikari.StartedEvent)
        async def start(event: hikari.StartedEvent):
            id = self.bot.get_me()
            global bot
            load  = load_bot_setting()
            """
            """
            if load == True:
                await self.bot.rest.create_message(
                    channel=COMMON_CHANNEL_ID,
                    content='S3R43o3 started...\n'
                    f'Check out bot source code @ ** https://github.com/sera619/DiscordBot-python-hikari **\n\n'
                    f'Plugins loaded:\n'
                    f'**Admin**\n**Commands**\n**Moderator**\n**Music**\n**WoW**\n'
                    f"\nCurrent date & time:\n**{datetime.now().strftime('%m/%d/%Y, %H:%M:%S')}**"
                )

            ### GET ALL CUSTOM EMOJIS ###
            #emojis = await self.bot.rest.fetch_guild_emojis(SERA_DISCORD_ID)
            #for emoji in emojis:
            #    print(emoji.name, emoji.id)
            global CLASS_ROLE_LIST
            CLASS_ROLE_LIST = await self.bot.rest.fetch_roles(SERA_DISCORD_ID)
            #print(CLASS_ROLE_LIST)
            
            return print("started", id)
        
        @self.bot.listen()
        async def on_starting(event: hikari.StartingEvent):
            self.bot.d.aio_session = aiohttp.ClientSession()
            self.bot.d.process_pool = concurrent.futures.ProcessPoolExecutor()

        @self.bot.listen()
        async def on_stopping(event: hikari.StoppingEvent):
            await self.bot.d.aio_session.close()
            self.bot.d.process_pool.shutdown(wait=True)

        @self.bot.command
        @lightbulb.command('botinfo', "Shows Information about Necro BOT.")
        @lightbulb.implements(lightbulb.SlashCommand)
        async def showInformation(ctx: lightbulb.Context):
            plugin_string = ""
            for plugin in self.bot.plugins:
                plugin_string += plugin.capitalize() +"\n"
            new_embed = hikari.Embed(
                title='**S3R43o3 BOT Information**',
                description=f'*Click the title-link above to check out the source code on my Github.*\n\n'
                    f'***PLEASE NOTICE:***\n*If this is your first time running this bot please use the command* **/admin init** to start the first initialization.\n'
                    f'\n\n**Plugins loaded:**\n'
                    f'{plugin_string}'
                    f'\n*For more information about specific plugin commands consult the help section with* **/help "plugin-name"** *(example: /help wow)*\n\n'
                    f"**Current date & time:**\n{datetime.now().strftime('%m/%d/%Y, %H:%M:%S')}",
                colour= 0xFF8800,
                url= "https://github.com/sera619/DiscordBot-python-hikari"
            )
            new_embed.set_thumbnail(LOGO_URL)
            await ctx.respond(embed=new_embed)
            

    def startBot(self):
        self.bot.run(
            status= hikari.Status.IDLE,
            activity= hikari.Activity(
                name="/help",
                type= hikari.ActivityType.WATCHING # --- schaut <name>
        )           
    )

    async def stopBot(self):
        await self.bot.close()

    def configBot(self):
        self.bot = lightbulb.BotApp(
            token=str(self.TOKEN),
            default_enabled_guilds=(int(self.SERA_DISCORD_ID)),
            intents= hikari.Intents.ALL,
            help_slash_command=True,
            ignore_bots=False)
        self.bot.load_extensions("plugins.commands", "plugins.moderator", "plugins.admin", "plugins.WoW", 'plugins.calender', "plugins.linux", "plugins.gamedev")
        tasks.load(self.bot)
        miru.install(self.bot)
        return self.bot


def main():
    load_bot_setting()
    discord_id = SERA_DISCORD_ID
    admin_id = SERA_ID
    token = TOKEN

    bot = NecroBot(token=token, admin_id=admin_id, discord_id=discord_id) 
    
    bot.startBot()

if __name__ == "__main__":
    main()