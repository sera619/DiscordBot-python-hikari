import miru
import hikari
from hikari import emojis
import random

from main import CLASSICONS
from plugins.config import (AddDpsRole,
    AddHpsRole,
    AddTankRole,
    SHOW_START_EMBED,
    WoWClassHandler)

class DiceView(miru.View):
    @miru.select(
        placeholder="Choose a color ...",
        options=[
            miru.SelectOption(label="Red"),
            miru.SelectOption(label="Green"),
            miru.SelectOption(label="Blue")
        ]
    )
    async def slm_colours(self, select: miru.Select, ctx: miru.Context):
        await ctx.respond(f"{select.values[0]} is the color you choosed!")

    # Create button
    @miru.button(emoji='6️⃣', style=hikari.ButtonStyle.PRIMARY)
    async def roll_6_side_button(self, button: miru.Button, ctx: miru.Context):
        roll = random.randint(1, 6)
        await ctx.edit_response(f"You rolled a **{roll}**!")

    @miru.button(label="x 20",emoji="⏹️", style=hikari.ButtonStyle.SUCCESS)
    async def roll_20_side_button(self, button: miru.Button, ctx: miru.Context):
        roll = random.randint(1, 20)
        await ctx.edit_response(f"You rolled a **{roll}**!")

    @miru.button(emoji="❎", style=hikari.ButtonStyle.DANGER)
    async def stop_button(self, button: miru.Button, ctx: miru.Context):
        await ctx.edit_response("Menu was closed", components=[])
        self.stop()
    
    async def on_timeout(self):
        await self.message.edit("The menu timed out.", components=[])
        self.stop()

class StartOptionView(miru.View):
    @miru.button(emoji="✅", style=hikari.ButtonStyle.SECONDARY)
    async def showStartEmbed(self, button: miru.Button, ctx: miru.Context):
        SHOW_START_EMBED = True
        await ctx.edit_response("Zeige Start Nachricht "+str(SHOW_START_EMBED), components=[])

    @miru.button(emoji="❌", style=hikari.ButtonStyle.DANGER)
    async def hideStartEmbed(self, button:miru.Button, ctx: miru.Context):
        SHOW_START_EMBED = False
        await ctx.edit_response("Zeige Start Nachricht: "+str(SHOW_START_EMBED), components=[])

class ClassView(miru.View):
    
    @miru.button(emoji=1017789881029763123,label="Death Knight", style=hikari.ButtonStyle.PRIMARY)
    async def setClassDK(self, button: miru.Button, ctx: miru.Context):
        WoWClassHandler().AddClassDK(new_dps=ctx.user)
        WoWClassHandler().LoadClassDK()
        await ctx.edit_response("You choosed Death Knight Class.", components=[])
        self.stop()

    @miru.button(emoji= 1017789934440026233,label="Demon Hunter", style=hikari.ButtonStyle.PRIMARY)
    async def setClassDH(self, button: miru.Button, ctx: miru.Context):
        WoWClassHandler().AddClassDH(new_dps=ctx.user)
        WoWClassHandler().LoadClassDH()
        await ctx.edit_response("You Choosed DH Class", components=[])
        self.stop()
    
    @miru.button(emoji=1017789969059819541,label="Druid", style=hikari.ButtonStyle.PRIMARY)
    async def setClassDruid(self, button: miru.Button, ctx: miru.Context):
        WoWClassHandler().AddClassDruid(new_dps=ctx.user)
        await ctx.edit_response("You Choosed Druid Class", components=[])
        self.stop()

    @miru.button(emoji=1017790009685852201, label="Hunter", style=hikari.ButtonStyle.PRIMARY)
    async def setClassHunter(self, button: miru.Button, ctx: miru.Context):
        WoWClassHandler().AddClassHunter(new_dps=ctx.user)
        await ctx.edit_response("You Choosed Hunter Class", components=[])
        self.stop()
    
    @miru.button(emoji=1017790054824947753,label="Mage", style=hikari.ButtonStyle.PRIMARY)
    async def setClassDH(self, button: miru.Button, ctx: miru.Context):
        WoWClassHandler().AddClassMage(new_dps=ctx.user)
        await ctx.edit_response("You Choosed Mage Class", components=[])
        self.stop()
    
    @miru.button(emoji=1017790056334889040,label="Monk", style=hikari.ButtonStyle.PRIMARY)
    async def setClassMonk(self, button: miru.Button, ctx: miru.Context):
        WoWClassHandler().AddClassMonk(new_dps=ctx.user)
        await ctx.edit_response("You Choosed Monk Class", components=[])
        self.stop()
    
    @miru.button(emoji=1017790057530265621,label="Paladin", style=hikari.ButtonStyle.PRIMARY)
    async def setClassPaladin(self, button: miru.Button, ctx: miru.Context):
        WoWClassHandler().AddClassPaladin(new_dps=ctx.user)
        await ctx.edit_response("You Choosed Paladin Class", components=[])
        self.stop()

    @miru.button(emoji=1017790058851483720,label="Priest", style=hikari.ButtonStyle.PRIMARY)
    async def setClassPriest(self, button: miru.Button, ctx: miru.Context):
        WoWClassHandler().AddClassPriest(new_dps=ctx.user)
        await ctx.edit_response("You Choosed Priest Class", components=[])
        self.stop()


    @miru.button(emoji=1017790059673563217, label='Rogue', style=hikari.ButtonStyle.PRIMARY)
    async def setClassRogue(self, button: miru.Button, ctx: miru.Context):
        WoWClassHandler().AddClassRogue(new_dps=ctx.user)
        await ctx.edit_response('You choosed Rogue Class.', components=[])
        self.stop()


    @miru.button(emoji=1017790061401620500 ,label="Shaman", style=hikari.ButtonStyle.PRIMARY)
    async def setClassShaman(self, button: miru.Button, ctx: miru.Context,):
        WoWClassHandler().AddClassShaman(new_dps=ctx.user)
        await ctx.edit_response("You Choosed Shaman Class", components=[])
        self.stop()


    @miru.button(emoji=1017790063310024774,label="Warlock", style=hikari.ButtonStyle.PRIMARY)
    async def setClassWarlock(self, button: miru.Button ,ctx: miru.Context):
        WoWClassHandler().AddClassWarlock(new_dps=ctx.user)
        WoWClassHandler().LoadClassWarlock()
        await ctx.edit_response("You Choosed Warlock Class", components=[])
        self.stop()


    @miru.button(emoji=1017790064698343496,label="Warrior", style=hikari.ButtonStyle.PRIMARY)
    async def setClassWarrior(self,button:miru.Button, ctx: miru.Context):
        WoWClassHandler().AddClassWarrior(new_dps=ctx.user)
        await ctx.edit_response("You Choosed Warrior Class", components=[])
        self.stop()
    
    
    async def on_timeout(self):
        await self.message.edit("The classcheck timed out.", components=[])
        self.stop()

class RoleView(miru.View):
    @miru.button(emoji="⚔️", label="DPS", style=hikari.ButtonStyle.DANGER)
    async def choose_dps_role(self, button: miru.Button, ctx: miru.Context):
        new_embed = hikari.Embed(
            title="Character Role Set",
            description=" **You have choose the dps role!**",
            )
        count = 2
        zero = 0
        while zero != count:
            zero += 1
            AddDpsRole(str(ctx.user))
            
        return await ctx.edit_response(embed= new_embed, components=[])

    @miru.button(emoji="💟", label='HPS', style=hikari.ButtonStyle.SUCCESS)
    async def choose_hps_role(self, button: miru.Button, ctx: miru.Context):
        new_embed = hikari.Embed(
            title="Character Role Set",
            description=" **You have choose the hps role!**",
            )
        count = 2
        zero = 0
        while zero != count:
            zero += 1
            AddHpsRole(str(ctx.user))
            
        return await ctx.edit_response(embed= new_embed, components=[])
    
    @miru.button(emoji="🛡️", label='Tank', style=hikari.ButtonStyle.SECONDARY)
    async def choose_tank_role(self, button: miru.Button, ctx: miru.Context):
        new_embed = hikari.Embed(
            title="Character Role Set",
            description=" **You have choose the tank role!**",
            )
        # debbug
        count = 2
        zero = 0
        while zero != count:
            zero += 1
        ####
            AddTankRole(str(ctx.user))
            
        return await ctx.edit_response(embed= new_embed, components=[])
    
    async def on_timeout(self):
        await self.message.edit("The menu timed out.", components=[])
        self.stop()
