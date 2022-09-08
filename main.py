from datetime import datetime
import os
import aiohttp
import concurrent.futures

import lightbulb
import hikari
import miru
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
                    content='Bot started\n'
                    f'Check out ** https://github.com/sera619/DiscordBot-python-hikari **\n\n'
                    f'Plugins loaded:\n'
                    f'**Admin**\n**Commands**\n**Moderator**\n**Music**\n'
                    f"\nAktuelles Datum und Zeit:\n**{datetime.now().strftime('%m/%d/%Y, %H:%M:%S')}**"
                )
            return print("started", id)
        
        @self.bot.listen()
        async def on_starting(event: hikari.StartingEvent):
            self.bot.d.aio_session = aiohttp.ClientSession()
            self.bot.d.process_pool = concurrent.futures.ProcessPoolExecutor()

        @self.bot.listen()
        async def on_stopping(event: hikari.StoppingEvent):
            await self.bot.d.aio_session.close()
            self.bot.d.process_pool.shutdown(wait=True)


    def startBot(self):
        self.bot.run(
            status= hikari.Status.IDLE,
            activity= hikari.Activity(
                name="nach geilen Bots",
                type= hikari.ActivityType.WATCHING # --- schaut <name>
        )           
    )


    def configBot(self):
        self.bot = lightbulb.BotApp(
            token=str(self.TOKEN),
            default_enabled_guilds=(int(self.SERA_DISCORD_ID)),
            intents= hikari.Intents.ALL,
            help_slash_command=True,
            ignore_bots=True)
        self.bot.load_extensions("plugins.commands", "plugins.moderator", "plugins.music", "plugins.admin")
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
        exit()
    finally:
        print("Bot exited")