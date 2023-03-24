import disnake
from disnake.ext import commands
import aiohttp

class CommandRolePlay(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="kiss", description=f"Поцеловать человека")
    async def kiss_command(self, inter: disnake.CommandInteraction, member: disnake.Member = commands.Param(name="пользователь", description="Выберите пользователя")):
        async with aiohttp.request("GET", "https://api.waifu.pics/sfw/kiss") as resp:
            pizda_ebanaya = await resp.json()
        if member.id == inter.author.id:
                await inter.response.send_message("Поцеловать самого себя, серьезно?", ephemeral=True)
        await inter.response.defer()
        msg = await inter.original_message()
        kiss_embed = disnake.Embed(
            title="", 
            description=f"{inter.author.mention} **целует** {member.mention} \nПравдо это мило?", 
            color=0x2F3136
        )
        kiss_embed.set_image(url=pizda_ebanaya['url'])
        await msg.edit(embed = kiss_embed)

    @commands.slash_command(name='kill', description=f'Убить себя или другого пользователя')
    async def kill_command(self, inter: disnake.CommandInteraction, member: disnake.Member = commands.Param(name="пользователь", description="Выберите пользователя")):
        async with aiohttp.request("GET", "https://api.waifu.pics/sfw/kill") as resp:
            pizda_ebanaya = await resp.json()
        if member.id == inter.author.id:
            await inter.response.send_message("Подумай о родителях!!", ephemeral=True)
        await inter.response.defer()
        msg = await inter.original_message()
        kill_embed = disnake.Embed(
            title="", 
            description=f"{inter.author.mention} **жестоко убивает** {member.mention} \nТы убийца", 
            color=0x2F3136
        )
        kill_embed.set_image(url=pizda_ebanaya['url'])
        await msg.edit(embed = kill_embed)

def setup(bot):
    bot.add_cog(CommandRolePlay(bot))