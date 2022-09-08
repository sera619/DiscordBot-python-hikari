import miru
import hikari
import random

from plugins.config import AddDpsRole, AddHpsRole, AddTankRole, SHOW_START_EMBED

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
