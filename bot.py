import disnake
from disnake.ext import commands
import os
import asyncio
from config import settings

class PersistentViewBot(commands.Bot): 
    def __init__(self): 
        super().__init__(command_prefix=settings['prefix'], intents=disnake.Intents().all(), activity=disnake.Activity(type=disnake.ActivityType.listening, name="музыку") ) 
        self.persistent_views_added = False
    async def on_ready(self):
        if not self.persistent_views_added:
            
            self.persistent_views_added = True
        print(f"=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\nБот запущен\nName: {bot.user.name}#{bot.user.discriminator}\nID: {bot.user.id}\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

bot = PersistentViewBot()
bot.remove_command("help")

list_cogs = []
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension("cogs." + filename[:-3])
        list_cogs.append(filename[:-3])


@bot.slash_command(description='Загрузить модуль бота')
@commands.has_role(1072894643458551878)
async def load(inter: disnake.CommandInteraction, module: str = commands.Param(name="module", description="Название модуля")):
    bot.load_extension(f"cogs.{module}")
    await inter.response.send_message(f"Загружен модуль `{module}`",ephemeral=True)

@bot.slash_command(description='Выгрузить модуль бота')
@commands.has_role(1072894643458551878)
async def unload(inter: disnake.CommandInteraction, module: str = commands.Param(name="module", description="Название модуля", choices=list_cogs)):
    bot.unload_extension(f"cogs.{module}")
    await inter.response.send_message(f"Выгружен модуль `{module}`",ephemeral=True)
    
@bot.slash_command(description="Перезагрузить модуль бота")
@commands.has_role(1072894643458551878)
async def reload(inter: disnake.CommandInteraction, module: str = commands.Param(name="module", description="Название модуля", choices=list_cogs)):
    bot.reload_extension(f"cogs.{module}")
    await inter.response.send_message(f"Перезагружен модуль `{module}`",ephemeral=True)


bot.run(settings['token'])