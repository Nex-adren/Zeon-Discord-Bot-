from discord.ext import commands

user_balances = {}


@commands.command()
async def pay(ctx, money: int):
    if money <= 0:
        await ctx.send("The sum must be greater than zero!")
        return

    user_id = ctx.author.id

    user_balances[user_id] = user_balances.get(user_id, money)

    await ctx.send(f"You have received {money} coins!")


@commands.command()
async def balance(ctx):
    user_id = ctx.author.id
    money = user_balances.get(user_id)

    await ctx.send(f"Balance: {money} coins")