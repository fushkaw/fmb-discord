import disnake
from disnake.ext import commands

class CommandHelp(commands.Cog):
    @commands.slash_command(name="help", description="Помощь")
    async def help(self, ctx):
        embed = disnake.Embed(
            title="Помощь по командам:",
            color=disnake.Colour.yellow())       
        embed.set_author(
            name="FMB",
            url="https://discord.gg/EcwU8Q7VGN",
            icon_url="https://cdn.discordapp.com/attachments/1007634776490000488/1073241752649085018/FMB.png")
        embed.set_footer(
            text="fushka © Copyright 2023",
            icon_url="https://media.discordapp.net/attachments/1007634776490000488/1073242488485195847/4fa220a09bddf43baf713f73bb7ccdec.jpg?width=508&height=508")
        embed.add_field(name="`/stats`", value="Информация о боте", inline=False)
        embed.add_field(name="`/play`", value="Воспроизводит песню (в разработке)", inline=False)
        embed.add_field(name="`/stop`", value="Остонавливает песню", inline=False)
        embed.add_field(name="`/pause`", value="Ставит воспроизведение песни на паузу", inline=False)
        await ctx.send(embed=embed)
        
        @commands.command()
        async def help(self, ctx):
            embed = disnake.Embed(
                title="Помощь по командам:",
                color=disnake.Colour.yellow())
            embed.set_author(
                name="FMB",
                url="https://discord.gg/EcwU8Q7VGN",
                icon_url="https://cdn.discordapp.com/attachments/1007634776490000488/1073241752649085018/FMB.png")
            embed.set_footer(
                text="fushka © Copyright 2023",
                icon_url="https://media.discordapp.net/attachments/1007634776490000488/1073242488485195847/4fa220a09bddf43baf713f73bb7ccdec.jpg?width=508&height=508")
            embed.add_field(name="`/stats`", value="Информация о боте", inline=False)
            embed.add_field(name="`/play`", value="Воспроизводит песню (в разработке)", inline=False)
            embed.add_field(name="`/stop`", value="Остонавливает песню", inline=False)
            embed.add_field(name="`/pause`", value="Ставит воспроизведение песни на паузу", inline=False)
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(CommandHelp(bot))