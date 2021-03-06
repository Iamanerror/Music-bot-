import discord
import json
impirt os
from discord.ext import commands

bot=commands.Bot(command_prefix='a.')
os.chdir('https://github.com/Iamanerror/Music-bot-/blob/master/Bot.py')

@bot.event
async def on_ready():
   print(bot.user.name) 


@bot.event
async def on_member_join(member):
    with open("users.json", "r") as f:
        users = json.load(f)

        await update_data(users, member)

        with open("users.json", "w") as f:
            json.dump(users, f)

@bot.event
async def on_message(message):
    with open("users.json", "r") as f:
        users = json.load(f)

        if message.author.bot:
            return
        else:
            await update_data(users, message.author)
            number = random.randint(5,10)
            await add_experience(users, message.author, number)
            await level_up(users, message.author, message.channel)

        with open("users.json", "w") as f:
            json.dump(users, f)
    await bot.process_commands(message)

async def update_data(users, user):
    if not user.id in users:
        users[user.id] = {}
        users[user.id]["experience"] = 0
        users[user.id]["level"] = 1

async def add_experience(users, user, exp):
    users[user.id]["experience"] += exp

async def level_up(users, user, channel):
    experience = users[user.id]["experience"]
    lvl_start = users[user.id]["level"]
    lvl_end = int(experience ** (1/4))

    if lvl_start < lvl_end:
        await bot.send_message(channel, f":tada: Congrats {user.mention}, you levelled up to level {lvl_end}!")
        users[user.id]["level"] = lvl_end
        
bot.run(os.environ['BOT_TOKEN'])
