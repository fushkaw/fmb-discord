import disnake
from disnake.ext import commands

class CommandClear(commands.Cog):
    def __init__(self, bot):
        self.persistent_views_added=False
        self.bot = bot
        
    @commands.command(name="clear", description="Удаляет сообщения")
    @commands.has_permissions(manage_messages=True)
    async def clear_command(self, inter: disnake.CommandInteraction, amount: int = commands.Param(name="amount", description="Количество сообщений для очистки")):
        try:
            if amount <= 0:
                msg = await inter.response.send_message(embed=disnake.Embed(description=f"Вы указали неверные аргументы!"), delete_after=60)
            if amount > 0:
                await inter.channel.purge(limit=amount)
                msg = await inter.response.send_message(embed=disnake.Embed(description=f"Вы очистили `{amount}` сообщений"), delete_after=60)
        except Exception as e:
            await inter.response.send_message(embed=disnake.Embed(
                title=f"Произошла ошибка при попытке отчистить {amount} сообщений", 
                description=f"Причины возникновения ошибки:\n- У вас недостаточно прав\n-У меня недостаточно прав\n- Вы указали не верные аргументы\nВозможные способы решения:\n- Проверьте есть ли у меня право на управление сообщениями", 
                color=0x2F3136), 
                delete_after=60
            )

def setup(bot):
    bot.add_cog(CommandClear(bot))