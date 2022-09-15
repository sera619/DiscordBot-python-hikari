from datetime import datetime
import os
import aiohttp
import concurrent.futures

import lightbulb
import hikari
import miru
from hikari import emojis
from lightbulb.ext import tasks
from plugins.config import SERA_DISCORD_ID, SERA_ID, TOKEN, LoadRoleList, SHOW_START_EMBED

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
            """
            """
            if SHOW_START_EMBED == True:
                await self.bot.rest.create_message(
                    channel=979384595114000384,
                    content='NecroBOT started...\n'
                    f'Check out bot source code @ ** https://github.com/sera619/DiscordBot-python-hikari **\n\n'
                    f'Plugins loaded:\n'
                    f'**Admin**\n**Commands**\n**Moderator**\n**Music**\n**WoW**\n'
                    f"\nCurrent date & time:\n**{datetime.now().strftime('%m/%d/%Y, %H:%M:%S')}**"
                )

            ### GET ALL CUSTOM EMOJIS ###
            
            # emojis = await self.bot.rest.fetch_guild_emojis(SERA_DISCORD_ID)
            # for emoji in emojis:
            #     print(emoji.name, emoji.id)


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
        @lightbulb.command('info', "Shows Information about Necro BOT.")
        @lightbulb.implements(lightbulb.SlashCommand)
        async def showInformation(ctx: lightbulb.Context):
            plugin_string = ""
            for plugin in self.bot.plugins:
                plugin_string += plugin +"\n"
            new_embed = hikari.Embed(
                title='**Necro BOT Information**',
                description=f'Check out bot source code @ ** https://github.com/sera619/DiscordBot-python-hikari **\n\n'
                    f'Plugins loaded:\n'
                    f'**{plugin_string}**\n'
                    f"\nCurrent date & time:\n**{datetime.now().strftime('%m/%d/%Y, %H:%M:%S')}**",
                colour= 0xFF8800
            )
            await ctx.respond(embed=new_embed)

    def startBot(self):
        self.bot.run(
            status= hikari.Status.IDLE,
            activity= hikari.Activity(
                name="/help",
                type= hikari.ActivityType.WATCHING # --- schaut <name>
        )           
    )

    def stopBot(self):
        self.bot.close()

    def configBot(self):
        self.bot = lightbulb.BotApp(
            token=str(self.TOKEN),
            default_enabled_guilds=(int(self.SERA_DISCORD_ID)),
            intents= hikari.Intents.ALL,
            help_slash_command=True,
            ignore_bots=False)
        self.bot.load_extensions("plugins.commands", "plugins.moderator", "plugins.admin", "plugins.WoW", 'plugins.calender')
        tasks.load(self.bot)
        miru.load(self.bot)
        return self.bot
        
        
        

def main():
    
    bot.startBot()


if __name__ == '__main__':
    global bot
    bot = None
    try:
        discord_id = SERA_DISCORD_ID
        admin_id = SERA_ID
        token = TOKEN
        bot = NecroBot(token=TOKEN, admin_id=admin_id, discord_id=discord_id) 
        main()
    except KeyboardInterrupt:
        bot.stopBot()
        exit()
    finally:
        print("Bot exited")