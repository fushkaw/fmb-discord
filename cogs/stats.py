import disnake
from disnake.ext import commands
import cpuinfo
import time
import psutil

class CommandStats(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="stats", description=f"статистика бота")
    async def stata_command(self, inter: disnake.CommandInteraction):
        await inter.response.defer()
        start = time.time() 
        msg = await inter.original_message()
        svmem = psutil.virtual_memory()
        memory_percent = psutil.virtual_memory().percent
        cpu_percent = psutil.cpu_percent()
        cores = psutil.cpu_count()
        svmem = psutil.virtual_memory()
        memory_percent = psutil.virtual_memory().percent
        members = []
        elapsed = time.time() - start
        for guild in self.bot.guilds:
            for member in guild.members:
                if member.bot == False:
                    if member not in members:
                        members.append(member)
        embed=disnake.Embed(
            title=f"Статистика бота", 
            description=f"\n**Основная информация:**\n"
                        f"Серверов: **{len(self.bot.guilds)}**\n"
                        f"Пользователи: **{len(members)}**\n\n"
                        "**Хостинг:**\n"
                        "Процессор: **Ryzen 9 4.2 Ghz**\n"
                        f"Количество ядер: **{cores}**\n"
                        f"Нагрузка: **{cpu_percent}%**\n"
                        f"ОЗУ: **{round(svmem.used/1000000)}MB / 1GB ({memory_percent}%)**\n"
                        f"Задержка: **{round(self.bot.latency*1000)}ms**\n\n"
                        "**О боте:** \n"
                        "Версия бота: **Alpha v1.0**\n"
                        "Версия python: **3.11.1**\n"
                        "Библиотека: **disnake**\n\n"
                       f"Информация сгенерирована за: {round(elapsed, 2)} sec",
            color=disnake.Colour.yellow())
        embed.set_thumbnail(url='https://media.discordapp.net/attachments/1007634776490000488/1073241752649085018/FMB.png?width=461&height=461')
        embed.set_footer(
            text=f"fushka ©️ Copyright 2023",
            icon_url="https://images-ext-1.discordapp.net/external/rUQnmJj9vqU53D0zLOSycBDhSaowoTO_vMO1r9yiLlo/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/967027636624846858/ade9645339b969bce2049b2b2d62abb0.png"
        )
        await msg.edit(embed=embed)

def setup(bot):
    bot.add_cog(CommandStats(bot))