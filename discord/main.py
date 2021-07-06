from discord.ext import commands
from sys import argv
bot, code_indicate = commands.Bot(command_prefix='>'), '`' * 3
@bot.command()
async def play(ctx):
    message = await ctx.send(code_indicate + "\n" + code_indicate)
    for i in open(argv[1]).read().split("."): await message.edit(content=code_indicate + "\n" + i + "\n" + code_indicate)
@bot.command()
async def code(ctx): await ctx.send("_main.sh_:\n" + code_indicate + "sh\n" + open(__file__.replace("py", "sh")).read() + code_indicate + "\n_gen.py_:\n" + code_indicate + "py\n" + open(__file__.replace("main", "gen")).read() + code_indicate + "\n_main.py_:" + code_indicate + "py\n" + "".join(open(__file__).readlines()[:-1]) + "bot.run(API_KEY)\n" + code_indicate)
bot.run(API_KEY)
